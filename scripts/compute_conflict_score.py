import h5py
import glob
import numpy as np
import argparse


def load_vectors(data_dir, key):
    files = glob.glob(f"{data_dir}/**/*.hdf5", recursive=True)
    xs = []

    for f in files:
        with h5py.File(f, "r") as h:
            if key not in h:
                continue
            x = h[key][:]
            if x.ndim == 2:
                xs.append(x)

    if len(xs) == 0:
        raise RuntimeError(f"No data found for key={key} in {data_dir}")

    return np.concatenate(xs, axis=0)


def pad_to_same_dim(x, y):
    dim = max(x.shape[-1], y.shape[-1])

    def pad(z):
        if z.shape[-1] == dim:
            return z
        pad_width = dim - z.shape[-1]
        return np.pad(z, ((0, 0), (0, pad_width)), mode="constant")

    return pad(x), pad(y)


def stat_gap(x, y):
    x, y = pad_to_same_dim(x, y)

    mean_gap = np.linalg.norm(x.mean(axis=0) - y.mean(axis=0))
    std_gap = np.linalg.norm(x.std(axis=0) - y.std(axis=0))

    return mean_gap, std_gap


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target_dir", required=True)
    parser.add_argument("--source_dir", required=True)
    parser.add_argument("--target_dim", type=int, default=16)
    parser.add_argument("--source_dim", type=int, default=14)

    args = parser.parse_args()

    qpos_t = load_vectors(args.target_dir, "observations/qpos")
    qpos_s = load_vectors(args.source_dir, "observations/qpos")

    act_t = load_vectors(args.target_dir, "action")
    act_s = load_vectors(args.source_dir, "action")

    qpos_mean_gap, qpos_std_gap = stat_gap(qpos_t, qpos_s)
    act_mean_gap, act_std_gap = stat_gap(act_t, act_s)

    dim_gap = abs(args.target_dim - args.source_dim)

    conflict_score = (
        dim_gap
        + qpos_mean_gap
        + qpos_std_gap
        + act_mean_gap
        + act_std_gap
    )

    print("==== Body-aware Conflict Score ====")
    print("target:", args.target_dir)
    print("source:", args.source_dir)
    print()
    print(f"dim_gap: {dim_gap:.6f}")
    print(f"qpos_mean_gap: {qpos_mean_gap:.6f}")
    print(f"qpos_std_gap: {qpos_std_gap:.6f}")
    print(f"action_mean_gap: {act_mean_gap:.6f}")
    print(f"action_std_gap: {act_std_gap:.6f}")
    print()
    print(f"conflict_score: {conflict_score:.6f}")


if __name__ == "__main__":
    main()
