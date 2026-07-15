# Seed 1 Summary: Cross-Embodiment Negative Transfer

## 1. Setup

| Item | Setting |
|---|---|
| Environment | RoboTwin2.0 |
| Policy | ACT |
| Task | `beat_block_hammer` |
| Target embodiment | `franka` |
| Source embodiment | `piper` |
| Evaluation data | `target_franka_50` validation set |
| Evaluation metric | Offline target-domain validation loss |
| State/action dimension | 16 |
| Chunk size | 50 |
| Alignment | Zero-padding piper 14D state/action to 16D |
| Seed | 1 |

---

## 2. Data Settings

| Dataset | Train data | Source ratio | Purpose |
|---|---|---:|---|
| `target_franka_50` | franka 50 | 0.0% | Target-only baseline |
| `mix_franka_piper_55` | franka 50 + piper 5 | 9.1% | Conflict-aware downweighting / routed mix |
| `mix_franka_piper_100` | franka 50 + piper 50 | 50.0% | Naive cross-embodiment mixing |

---

## 3. Seed 1 Results

| Method | Train data | Source ratio | L1 | KL | Target-val loss | Interpretation |
|---|---|---:|---:|---:|---:|---|
| Target-only | franka 50 | 0.0% | 0.138430 | 0.020713 | 0.345563 | Best target-domain performance |
| Routed mix | franka 50 + piper 5 | 9.1% | 0.266665 | 0.168333 | 1.949998 | Downweighting high-conflict source partially mitigates hurt |
| Naive mix | franka 50 + piper 50 | 50.0% | 0.475384 | 0.212819 | 2.603570 | Naive source mixing causes negative transfer |

---

## 4. Key Trend

The ordering is:

```text
target-only < routed piper5 < naive piper50
