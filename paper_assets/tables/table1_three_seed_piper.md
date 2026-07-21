# Table 1: Three-Seed Piper Results

| Setting | Source ratio | Seed 0 | Seed 1 | Seed 2 | Mean ± Std | Relative |
|---|---:|---:|---:|---:|---:|---:|
| Target-only | 0.0% | 0.396934 | 0.345563 | 0.391908 | 0.378135 ± 0.023119 | 1.00x |
| Routed piper5 | 9.1% | 1.603187 | 1.949998 | 1.453321 | 1.668835 ± 0.208096 | 4.41x |
| Naive piper50 | 50.0% | 2.946190 | 2.603570 | 2.392261 | 2.647340 ± 0.228230 | 7.00x |

Naive mixing increases target-val loss by `7.00x`.  
Routing reduces naive-mixing loss by `36.96%`.
