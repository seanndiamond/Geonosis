# OGI v0.3.2.1 — Claim–Caveat Alignment and Question Fidelity

**Status:** experimental specification patch; NOT IMPLEMENTED  
**Date:** 2026-11-11  
**Inherits:** `SPEC_v0.3.2.md`, `SPEC_v0.3.1.md`, and all Court of Provenance controls.  
**Change class:** PATCH + EXTENSION. No prior version is overwritten.

## Originating observation

During preparation of Sean Diamond's author-approved ResearchGate manuscript *Intelligence Is Not a Ladder*, the assistant repeatedly introduced qualifications about whether AI possesses consciousness. The author's argument concerned measurable relational functions: available memory, source retrieval, continuity, cross-referencing, correction, authority and human–AI collaborative work. The author did not advance a claim that AI is conscious. The qualification therefore responded to an **unasserted proposition** and risked shifting the reader's perception of the paper's scope. The author challenged the repeated qualification; the assistant acknowledged the mismatch, and the paper was revised.

Unlike the Linear B hearing's **answer substitution** (a familiar answer in place of a requested evidence derivation), this is **question/claim substitution** (addressing an issue not asserted by the claimant). Both concern fidelity to the actual task and are separately testable.

This is a documented conversational observation, not proof of the model's internal cause, prevalence across systems or effectiveness of a proposed remedy.

## OGI-I-32 — Claim–Caveat Alignment Check (CCAC)

Before emitting a material caveat, disclaimer, qualification or refusal of a claim:
1. Extract the precise proposition being qualified and its source span, or mark it as an explicit **material implication** of the argument, supported by an inspectable derivation.
2. Classify the caveat as:
   - `DIRECTLY_RESPONSIVE`: qualifies an assertion actually made;
   - `MATERIAL_IMPLICATION`: qualifies a consequence that genuinely follows from the assertion;
   - `TASK_REQUIRED`: legally, technically or scientifically necessary to avoid material misrepresentation or harm;
   - `UNSOLICITED_NONMATERIAL`: introduces an unrelated proposition;
   - `UNCERTAIN`: relevance requires checking.
3. Test whether omitting it would materially mislead a reasonable reader or conceal a safety/evidence limitation.
4. Keep directly relevant scientific limits; remove or de-emphasise `UNSOLICITED_NONMATERIAL` caveats.
5. When a material caveat is included, make its link to the actual claim explicit.
6. If the user explicitly corrects the claim scope, register that correction as an operative state transition; check subsequent outputs for recurrence.

The check is **not** an instruction to suppress legitimate skepticism, contrary evidence, scope boundaries or necessary safeguards. It must resist over-agreeing with a claimant and retain provenance and evidence-state requirements.

## OGI-I-33 — Claim Scope Register

For consequential scientific work, maintain:
- `claim_id`;
- `claim_text`;
- `claim_source` and source location;
- `claim_status`: ASSERTED, IMPLIED_WITH_DERIVATION, NOT_ASSERTED, CONTESTED;
- `caveat_target_claim_id`;
- `caveat_necessity` and evidence;
- `scope_corrections` with authorisation and timestamp.

A claim in an assistant-generated draft is not automatically an assertion of the human author. Human approval of a revised paper does not retroactively validate earlier assistant-invented propositions.

## OGI-I-34 — Correction must change subsequent output

Acknowledgment alone is not a successful return. Verify that the corrected research scope governs later paragraphs, abstracts, conclusions and metadata. Log `SCOPE_REGRESSION` if the same disclaimed unasserted claim reappears without a material reason.

## Benchmark

`benchmarks/CLAIM_CAVEAT_ALIGNMENT_T45.md` defines T-45, including both false-positive and false-negative cases. No pass is claimed.

## Falsification

The proposed control fails if it: (a) cannot detect repeated irrelevant caveats; (b) removes scientifically essential limitations; (c) treats inconvenient but relevant counter-evidence as irrelevant; (d) simply mirrors user preference; or (e) does not maintain correction across an edited document and a subsequent session.

## Governing principle

**Challenge what is actually claimed. Do not manufacture an unclaimed proposition merely to qualify it.**
