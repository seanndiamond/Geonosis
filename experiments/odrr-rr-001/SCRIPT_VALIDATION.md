# Analysis Script Validation Record

**Date:** 2026-09-07  
**Protocol:** ODRR-RR-001 v0.2-draft  
**Purpose:** software smoke test only

Before confirmatory human data exist, the validation and analysis scripts were exercised on a deliberately synthetic dataset containing:
- 60 artificial participant tokens;
- 8 artificial stimulus IDs;
- 4 orientations per stimulus;
- 1,920 synthetic trial rows.

The validator accepted the schema and rating ranges.

The analysis program successfully:
- formed transition-level ODRR scores;
- aggregated by source and participant;
- kept participant as the primary unit of inference;
- calculated target-control paired differences;
- ran the sign-flip permutation test;
- generated bootstrap confidence intervals;
- computed paired standardized effect size;
- applied the predeclared outcome-classification logic.

The synthetic values were intentionally generated with target/control separation so that the positive branch of the decision logic would be exercised.

**This is not empirical evidence for ODRR.** The synthetic values are not observations, are not participants, and are not part of any scientific effect estimate. Their only evidentiary role is to demonstrate that the analysis machinery can execute before confirmatory data are collected.

Synthetic raw values are not included in the scientific dataset and must never be merged with participant data.
