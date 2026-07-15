# Body-Aware Conflict Routing

## 1. Motivation

Naive cross-embodiment data mixing assumes that source and target robot demonstrations are equally useful. However, our preliminary experiments show that this assumption can fail when the source embodiment has high state/action conflict with the target embodiment.

In the `beat_block_hammer` task, piper demonstrations significantly degrade franka target-domain validation performance under weak zero-padding alignment.

Therefore, we introduce a lightweight body-aware routing rule:

> high-conflict source data should be downweighted or filtered before policy training.

---

## 2. Conflict Score

For a target embodiment `t` and a source embodiment `s`, we define:

```text
C(s, t) =
dim_gap(s, t)
+ qpos_mean_gap(s, t)
+ qpos_std_gap(s, t)
+ action_mean_gap(s, t)
+ action_std_gap(s, t)
