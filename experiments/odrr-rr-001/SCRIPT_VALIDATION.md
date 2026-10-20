# Analysis Script Validation Record

**Date:** 2026-09-07  
**Protocol:** ODRR-RR-001 v0.2-draft  
**Purpose:** software smoke test only

## Run 1 — primary decision path

Before confirmatory human data exist, the validation and analysis scripts were exercised on a deliberately synthetic dataset containing:
- 60 artificial participant tokens;
- 8 artificial target/control stimulus IDs;
- 4 orientations per stimulus;
- 1,920 synthetic trial rows.

The validator accepted the schema and rating ranges. The initial analysis program successfully formed ODRR scores, aggregated at participant level, ran the sign-flip permutation test, generated bootstrap intervals and selected a predeclared outcome class.

## Self-audit correction

After the outcome-neutral quality controls were added to protocol v0.2, a prose/code mismatch was detected: the written protocol gave the QC gate precedence, but the then-current analysis script did not yet enforce it.

That gap was corrected **before confirmatory data collection**. The earlier script remains recoverable in Git history.

## Run 2 — quality-control gate implementation

A new synthetic dataset included:
- 60 artificial participant tokens;
- 8 artificial target/control stimulus IDs;
- QC-ROT-STABLE trials;
- QC-REARRANGED trials;
- 4 presentations per source.

The revised script successfully:
- calculated the QC-ROT-STABLE median mere-rotation score;
- calculated the QC-ROT-STABLE median grouping-change score;
- calculated the QC-REARRANGED median grouping-change score;
- evaluated the study-level QC gate before classifying the target/control result;
- computed target/control ODRR only from TARGET and CONTROL labels.

For the deliberately constructed passing-QC smoke test, the observed synthetic QC summaries were approximately:
- QC-ROT-STABLE median mere rotation: 8.49;
- QC-ROT-STABLE median grouping change: 1.94;
- QC-REARRANGED median grouping change: 8.33.

The positive target/control branch also executed successfully. These numbers were deliberately generated and carry no empirical meaning.

## Evidentiary boundary

**This is not empirical evidence for ODRR.** The synthetic values are not observations, are not participants, and are not part of any scientific effect estimate. Their only evidentiary role is to demonstrate that the analysis machinery and QC veto can execute before confirmatory data are collected.

Synthetic raw values are not included in the scientific dataset and must never be merged with participant data.
