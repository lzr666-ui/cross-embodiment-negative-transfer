# Cross-Embodiment Negative Transfer

Preliminary experiments for studying when cross-embodiment robot data hurts target-domain policy learning.

## Research Question

When does cross-embodiment data hurt target robot policy learning, and how can body-aware routing mitigate this negative transfer?

## Current Findings

- Naive franka+piper mixing hurts franka target-domain validation performance.
- Piper and aloha-agilex are high-conflict source embodiments for franka.
- A lightweight body-aware conflict score captures state/action mismatch.
- Conflict-aware source downweighting reduces target validation loss compared with naive mixing.

## Main Results

| Setting | Mean target-val loss |
|---|---:|
| Target-only | 0.378 |
| Routed franka+piper5 | 1.669 |
| Naive franka+piper50 | 2.647 |

Naive mixing increases target-domain validation loss by **7.00x** compared with target-only training.  
Body-aware routing reduces the naive-mixing loss by **37.0%**.

## Conflict Scores

| Target | Source | Conflict score | Source-only loss | Naive mix loss |
|---|---|---:|---:|---:|
| franka | piper | 16.038 | 7.152 | 2.775 |
| franka | aloha-agilex | 15.272 | 13.895 | 3.118 |

## Repository Structure

```text
scripts/
  compute_conflict_score.py
  eval_target_val_loss.py
  route_by_conflict.py

exp_logs/
  beat_block_hammer/
    seed1_summary.md
    seed0_summary.md
    body_aware_conflict_routing_method.md
    paper_outline.md
    seed0_seed1_seed2_comparison.md
    seed2_summary.md
    body_aware_routing_rule.md
