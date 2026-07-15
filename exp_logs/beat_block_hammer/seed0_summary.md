# Seed 0 Summary: Cross-Embodiment Negative Transfer

## Setup

- Environment: RoboTwin2.0
- Policy: ACT
- Task: beat_block_hammer
- Target embodiment: franka
- Source embodiment: piper
- Alignment: zero-padding piper state/action from 14D to 16D
- Evaluation: offline target-domain validation loss on franka validation set
- State dim: 16
- Chunk size: 50
- Seed: 0

## Main Results

| Method | Train data | Source ratio | Target-val loss | Relative |
|---|---|---:|---:|---:|
| Target-only | franka 50 | 0% | 0.396934 | 1.00x |
| Routed mix | franka 50 + piper 5 | 9.1% | 1.603187 | 4.04x |
| Routed mix | franka 50 + piper 10 | 16.7% | 2.614141 | 6.59x |
| Routed mix | franka 50 + piper 25 | 33.3% | 2.601172 | 6.55x |
| Naive mix | franka 50 + piper 50 | 50.0% | 2.946190 | 7.42x |
| Source-only | piper 50 | 100% | 7.151734 | 18.02x |

## Conflict Score

| Target | Source | dim gap | qpos mean gap | qpos std gap | action mean gap | action std gap | Conflict score |
|---|---|---:|---:|---:|---:|---:|---:|
| franka | piper | 2.000 | 5.482 | 1.536 | 5.482 | 1.537 | 16.038 |

## Interpretation

Naive franka+piper mixing significantly increases franka target-domain validation loss compared with the franka-only baseline. Piper-only transfer performs worst, suggesting that piper is a high-conflict source embodiment for franka under weak zero-padding alignment.

Conflict-aware downweighting partially mitigates negative transfer. Reducing the piper source ratio from 50.0% to 9.1% decreases target-val loss from 2.946190 to 1.603187, corresponding to a 45.6% reduction.

## Current Limitation

- Only seed 0 has been evaluated.
- Only one source embodiment is used: piper.
- Only one task is used: beat_block_hammer.
- Evaluation uses offline validation loss, not closed-loop success rate.
- Policy is ACT, not yet pi0-style VLA.
