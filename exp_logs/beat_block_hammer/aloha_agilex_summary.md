# Aloha-AgileX Source Summary

## Setup

| Item | Setting |
|---|---|
| Environment | RoboTwin2.0 |
| Policy | ACT |
| Task | `beat_block_hammer` |
| Target embodiment | `franka` |
| Source embodiment | `aloha-agilex` |
| Evaluation data | `target_franka_50` validation set |
| Evaluation metric | Offline target-domain validation loss |
| Alignment | zero-padding aloha-agilex 14D to 16D |
| State dim | 16 |
| Chunk size | 50 |

## Conflict Score

| Target | Source | dim gap | qpos mean gap | qpos std gap | action mean gap | action std gap | Conflict score |
|---|---|---:|---:|---:|---:|---:|---:|
| franka | aloha-agilex | 2.000000 | 4.933475 | 1.704460 | 4.926703 | 1.707100 | 15.271738 |

## Results

| Method | Train data | Source ratio | L1 | KL | Target-val loss |
|---|---|---:|---:|---:|---:|
| Source-only | aloha-agilex 50 | 100.0% | 0.682021 | 1.321261 | 13.894630 |
| Naive mix | franka 50 + aloha-agilex 50 | 50.0% | 0.454245 | 0.266362 | 3.117869 |

## Interpretation

Aloha-agilex is another high-conflict source embodiment for franka. Similar to piper, aloha-agilex causes severe degradation under source-only transfer and also hurts franka target-domain validation performance under naive mixing.

Compared with the three-seed franka-only baseline:

```text
target-only mean loss = 0.378135
franka+aloha naive mix loss = 3.117869
