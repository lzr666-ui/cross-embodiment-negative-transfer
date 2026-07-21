# Experiments Draft

## 5. Experiments

### 5.1 Experimental Setup

We conduct experiments in RoboTwin2.0 using the ACT policy. We focus on the `beat_block_hammer` task and treat `franka` as the target embodiment. We evaluate two source embodiments, `piper` and `aloha-agilex`.

All policies are evaluated on the same franka validation set using offline target-domain validation loss. This ensures that the comparison measures target-domain imitation quality rather than validation loss on different mixed data distributions.

Because different embodiments expose different state/action dimensionalities, we apply a weak zero-padding alignment to map source state/action vectors to the 16-dimensional franka-compatible representation. The dimensional gap before zero-padding is still used in the conflict score.

### 5.2 Does Cross-Embodiment Mixing Hurt?

We first compare target-only training with naive cross-embodiment mixing. For piper, we repeat the key experiments across three random seeds.

| Setting | Source ratio | Seed 0 | Seed 1 | Seed 2 | Mean ± Std | Relative |
|---|---:|---:|---:|---:|---:|---:|
| Target-only | 0.0% | 0.396934 | 0.345563 | 0.391908 | 0.378135 ± 0.023119 | 1.00x |
| Routed piper5 | 9.1% | 1.603187 | 1.949998 | 1.453321 | 1.668835 ± 0.208096 | 4.41x |
| Naive piper50 | 50.0% | 2.946190 | 2.603570 | 2.392261 | 2.647340 ± 0.228230 | 7.00x |

Naive franka+piper mixing increases the average franka target-domain validation loss from `0.378` to `2.647`, corresponding to a `7.00x` degradation. This shows that cross-embodiment data can significantly hurt target-domain policy learning under weak alignment.

### 5.3 Does the Effect Generalize to Another Source Embodiment?

To verify that the observed negative transfer is not specific to piper, we further evaluate `aloha-agilex` as another source embodiment.

| Target | Source | Conflict score | Source-only loss | Naive mix loss | Target-only baseline | Negative transfer |
|---|---|---:|---:|---:|---:|---|
| franka | piper | 16.037915 | 7.151734 | 2.647340 | 0.378135 | Yes |
| franka | aloha-agilex | 15.271738 | 13.894630 | 3.117869 | 0.378135 | Yes |

Aloha-agilex also exhibits high conflict with franka and hurts target-domain validation performance under naive mixing. The aloha-only policy reaches a franka validation loss of `13.895`, and naive franka+aloha mixing increases the loss to `3.118`. This suggests that negative transfer appears across multiple high-conflict source embodiments.

### 5.4 Body-Aware Conflict Score

We compute a lightweight body-aware conflict score based on state/action dimensional mismatch and distributional gaps:

```text
C(s, t) =
dim_gap
+ qpos_mean_gap
+ qpos_std_gap
+ action_mean_gap
+ action_std_gap
