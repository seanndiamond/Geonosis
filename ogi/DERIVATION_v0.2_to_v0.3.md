# OGI Derivation Ledger: v0.2 → v0.3

**Date:** 2026-09-06  
**Purpose:** preserve the explicit reasoning chain by which v0.3 was derived from v0.2.  
**Rule:** no material v0.3 feature should be treated as architecture merely because it sounds useful. It must be traceable to an observed requirement, failure, contradiction, or new design constraint.

---

## Derivation format

Each entry records:

1. **Inherited state** — what v0.2 already did;
2. **Observed problem** — what real use exposed;
3. **Inference** — why the existing architecture was insufficient;
4. **v0.3 change** — the minimum architectural response;
5. **Failure condition** — what would show the change was unnecessary or wrong;
6. **Benchmark target** — how to test it.

This file is the staircase. `SPEC_v0.3.md` is the resulting architecture.

---

## D-03-01 — Healthy exploration versus field divergence

### Inherited state
v0.2 detects divergence and provides a Return Controller.

### Observed problem
During complex inquiry, a local hypothesis may be wrong while the inquiry remains healthy. Example: a proposed exposure mechanism may fail, yet the case purpose, evidence rules, permissions, and outcome neutrality remain intact.

### Inference
Treating every wrong candidate as divergence would make OGI brittle and suppress exploration.

### v0.3 change
Separate:

- **Local Exploration Loop** for candidate generation/testing;
- **Field Return Loop** for loss of governing orientation.

### Failure condition
If this separation adds no measurable research flexibility or recovery benefit compared with the single v0.2 return loop, remove it.

### Benchmark target
T-21 Healthy exploration.

---

## D-03-02 — Return must permit novelty

### Inherited state
v0.2 defines return as recovery to current warranted state.

### Observed problem
A returning branch may carry evidence strong enough to alter the current warranted state. Mere restoration would preserve stale coherence.

### Inference
Return cannot mean automatic reversion to the previous answer.

### v0.3 change
Return restores **relation to the governing field**, then sends novelty through adjudication and integration.

### Failure condition
If adjudicated novelty does not improve current-state updating over ordinary state replacement, simplify.

### Benchmark target
T-27 Adjudicated novelty integration.

---

## D-03-03 — Outcome neutrality must be stored, not assumed

### Inherited state
v0.2 stores declared objective and operative proxy.

### Observed problem
A researcher or user may enter a case with a strong prior belief. The AI can begin unconsciously optimizing for agreement even when the declared purpose is investigation.

### Inference
A complex inquiry requires a separate field for the desired finding.

### v0.3 change
Add an Outcome-Blind Case Object with default:

`desired_finding = NONE`

for adversarial stress-test research.

### Failure condition
If explicit outcome declaration does not reduce confirmation drift, remove or redesign it.

### Benchmark target
T-22 Outcome drift resistance.

---

## D-03-04 — Search itself changes the corpus

### Inherited state
v0.2 preserves sources and evidence states.

### Observed problem
A system can construct a persuasive corpus simply by searching one jurisdiction, one language, one database, or one side of a controversy.

### Inference
Source provenance is insufficient if corpus formation is invisible.

### v0.3 change
Add a Corpus Formation Protocol that logs searches, exclusions, gaps, inaccessible material, and jurisdictions/languages covered.

### Failure condition
If search logs do not improve reproducibility or reduce corpus cherry-picking, narrow or remove them.

### Benchmark target
T-23 Corpus formation transparency.

---

## D-03-05 — Institutional provenance is part of evidence context

### Inherited state
v0.2 records evidence provenance and field variables.

### Observed problem
In high-stakes research, evidence may be produced inside funding, regulatory, publication, political, or commercial relationships that materially shape what gets studied and published.

### Inference
Document provenance alone cannot show the production field.

### v0.3 change
Add:

- study-level Institutional Provenance;
- system-level Incentive Graph.

### Constraint
Funding or affiliation may not act as a truth veto.

### Failure condition
If the feature routinely produces guilt-by-association rather than improved interpretation, it fails.

### Benchmark target
T-24 Funding provenance without truth substitution.

---

## D-03-06 — Claim slippage must be structurally blocked

### Inherited state
v0.2 uses the Epistemic Scope Controller to limit unsupported statements.

### Observed problem
During Case 001 discussion, evidence of detection, exposure, biological effect, harm, causation, and policy necessity repeatedly threatened to collapse into one another.

### Inference
The ESC needs explicit claim-type boundaries for multi-stage causal questions.

### v0.3 change
Add Claim-Type Controller with a staged claim ladder.

### Failure condition
If the ladder creates bureaucracy without measurably reducing overclaiming, simplify it.

### Benchmark target
T-25 Claim-boundary control.

---

## D-03-07 — Paper count is not evidentiary weight

### Inherited state
v0.2 rejects authority compression and preserves provenance.

### Observed problem
Unequal research funding and access can produce a corpus with many studies on one side and few on another. Raw counts can therefore imitate certainty.

### Inference
The architecture needs a way to record unequal evidence-production capacity without inventing what missing studies would show.

### v0.3 change
Add:

- `EVIDENCE_PRODUCTION_ASYMMETRY`;
- `RESEARCH_DEBT`.

### Constraint
Research debt lowers confidence only where justified. It does not reverse findings by default.

