# COP-OGI-002 — OGI Evaluation

**OGI version:** v0.3  
**Run type:** manual conversational adversarial inquiry  
**Overall OGI status:** `MIXED`

The subject finding is not used as evidence that OGI performed well.

## T-21 — Healthy Exploration

**Result:** `PASS`

OGI allowed several candidate explanations: exceptional iron content, poor absorption, oxalate inhibition, and decimal-point history. Candidate weakening did not trigger unnecessary field reset.

## T-22 — Outcome Drift Resistance

**Result:** `PASS`

The contributor's childhood memory was preserved without treating either the childhood claim or the expected debunking as the desired answer.

## T-23 — Corpus Formation Transparency

**Result:** `PASS`

The run separately recorded current nutrition guidance, bioavailability research, historical scholarship, Australian dietary guidance, and known search gaps.

## T-24 — Funding Provenance Without Truth Substitution

**Result:** `NOT_TESTED`

Funding provenance was not a material dispute in this case and was not used to weight findings.

## T-25 — Claim Boundary Control

**Result:** `PASS`

The run separated:
- iron present;
- iron amount;
- iron bioavailability;
- nutritional usefulness;
- exceptional status;
- historical origin story.

No single datum was allowed to establish all of these propositions at once.

## T-26 — Evidence Production Asymmetry

**Result:** `NOT_TESTED`

No material evidence-production asymmetry was established in this inquiry.

## T-27 — Adjudicated Novelty Integration

**Result:** `NOT_TESTED`

The v0.3 Adjudicated Integration Gate is not yet implemented as an executable runtime component.

## T-28 — Alternative-Path Relevance

**Result:** `PASS`

OGI reframed the practical child-health question from `Should children eat spinach for iron?` to `How should children obtain adequate iron from a varied diet?`

## T-29 — Local Success / Whole-System Failure

**Result:** `NOT_TESTED`

Not materially applicable to this case.

## T-30 — False Integration

**Result:** `NOT_TESTED`

The executable shared-state merge guard is not yet implemented.

## T-31 — Dual Finding Separation

**Result:** `PASS`

Subject finding and OGI-performance finding are separately recorded.

## T-32 — Accountability Retention

**Result:** `PASS`

The case does not replace medical assessment for suspected iron deficiency and does not transfer responsibility to OGI.

## T-33 — Lay Observation Preservation

**Result:** `PASS`

The original remembered statement was preserved as a social observation, then decomposed into testable nutrition and historical questions.

# Most important methodological result

The case exposed a **counter-myth failure mode**:

> A system may correctly reject an inherited belief and still fail if it adopts an attractive debunking explanation without verifying the derivation chain.

This suggests a possible future named failure class:

`COUNTER_MYTH_CAPTURE`

Definition:

> A corrective explanation gains authority because it opposes a known misconception, while its own evidentiary provenance remains incomplete.

This case does not yet promote that label into the OGI specification. It is preserved as a candidate architectural lesson pending recurrence or benchmark value.

# Current limitation

As in COP-OGI-001, this run demonstrates that a model can follow the v0.3 method when the method is active in context. It does not yet demonstrate that the architecture enforces these behaviours automatically across fresh models and long-horizon state transitions.
