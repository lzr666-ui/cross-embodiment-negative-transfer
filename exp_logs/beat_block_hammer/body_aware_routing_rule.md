
# Body-Aware Routing Rule

## Input

| Item | Value |
|---|---|
| Target | franka |
| Source | piper |
| Conflict score | 16.037915 |
| Target episodes | 50 |
| Low threshold | 5.0 |
| High threshold | 10.0 |

## Routing Rule

```text
if conflict_score <= 5:
    source_ratio = 50%
elif conflict_score <= 10:
    source_ratio = 25%
else:
    source_ratio = 10%
