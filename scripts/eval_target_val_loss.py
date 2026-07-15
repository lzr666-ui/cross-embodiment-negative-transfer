import argparse
import sys
import torch

from act_policy import ACTPolicy
from utils import load_data, compute_dict_mean, set_seed


def make_policy(policy_config):
    return ACTPolicy(policy_config)


def forward_pass(data, policy):
    image_data, qpos_data, action_data, is_pad = data
    image_data = image_data.cuda()
    qpos_data = qpos_data.cuda()
    action_data = action_data.cuda()
    is_pad = is_pad.cuda()
    return policy(qpos_data, image_data, action_data, is_pad)


def eval_target_val_loss(args):
    set_seed(args.seed)

    camera_names = args.camera_names.split(",")

    policy_config = {
        "lr": args.lr,
        "num_queries": args.chunk_size,
        "kl_weight": args.kl_weight,
        "hidden_dim": args.hidden_dim,
        "dim_feedforward": args.dim_feedforward,
        "lr_backbone": args.lr_backbone,
        "backbone": args.backbone,
        "enc_layers": args.enc_layers,
        "dec_layers": args.dec_layers,
        "nheads": args.nheads,
        "camera_names": camera_names,
        "state_dim": args.state_dim,
    }

    print("==== Offline Target Validation ====")
    print("ckpt:", args.ckpt_path)
    print("eval dataset:", args.eval_dataset)
    print("num episodes:", args.num_episodes)
    print("camera names:", camera_names)
    print("state_dim:", args.state_dim)

    _, val_dataloader, _, _ = load_data(
        args.eval_dataset,
        args.num_episodes,
        camera_names,
        args.batch_size,
        args.batch_size,
    )

    old_argv = sys.argv
    sys.argv = [
        "eval_target_val_loss.py",
        "--ckpt_dir", "tmp_eval_ckpt",
        "--policy_class", "ACT",
        "--task_name", "beat_block_hammer",
        "--seed", str(args.seed),
        "--num_epochs", "1",
        "--state_dim", str(args.state_dim),
        "--kl_weight", str(args.kl_weight),
        "--chunk_size", str(args.chunk_size),
        "--hidden_dim", str(args.hidden_dim),
        "--dim_feedforward", str(args.dim_feedforward),
        "--lr", str(args.lr),
        "--lr_backbone", str(args.lr_backbone),
        "--backbone", str(args.backbone),
        "--enc_layers", str(args.enc_layers),
        "--dec_layers", str(args.dec_layers),
        "--nheads", str(args.nheads),
        "--camera_names", ",".join(camera_names),
    ]

    policy = make_policy(policy_config)

    sys.argv = old_argv
    ckpt = torch.load(args.ckpt_path, map_location="cpu")
    loading_status = policy.load_state_dict(ckpt)
    print("loading_status:", loading_status)
    policy.cuda()
    policy.eval()

    epoch_dicts = []
    with torch.inference_mode():
        for batch_idx, data in enumerate(val_dataloader):
            forward_dict = forward_pass(data, policy)
            epoch_dicts.append(forward_dict)

    summary = compute_dict_mean(epoch_dicts)

    print("\n==== Result ====")
    for k, v in summary.items():
        if torch.is_tensor(v):
            print(f"{k}: {v.item():.6f}")
        else:
            print(f"{k}: {v}")

    print("\nTarget-val loss:", float(summary["loss"]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--ckpt_path", required=True)
    parser.add_argument("--eval_dataset", required=True)
    parser.add_argument("--num_episodes", type=int, default=50)

    parser.add_argument("--camera_names", type=str, default="cam_high,cam_left_wrist,cam_right_wrist")
    parser.add_argument("--batch_size", type=int, default=8)

    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--state_dim", type=int, default=16)

    parser.add_argument("--lr", type=float, default=1e-5)
    parser.add_argument("--lr_backbone", type=float, default=1e-5)
    parser.add_argument("--kl_weight", type=int, default=10)
    parser.add_argument("--chunk_size", type=int, default=100)
    parser.add_argument("--hidden_dim", type=int, default=512)
    parser.add_argument("--dim_feedforward", type=int, default=3200)
    parser.add_argument("--backbone", type=str, default="resnet18")
    parser.add_argument("--enc_layers", type=int, default=4)
    parser.add_argument("--dec_layers", type=int, default=7)
    parser.add_argument("--nheads", type=int, default=8)

    args = parser.parse_args()
    eval_target_val_loss(args)
