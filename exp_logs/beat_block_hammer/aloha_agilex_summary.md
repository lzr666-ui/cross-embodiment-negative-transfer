# Aloha-AgileX Summary: Cross-Embodiment Negative Transfer

## Setup

- Task: beat_block_hammer
- Target embodiment: franka
- Source embodiment: aloha-agilex
- Policy: ACT
- Evaluation: offline target-domain validation loss on franka validation set
- Target demos: 50
- Source demos: 50
- Seeds: 0, 1, 2
- State/action dimension: franka 16D, aloha-agilex original 14D padded to 16D for ACT training

## Body-Aware Conflict Score

| Target | Source | target_dim | source_dim | dim_gap | qpos_mean_gap | qpos_std_gap | action_mean_gap | action_std_gap | conflict_score |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| franka | aloha-agilex | 16 | 14 | 2.000000 | 4.933475 | 1.704460 | 4.926703 | 1.707100 | 15.271738 |

## Offline Target Validation Results

| Setting | Target demos | Source demos | Source ratio | Seed0 | Seed1 | Seed2 | Mean | Std |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| target-only | 50 | 0 | 0.0% | 0.396934 | 0.345563 | 0.391908 | 0.378135 | 0.023119 |
| aloha routed | 50 | 5 | 9.1% | 1.831955 | 2.041737 | 2.694631 | 2.189441 | 0.367331 |
| aloha naive | 50 | 50 | 50.0% | 2.655153 | 2.869212 | 3.749108 | 3.091158 | 0.473378 |

## Derived Metrics

- Naive negative transfer ratio: 3.091158 / 0.378135 = 8.17x
- Routed negative transfer ratio: 2.189441 / 0.378135 = 5.79x
- Routing mitigation over naive mixing: (3.091158 - 2.189441) / 3.091158 = 29.17%

## Interpretation

Aloha-agilex has a high body-aware conflict score with franka. Under naive 50:50 cross-embodiment mixing, the target-domain validation loss increases substantially compared with target-only training. Reducing the source ratio from 50 aloha demonstrations to 5 aloha demonstrations lowers the target validation loss, suggesting that body-aware routing/source downweighting can partially mitigate negative transfer.

However, the routed setting still performs worse than target-only, indicating that source downweighting mitigates but does not fully solve the embodiment mismatch problem under weak alignment.
