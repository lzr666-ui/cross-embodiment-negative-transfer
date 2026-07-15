import argparse
import math


def route_by_conflict(conflict_score, low_threshold, high_threshold):
    if conflict_score <= low_threshold:
        level = "low"
        source_ratio = 0.50
        decision = "keep source data"
    elif conflict_score <= high_threshold:
        level = "medium"
        source_ratio = 0.25
        decision = "moderately downweight source data"
    else:
        level = "high"
        source_ratio = 0.10
        decision = "strongly downweight source data"

    soft_weight = math.exp(-conflict_score / high_threshold)

    return {
        "conflict_level": level,
        "recommended_source_ratio": source_ratio,
        "soft_source_weight": soft_weight,
        "decision": decision,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=str, default="franka")
    parser.add_argument("--source", type=str, default="piper")
    parser.add_argument("--conflict_score", type=float, required=True)
    parser.add_argument("--low_threshold", type=float, default=5.0)
    parser.add_argument("--high_threshold", type=float, default=10.0)
    parser.add_argument("--target_episodes", type=int, default=50)

    args = parser.parse_args()

    result = route_by_conflict(
        args.conflict_score,
        args.low_threshold,
        args.high_threshold,
    )

    source_episodes = round(
        args.target_episodes
        * result["recommended_source_ratio"]
        / (1 - result["recommended_source_ratio"])
    )

    total_episodes = args.target_episodes + source_episodes
    actual_ratio = source_episodes / total_episodes

    print("==== Body-Aware Routing Decision ====")
    print(f"target: {args.target}")
    print(f"source: {args.source}")
    print(f"conflict_score: {args.conflict_score:.6f}")
    print(f"conflict_level: {result['conflict_level']}")
    print(f"decision: {result['decision']}")
    print()
    print(f"target_episodes: {args.target_episodes}")
    print(f"recommended_source_episodes: {source_episodes}")
    print(f"total_episodes: {total_episodes}")
    print(f"actual_source_ratio: {actual_ratio * 100:.2f}%")
    print()
    print(f"soft_source_weight: {result['soft_source_weight']:.6f}")

    print("\nSuggested dataset name:")
    print(f"mix_{args.target}_{args.source}_{total_episodes}")


if __name__ == "__main__":
    main()
