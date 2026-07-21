# Seed 2 Summary: Cross-Embodiment Negative Transfer

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
| Seed | 2 |

## Results

| Method | Train data | Source ratio | L1 | KL | Target-val loss |
|---|---|---:|---:|---:|---:|
| Target-only | franka 50 | 0.0% | 0.156784 | 0.023512 | 0.391908 |
| Routed mix | franka 50 + piper 5 | 9.1% | 0.267645 | 0.118568 | 1.453321 |
| Naive mix | franka 50 + piper 50 | 50.0% | 0.481191 | 0.191107 | 2.392261 |

## Trend

```text
target-only < routed piper5 < naive piper50
