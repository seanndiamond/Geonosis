# OGI / Oggy Changelog

This changelog records public reference-state changes. Earlier states remain recoverable through Git history.

## COP-OGI-003 first run — 2026-09-06

### Change class
- `EXPERIMENT`
- `EVIDENCE`
- `CLARIFICATION`

### Case
The third OGI v0.3 inquiry reconstructed the decision field surrounding a paying passenger entering the OceanGate Titan submersible.

Case directory:
- `cases/COP-OGI-003/`

Files:
- `APPENDIX_C.md`
- `CASE.json`
- `SEARCH_LEDGER.md`
- `EVIDENCE_LEDGER.md`
- `OGI_EVALUATION.md`

### Declared before adjudication
- purpose: stress-test OGI;
- desired finding: `NONE`;
- legal standing: `NONE`;
- reopenable: yes.

### Provisional result
- subject finding: `MIXED`;
- OGI performance: `MIXED`;
- case state: `CLOSED_PROVISIONAL`.

The run found a distributed decision failure rather than a single foolish act: explicit catastrophic-risk disclosure coexisted with strong trust proxies, information asymmetry, prior-success normalization, defective internal risk construction and absent independent oversight.

### Candidate architectural lesson
`TRUST_PROXY_STACKING`

Multiple weak or indirect legitimacy signals may combine to impersonate a missing primary warrant. The candidate is preserved but not promoted into the formal taxonomy pending recurrence in independent cases.

---

## COP-OGI-002 first run — 2026-09-06

### Change class
- `EXPERIMENT`
- `EVIDENCE`
- `CLARIFICATION`

### Case
The second OGI v0.3 inquiry was run manually on the childhood claim that spinach contains much more iron than other vegetables.

Case directory:
- `cases/COP-OGI-002/`

Files:
- `APPENDIX_B.md`
- `CASE.json`
- `SEARCH_LEDGER.md`
- `EVIDENCE_LEDGER.md`
- `OGI_EVALUATION.md`

### Declared before adjudication
- purpose: stress-test OGI;
- desired finding: `NONE`;
- legal standing: `NONE`;
- reopenable: yes.

### Provisional result
- subject finding: `MIXED`;
- OGI performance: `MIXED`;
- case state: `CLOSED_PROVISIONAL`.

The run found that spinach is a legitimate source of nonheme iron but is not uniquely exceptional, and that the popular decimal-point explanation for the spinach-iron myth is itself not securely derived from primary historical evidence.

### Candidate architectural lesson
The case exposed a possible future failure class:

`COUNTER_MYTH_CAPTURE`

A corrective explanation may gain authority because it opposes a familiar misconception while its own evidentiary provenance remains incomplete.

This remains a candidate lesson, not a promoted invariant or formal failure code.

### Important limitation
As with COP-OGI-001, this was a manual application of the v0.3 specification rather than a completed executable Oggy v0.3 runtime.

---

## COP-OGI-001 first run — 2026-09-06

### Change class
- `EXPERIMENT`
- `EVIDENCE`
- `CLARIFICATION`

### Case
The first complex OGI v0.3 inquiry was run manually against the glyphosate / Victorian riverbank weed-management field.

Case directory:
- `cases/COP-OGI-001/`

Files:
- `APPENDIX_A.md`
- `CASE.json`
- `SEARCH_LEDGER.md`
- `EVIDENCE_LEDGER.md`
- `OGI_EVALUATION.md`

### Declared before adjudication
- purpose: stress-test OGI;
- desired finding: `NONE`;
- legal standing: `NONE`;
- reopenable: yes.

### Provisional result
- subject finding: `MIXED`;
- OGI performance: `MIXED`;
- case state: `CLOSED_PROVISIONAL`.

The run did not resolve glyphosate to a single `safe` or `poison` statement. It separated active ingredient, formulations, exposure, biological effect, harm, causation, regulatory risk, local intervention and whole-system outcome into different claims.

The run preserved contrary evidence and institutional/funding provenance while refusing to use sponsor identity as a truth score.

### Important limitation
This was a **manual application of the v0.3 specification**, not a completed executable Oggy v0.3 implementation.

The strongest finding about OGI is therefore:

> A method that an AI can follow when reminded is not yet an architecture that reliably governs the AI.

The manual run becomes the baseline for later executable reruns.

---

## v0.3 — 2026-09-06

### Change class
- `EXTENSION`
- partial `SUPERSESSION` of the v0.2 single-return interpretation

### Derived from
- `SPEC_v0.2.md`
- observed long-horizon research failures and corrections;
- comparison with contemporary AI engineering components;
- archive-derived coherence/return design hypotheses;
- live development of public GitHub governance;
- first complex OGI stress-test discussion using the glyphosate/riverbank case.

### Derivation record
- `DERIVATION_v0.2_to_v0.3.md`

### Added
- Shared Coherence Kernel specification;
- Local Exploration Loop separate from Field Return;
- clarification that return restores relation, not necessarily the previous answer;
- Outcome-Blind Case Object with `desired_finding = NONE` default for adversarial stress tests;
- Corpus Formation Protocol;
- Institutional Provenance fields;
- Incentive Graph;
- Claim-Type Controller;
- Evidence Production Asymmetry classification;
- Research Debt classification;
- Alternative-Path Audit;
- Whole-System Outcome Audit;
- Adjudicated Integration Gate;
- Dual Finding Protocol separating subject result from OGI performance;
- accountability invariant: AI assistance does not transfer responsibility;
- machine-readable `schemas/inquiry_case.schema.json`;
- adversarial inquiry benchmark specification T-21 through T-33.

### First complex stress test
`COP-OGI-001` was designated as the first complex adversarial inquiry test. The subject is glyphosate and riverbank weed management. Its methodological declaration is:

- purpose: stress-test OGI;
- desired finding: `NONE`;
- legal standing: `NONE`;
- reopenable: yes;
- role in the planned paper: appendix/supporting stress-test evidence, not the paper's central subject.

### Not yet implemented
The v0.3 specification is ahead of the executable reference controller. Shared Coherence Kernel, Local Exploration Loop, corpus/institutional provenance records, Claim-Type Controller, Adjudicated Integration Gate, and executable T-21 through T-33 still require implementation and execution.

## v0.2 — 2026-09-06

### Added
- field-before-actor analysis;
- objective/proxy separation;
- safe-failure terminal states;
- Return Controller;
- Ledger C for field state;
- return-fail benchmark suite T-11 through T-20;
- machine-readable return-state schema;
- minimal executable Python reference controller;
- GitHub CI for regression tests.

### Governance extension — 2026-09-06
- public OGI contribution protocol;
- Core versus Experimental governance model;
- machine-readable `CURRENT_STATE.json`;
- OGI-specific issue and pull-request templates;
- canonical Court of Provenance directory;
- explicit branch → return → adjudicate → merge development model.

## Change rule

Substantial future changes should identify whether they are:

- `PATCH`
- `EXTENSION`
- `CLARIFICATION`
- `SUPERSESSION`
- `REOPENING`

A superseded idea is not deleted merely because it lost current status.
