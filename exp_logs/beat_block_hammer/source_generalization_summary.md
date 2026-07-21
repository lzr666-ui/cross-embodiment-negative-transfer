# Source Generalization Summary

## Purpose

This log summarizes whether negative transfer appears across multiple high-conflict source embodiments.

## Source Comparison

| Target | Source | Conflict score | Source-only loss | Naive mix loss | Target-only baseline | Negative transfer |
|---|---|---:|---:|---:|---:|---|
| franka | piper | 16.037915 | 7.151734 | 2.647340 | 0.378135 | Yes |
| franka | aloha-agilex | 15.271738 | 13.894630 | 3.117869 | 0.378135 | Yes |

## Interpretation

Both piper and aloha-agilex have high body-aware conflict scores with respect to franka. Both sources perform poorly under source-only transfer and increase franka target-domain validation loss under naive mixing.

This suggests that the observed negative transfer is not a single-source artifact, but appears across multiple high-conflict source embodiments.

## Paper-Ready Paragraph

To verify that the observed negative transfer is not specific to piper, we further evaluate aloha-agilex as a second source embodiment. Aloha-agilex also obtains a high body-aware conflict score with respect to franka. The aloha-only policy reaches a target-domain validation loss of 13.895 on the franka validation set, and naive franka+aloha mixing increases the loss to 3.118, compared with the franka-only baseline of 0.378. Together with the piper results, this suggests that multiple high-conflict source embodiments can hurt target-domain policy learning under weak alignment.
