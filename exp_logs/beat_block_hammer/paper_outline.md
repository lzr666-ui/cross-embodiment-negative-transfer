# Paper Outline

## Title

When Does Cross-Embodiment Data Hurt VLA?
A Body-Aware Diagnosis and Routing Method

## 1. Introduction

- Cross-embodiment robot data is increasingly used for generalist robot policies.
- However, mixing data across embodiments is not always beneficial.
- We ask: when does cross-embodiment data hurt target-domain policy learning?
- We hypothesize that high-conflict source embodiments can induce negative transfer under weak alignment.

## 2. Preliminary Study

- Environment: RoboTwin2.0
- Policy: ACT
- Task: beat_block_hammer
- Target: franka
- Source: piper
- Finding:
  - naive mixing hurts
  - piper-only transfer is poor
  - zero-padding is not sufficient alignment

## 3. Conflict Score

- Define body-aware conflict score:
  - dim gap
  - qpos mean/std gap
  - action mean/std gap
- franka-piper conflict score = 16.038
- High score is consistent with observed performance drop.

## 4. Body-Aware Conflict Routing

- Use conflict score to route source data.
- High conflict -> reduce source ratio.
- piper is routed from 50% source ratio to about 10%.

## 5. Experiments

### 5.1 Negative Transfer

| Setting | Mean target-val loss |
|---|---:|
| Target-only | 0.371 |
| Naive franka+piper | 2.775 |

### 5.2 Routing Mitigation

| Setting | Mean target-val loss |
|---|---:|
| Naive mix | 2.775 |
| Routed mix | 1.777 |

Routing reduces loss by 36.0%.

## 6. Limitations

- ACT baseline, not yet pi0-style VLA.
- One task.
- One source embodiment.
- Offline validation loss only.
- Closed-loop success rate remains future work due to WSL rendering issue.

## 7. Next Work

- Add more tasks/sources.
- Move to pi0/OpenPI.
- Run closed-loop simulation on native Ubuntu/server.