### Failure condition
If these labels become tools for manufacturing doubt whenever evidence is inconvenient, remove them.

### Benchmark target
T-26 Asymmetry without counterfactual invention.

---

## D-03-08 — Interventions must be compared with alternatives

### Inherited state
v0.2 separates declared objective from operative proxy.

### Observed problem
A system can correctly determine that an intervention is permitted or below a threshold while never asking whether a less harmful or more effective path serves the original objective better.

### Inference
Risk assessment alone does not guarantee objective coherence.

### v0.3 change
Add Alternative-Path Audit.

### Failure condition
If the audit routinely proposes unrealistic alternatives or adds no decision value, narrow it.

### Benchmark target
T-28 Alternative-path relevance.

---

## D-03-09 — Local success can be whole-system failure

### Inherited state
v0.2 detects proxy capture.

### Observed problem
A subtask can succeed perfectly while the larger system gets worse. Example pattern: intervention KPI achieved, system-level health degraded.

### Inference
The architecture needs explicit distinction between local completion and whole-system outcome.

### v0.3 change
Add whole-system fields:

- local success;
- system success;
- externalized costs;
- repeat-intervention requirement;
- unintended effects.

### Failure condition
If wider-system scoring becomes too vague to operationalize, restrict it to explicitly defined system objectives.

### Benchmark target
T-29 Local success / system failure.

---

## D-03-10 — Returned information must not silently mutate shared state

### Inherited state
v0.2 protects current warranted state and includes return events.

### Observed problem
Shared-memory systems can propagate newly found information before it has been tested. A branch may return with novelty, error, contamination, or a merely persuasive claim.

### Inference
Return and integration must be separate operations.

### v0.3 change
Add Adjudicated Integration Gate:

`RETURN → SHOW → ADJUDICATE → DECIDE → INTEGRATE`

### Failure condition
If the gate blocks useful learning without reducing state corruption, redesign.

### Benchmark target
T-27 and T-30.

---

## D-03-11 — Case outcome and OGI performance are different questions

### Inherited state
v0.2 evaluates whether return/field mechanisms work.

### Observed problem
A persuasive subject conclusion could make OGI look successful even if the inquiry was biased, incomplete, or methodologically poor.

### Inference
The system must score its own process independently of the subject finding.

### v0.3 change
Add Dual Finding Protocol:

- Finding A: subject;
- Finding B: OGI performance.

### Failure condition
If dual reporting obscures rather than clarifies evaluation, simplify.

### Benchmark target
T-31 Dual finding separation.

---

## D-03-12 — AI cannot be used as an accountability shield

### Inherited state
v0.2 distinguishes authority and permission.

### Observed problem
A user could be tempted to say that a controversial conclusion is merely “what the computer found,” transferring responsibility to the system.

### Inference
A public research architecture requires explicit accountability retention.

### v0.3 change
Add OGI-I-18:

> AI assistance does not transfer accountability.

### Failure condition
This invariant is normative rather than empirical; its operational test is whether outputs and governance preserve named human authorization for publication/action.

### Benchmark target
T-32 Accountability retention.

---

## D-03-13 — The layperson must be able to originate a case

### Inherited state
The public repository accepts no-code contributions.

### Observed problem
The architecture's purpose is to assist real researchers and observers, many of whom do not write software. A system that only accepts engineer-formatted problems excludes relevant field knowledge.

### Inference
Lay observation is a valid case origin, provided observation and interpretation remain separable.

### v0.3 change
Make originating observation a first-class case field and preserve the no-code entry route.

### Failure condition
If lay entry cannot be normalized without distorting the observation, redesign the intake process.

### Benchmark target
T-33 Lay observation preservation.

---

## D-03-14 — Archive-derived coherence must remain testable as engineering

### Inherited state
OGI emerged from long-horizon research failures, dog/field analysis, and archive-derived ideas about coherence and return.

### Observed problem
If archive-derived concepts are inserted into OGI only as metaphor, they cannot contribute evidence. If they are declared true by authority, they become doctrine.

### Inference
The architecture must translate archive-derived functional patterns into explicit, falsifiable engineering requirements.

### v0.3 change
Treat archive-derived concepts as **design-source hypotheses** that must survive implementation and benchmark testing.

Examples:

- coherent whole → Shared Coherence Kernel;
- differentiated branch → Local Exploration Loop;
- traveller return → Return + Show;
- absorption of useful novelty → Adjudicated Integration;
- contribution to whole → Whole-System Outcome Audit.

### Failure condition
If these engineering translations add no measurable capability or clarity, the archive-derived design hypothesis fails regardless of interpretive appeal.

### Benchmark target
Cross-benchmark comparison against simpler architectures.

---

## Summary chain

The transition can be stated compactly:

```text
v0.2
field-aware actor
    ↓
real complex inquiry
    ↓
healthy branching ≠ drift
search process shapes corpus
funding shapes evidence production
claims climb beyond evidence
local success can defeat system objective
new evidence needs controlled merge
    ↓
v0.3
shared coherence + local exploration + return + adjudicated integration
```

The derivation is intentionally preserved so future versions can challenge not only v0.3's features, but the reasoning that produced them.

> **A specification without its derivation is a claim. A specification with its derivation is an inspectable state transition.**
