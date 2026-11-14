# ODRR-RR-001 — Blinded Replication of Orientation-Dependent Relational Rebinding

**Status:** PREREGISTRATION DRAFT — NO CONFIRMATORY DATA COLLECTED  
**Court case:** IMG-2026-001 / GEO-CASE-METHOD-006  
**Date opened:** 2026-09-07  
**Repository role:** public methods, audit trail, code, pilot record, preregistration materials, later anonymized results

## Why this study exists

The Court of Provenance recorded a pilot observation termed **Orientation-Dependent Relational Rebinding (ODRR)**: changing image orientation sometimes altered which visible features grouped together while a coherent organization persisted or re-formed.

The pilot was exploratory and explicitly confounded. It was not blinded, used familiar sources in places, mixed rendering transformations in at least one sequence, and involved investigators who knew the developing hypothesis. Those weaknesses are not hidden. They are the reason this confirmatory study exists.

## Narrow confirmatory question

> In pre-identified pilot image sets, does rotation produce higher observer-rated relational rebinding while preserving coherence than in matched control image sets under blinded, randomized viewing conditions?

This study **does not test**:
- intentional multi-orientation encoding;
- authorship, language, historical meaning or ontology;
- whether Geonosis as a whole is correct;
- whether any particular archaeological interpretation is correct.

## Current evidence state

Pilot observations: **INSPECTED / exploratory**.  
Independent human replication: **NOT YET RUN**.  
Confirmatory protocol: **being frozen before data collection**.

The Court staircase applies:

`ASSERTED -> CITED -> LOCATED -> RETRIEVED -> INSPECTED -> MAPPED -> DERIVED -> REPRODUCED -> CHALLENGED -> SURVIVED`

No downstream state is inferred in advance.

## Files

- `PREREGISTRATION_DRAFT.md` — full protocol and decision rules.
- `ANALYSIS_PLAN.md` — confirmatory statistics, exclusion rules and outcome classification.
- `PILOT_DATA.csv` — RPL-000 to RPL-005, explicitly exploratory.
- `STIMULUS_MANIFEST_TEMPLATE.csv` — provenance and condition fields for every image source.
- `BLINDING_AND_RANDOMIZATION.md` — concealment, key sealing and deterministic randomization.
- `ETHICS_AND_GOVERNANCE.md` — human-participant gate and data minimization.
- `OBSERVER_INSTRUCTIONS.md` — neutral participant-facing task text.
- `FROZEN_DECISIONS.json` — machine-readable preregistration state.
- `scripts/generate_randomization.py`
- `scripts/analyze_confirmatory.py`
- `scripts/validate_data.py`
- `scripts/seal_blind_key.py`

## Hard rule before collection

No confirmatory participant data are to be collected until:
1. the stimulus set and matching rules are complete;
2. the blind key is sealed and its SHA-256 hash committed;
3. the preregistration is frozen in a time-stamped read-only registry;
4. human-research ethics review/authorization or a documented determination of the applicable review pathway is in place;
5. the analysis scripts pass validation on synthetic data.

## Pilot/confirmatory separation

The six RPL records are historical pilot evidence. They may justify the hypothesis and inform the design, but they cannot be counted as confirmatory observations.

## Court posture

A result is allowed to weaken the claim.

If matched controls perform equivalently, the ODRR effect is downgraded at the tested scope. If controls outperform the target set, that is recorded. Negative results remain in the repository.

**SHOW ME.**
