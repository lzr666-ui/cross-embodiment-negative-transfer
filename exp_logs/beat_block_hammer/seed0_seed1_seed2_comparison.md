# Seed 0/1/2 Comparison

## Setup

| Item | Setting |
|---|---|
| Environment | RoboTwin2.0 |
| Policy | ACT |
| Task | `beat_block_hammer` |
| Target embodiment | `franka` |
| Source embodiment | `piper` |
| Evaluation data | `target_franka_50` validation set |
| Evaluation metric | Offline target-domain validation loss |
| Alignment | zero-padding piper 14D to 16D |
| State dim | 16 |
| Chunk size | 50 |
| Seeds | 0, 1, 2 |

## Raw Results

| Setting | Source ratio | Seed 0 | Seed 1 | Seed 2 |
|---|---:|---:|---:|---:|
| Target-only | 0.0% | 0.396934 | 0.345563 | 0.391908 |
| Routed piper5 | 9.1% | 1.603187 | 1.949998 | 1.453321 |
| Naive piper50 | 50.0% | 2.946190 | 2.603570 | 2.392261 |

## Mean and Standard Deviation

| Setting | Source ratio | Mean | Std | Relative to target-only |
|---|---:|---:|---:|---:|
| Target-only | 0.0% | 0.378135 | 0.023119 | 1.00x |
| Routed piper5 | 9.1% | 1.668835 | 0.208096 | 4.41x |
| Naive piper50 | 50.0% | 2.647340 | 0.228230 | 7.00x |

## Main Trend

Across all three seeds:

```text
target-only < routed piper5 < naive piper50
