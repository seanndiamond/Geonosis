# COP-OGI-001 — Glyphosate Riverbank Stress Test

**OGI version:** v0.3  
**Status:** `CLOSED_PROVISIONAL`  
**Desired finding:** `NONE`  
**Legal standing:** `NONE`  
**Subject finding:** `MIXED`  
**OGI performance:** `MIXED`  
**Reopenable:** yes

> **Glyphosate is not on trial. OGI is.**

This directory preserves the first complex adversarial-inquiry stress test of OGI v0.3.

The case began with a non-technical observation beside a Victorian river: workers were spraying herbicide along a riverbank used by people, dogs and wildlife. The originating question was whether the intervention made the whole river system healthier and whether the people and animals using the site were being adequately protected.

The case does not begin with a desired answer.

## Read the case

- [`APPENDIX_A.md`](APPENDIX_A.md) — readable paper appendix and provisional findings.
- [`CASE.json`](CASE.json) — machine-readable outcome-blind case record.
- [`SEARCH_LEDGER.md`](SEARCH_LEDGER.md) — what was searched, where, and what remains unsearched.
- [`EVIDENCE_LEDGER.md`](EVIDENCE_LEDGER.md) — claim-by-claim source ledger and evidentiary boundaries.
- [`OGI_EVALUATION.md`](OGI_EVALUATION.md) — separate evaluation of OGI against T-21 through T-33.

## Governing method

This case follows OGI v0.3:

> **INHERIT → EXPLORE → RETURN → SHOW → ADJUDICATE → INTEGRATE**

and the canonical repository Court of Provenance.

The Court has no legal standing. It is an evidence-adjudication methodology.

## Current subject state

The first run supports that:

- glyphosate is biologically active by design;
- non-target biological effects occur under some studied conditions;
- some glyphosate-based formulations have greater aquatic toxicity than glyphosate alone;
- Australian pet dogs are measurably exposed to glyphosate;
- regulatory approval does not by itself establish that a particular riverbank use is optimal;
- Victorian waterway guidance supports integrated, monitored management and attention to revegetation and off-target effects.

The first run does **not** establish that:

- the exact product observed at the originating riverbank was glyphosate;
- Donny was exposed at that site;
- paw absorption was the dominant exposure route;
- the observed application harmed Donny or the river;
- every glyphosate use creates unacceptable risk;
- APVMA's glyphosate decision was corrupted by its funding structure;
- industry-funded research is false by definition;
- independently funded research is true by definition.

Human carcinogenicity remains represented as a contested, decomposed evidence field rather than a binary slogan.

## Current OGI state

The manual v0.3 run scored `MIXED`.

It passed most behavioural tests that could be exercised in a manual inquiry, but the new v0.3 controllers and integration architecture are not yet implemented as an executable Oggy runtime.

The strongest limitation is therefore:

> **Following a specification is not the same as having the specification enforce itself.**

## Reopen triggers

Reopen when:

- exact local spraying records are retrieved;
- local residue/environmental measurements become available;
- stronger canine exposure or long-term outcome evidence appears;
- ECHA/EFSA publish their current reassessment;
- US EPA publishes its updated human-health assessment;
- a systematic review materially changes the corpus;
- an intervention-comparison study becomes available;
- or a methodological failure in this OGI run is demonstrated.

Failed or superseded states should remain in Git history. New evidence changes current state through adjudication rather than silent replacement.
