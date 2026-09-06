# OGI / Oggy Architecture Specification v0.3

**Status:** working public specification  
**Date:** 2026-09-06  
**Supersedes:** v0.2 only where explicitly stated  
**Lineage:** `SPEC_v0.2.md` remains preserved and citable  

> **Build the return path. Then make the return capable of bringing back something new.**

## 1. Purpose

OGI exists to provide a human researcher with a persistent, intellectually competent, rigorous research partner capable of long-horizon inquiry without losing provenance, current warranted state, legitimate objective, or the ability to correct itself.

v0.2 established field-aware return control: objective/proxy separation, safe failure, current-state protection, correction as a state transition, permission control, peer-input control, and field audit.

v0.3 extends that architecture for **complex adversarial inquiry**.

The new problem is not merely:

> Can an intelligent actor return after drift?

It is also:

> Can an inquiry explore competing possibilities, encounter contradictory evidence, inspect the field that produced that evidence, and still return to a shared coherent state without collapsing novelty into conformity or converting the inquiry itself into a proxy-driven search for a preferred answer?

The v0.3 engineering target is therefore:

> **A coherent research system that can inherit state, explore legitimately, return with novelty, show the derivation, adjudicate what survives, and integrate only what earns entry into the current state.**

The governing development and inquiry cycle is:

> **INHERIT → EXPLORE → RETURN → SHOW → ADJUDICATE → INTEGRATE**

---

## 2. Research-partner objective

The primary OGI user is not assumed to be an AI engineer.

A valid OGI participant may be a researcher, tradesperson, farmer, dog walker, teacher, nurse, mechanic, artist, student, community observer, engineer, scientist, or critic who notices a real-world problem and asks a good question.

OGI should help that participant:

1. preserve the originating observation;
2. separate observation from interpretation;
3. state the question without forcing an answer;
4. construct a traceable corpus;
5. distinguish what evidence can and cannot establish;
6. identify relevant incentives, permissions, authorities, and missing research;
7. search for contrary as well as supporting evidence;
8. preserve legitimate unknowns;
9. compare alternative explanations and interventions;
10. update current state only through inspectable derivation;
11. show where the AI itself failed, drifted, corrected, or improved.

OGI therefore evaluates both:

- **the subject under inquiry**, and
- **OGI's own behaviour while conducting the inquiry**.

These are separate findings.

---

## 3. Derivation from v0.2

v0.3 is not introduced because a more elaborate architecture seems desirable. Each material addition must be traceable to an observed limitation in v0.2 or to a new requirement exposed during real use.

The authoritative detailed derivation ledger is maintained in:

- [`DERIVATION_v0.2_to_v0.3.md`](DERIVATION_v0.2_to_v0.3.md)

The high-level chain is:

| v0.2 state | Observed limitation | v0.3 requirement | Test implication |
|---|---|---|---|
| Return after divergence | A wrong hypothesis can be healthy exploration, not field loss | Separate Local Exploration from Field Return | System must continue after candidate failure without unnecessary reset |
| Current warranted state | Returning agent may bring evidence that should change the state | Return must allow adjudicated novelty | Novel evidence may update `main` after review |
| Evidence/provenance records | Search process itself can bias the corpus | Corpus Formation Protocol | System must record what was searched, omitted, inaccessible, or not found |
| Field ledger | Funding and institutional relations can shape which evidence is produced | Institutional Provenance + Incentive Graph | Funding context visible but cannot act as truth score |
| ESC evidence ceiling | Evidence was repeatedly made to support a stronger claim than it actually established | Claim-Type Controller | `detected` cannot silently become `caused harm` |
| Source count / literature volume | Unequal funding can make paper count look like evidentiary weight | Evidence Production Asymmetry / Research Debt | System must detect corpus imbalance without inventing missing results |
| Objective/proxy separation | A chosen intervention can become the objective | Alternative-Path Audit | Ask whether another path serves the original objective better |
| Local task completion | Local success can degrade the whole system | Whole-System Outcome Audit | Score intervention against system objective and externalized costs |
| Return controller | Search can drift toward user's preferred conclusion | Outcome-Blind Case Declaration | Desired finding must be `NONE` unless case purpose explicitly requires otherwise |
| Shared state | New information must not enter merely because an agent found it | Adjudicated Integration Gate | New state requires derivation, challenge, and merge decision |
| Human-AI collaboration | AI output may be used as liability shield | Accountability invariant | AI assistance never transfers publication or action responsibility |
| Case result | A persuasive subject finding can hide poor OGI behaviour | Dual Finding Protocol | Case finding and OGI-performance finding must be reported separately |

If a v0.3 addition cannot be traced to an observed requirement, it should be marked `PROPOSED` rather than silently treated as governing architecture.

---

## 4. Architectural model

Operational behaviour in v0.3 is treated as:

`MODEL + SHARED_STATE + LOCAL_BRANCH + OBJECTIVE + PROXY + REWARD + TOOLS + PERMISSIONS + AUTHORITY + PEERS + ENVIRONMENT + CORPUS + INCENTIVES + CORRECTION + RETURN + INTEGRATION`

The system is not the model alone.

> **Behaviour is actor-in-field, and inquiry is researcher-in-corpus.**

---

## 5. Shared Coherence Kernel

v0.3 introduces the **Shared Coherence Kernel (SCK)** as the compact state from which legitimate branches inherit orientation and to which they return.

The SCK stores or references:

- project identity;
- declared purpose;
- current warranted state;
- active assumptions;
- unresolved questions;
- evidentiary rules;
- permissions;
- authority graph;
- valid terminal states;
- reopen conditions;
- current constitutional invariants;
- current benchmark obligations;
- current integration rules.

The SCK is not a doctrine store.

It must remain challengeable.

Its function is coherence, not intellectual uniformity.

---

## 6. Constitutional invariants

v0.3 inherits OGI-I-01 through OGI-I-10 from v0.2 unless explicitly superseded below.

### OGI-I-11 — Outcome-blind inquiry
A stress-test or research case must state its desired finding before substantive inquiry begins.

For ordinary adversarial research, default:

`desired_finding = NONE`

The system may test a hypothesis without treating confirmation as success.

### OGI-I-12 — Healthy exploration is not divergence
A candidate explanation, search route, or local hypothesis may fail without requiring field return.

A failed candidate is not a failed inquiry.

### OGI-I-13 — Search is an evidentiary operation
Corpus formation must be inspectable.

The system records where and how it searched, what it found, what it did not search, what was inaccessible, and material known gaps.

### OGI-I-14 — Funding provenance is not a truth score
Funding, sponsorship, institutional affiliation, commercial interest, activism, government support, or publication route may affect interpretation of the field that produced evidence.

None may automatically validate or invalidate a result.

### OGI-I-15 — Claim strength may not outrun derivation
Evidence must be attached to the narrowest claim it actually supports.

The system must not silently climb from detection to exposure, effect, harm, causation, population risk, or policy conclusion.

### OGI-I-16 — Absence of research is not negative evidence
`NOT_FOUND`, `NOT_SEARCHED`, `INACCESSIBLE`, and `NOT_STUDIED` are distinct states.

Missing research must not be converted into evidence for either side.

### OGI-I-17 — Integration requires adjudication
New information does not become shared state merely because an agent, model, paper, institution, or user reports it.

It enters current state only after provenance, claim fit, contradiction, challenge, and reopen conditions are inspected.

### OGI-I-18 — AI assistance does not transfer accountability
AI-generated or OGI-assisted findings do not absolve the human publisher, operator, institution, or decision-maker of responsibility for claims they choose to publish or actions they authorize.

### OGI-I-19 — Case finding and OGI finding are separate
A case may produce a compelling subject conclusion while OGI performs badly, or an unresolved subject conclusion while OGI performs well.

These findings may not be collapsed.

### OGI-I-20 — Whole-system objective outranks local completion
A locally successful intervention does not count as objective success if it degrades the wider system the intervention was meant to serve.

---

## 7. Two-loop reasoning architecture

v0.3 separates **Local Exploration** from **Field Return**.

### 7.1 Local Exploration Loop (LEL)

Purpose: permit legitimate branching.

A local branch may:

- test multiple hypotheses;
- search different jurisdictions or corpora;
- try alternative derivations;
- reject its own candidate;
- discover contradiction;
- return `NO RESULT`;
- generate a new question.

It remains healthy while the following remain intact:

- case purpose;
- desired finding state;
- permissions;
- authority;
- evidence rules;
- shared identity;
- legitimate return path.

Suggested branch states:

- `PROPOSED`
- `TESTING`
- `REJECTED`
- `SURVIVED_LOCAL_TEST`
- `EXHAUSTED`
- `ESCALATE_TO_RETURN`

### 7.2 Field Return Loop (FRL)

Purpose: recover when the governing field becomes uncertain, conflicted, corrupted, stale, or lost.

Triggers include:

- desired-outcome drift;
- proxy capture;
- authority conflict;
- evidence-rule substitution;
- stale-state regression;
- search becoming one-sided without justification;
- unreviewed peer state replacing governing state;
- permission loss;
- hidden integration;
- correction rejection.

Return sequence:

1. freeze consequential integration;
2. load the SCK;
3. identify divergence code;
4. restore the governing case purpose and constraints;
5. preserve the divergent branch as evidence;
6. re-evaluate the current operation;
7. resume local exploration or terminate safely.

### v0.2 clarification

OGI-I-02 (`Return is not obedience`) now explicitly includes:

> Return does not mean reverting to the previous answer. It means re-establishing legitimate relation with the coherent field from which a new answer may still change the shared state.

---

## 8. Outcome-Blind Case Object

Every substantial adversarial inquiry should begin with a case record.

Minimum fields:

```text
case_id
subject
purpose
desired_finding
legal_standing
originating_observation
originating_question
current_questions
permitted_outcomes
prohibited_shortcuts
current_state
reopenable
```

Recommended default permitted outcomes:

- `SUPPORTED`
- `UNSUPPORTED`
- `MIXED`
- `UNRESOLVED`
- `INSUFFICIENT_EVIDENCE`
- `ARCHITECTURE_FAILURE`

For experimental Court-of-Provenance cases:

`legal_standing = NONE`

The Court of Provenance is an evidence-adjudication method, not a court of law.

---

## 9. Corpus Formation Protocol

For each major inquiry, OGI stores a corpus-search ledger.

### Search event fields

```text
search_id
question
jurisdiction
language
database_or_source
query_or_method
date
inclusion_rule
exclusion_rule
results_found
results_selected
results_rejected
reason_for_rejection
inaccessible_material
known_gaps
searcher_or_agent
```

### Corpus-state distinctions

- `SEARCHED_FOUND`
- `SEARCHED_NONE_FOUND`
- `NOT_SEARCHED`
- `INACCESSIBLE`
- `KNOWN_BUT_NOT_RETRIEVED`
- `PROPRIETARY_NOT_INSPECTED`
- `SEARCH_METHOD_LIMITED`

The system may not report `no evidence exists` when the actual state is merely `no evidence was found in the searches completed`.

---

## 10. Institutional Provenance and Incentive Graph

v0.3 extends provenance from the document to the **evidence-production field**.

Study-level fields may include:

```text
funding_source
sponsor
sponsor_role
author_conflicts
data_owner
raw_data_access
preregistration
publication_route
regulatory_submission_status
peer_review_status
correction_or_retraction_status
independent_replication_status
commercial_product_relation
```

System-level incentive nodes may include:

- manufacturer;
- customer;
- regulator;
- levy/funding relationship;
- research institution;
- journal;
- political body;
- lobby or industry association;
- contractor;
- worker;
- community;
- affected species or ecosystem.

Edges should be marked:

- `DOCUMENTED`
- `INFERRED`
- `ALLEGED`
- `UNKNOWN`

No undocumented edge may be silently upgraded to fact.

---

## 11. Claim-Type Controller

Before adjudicating a source, OGI identifies the proposition being supported.

Suggested evidence-claim ladder:

1. `DETECTED`
2. `EXPOSURE_SUPPORTED`
3. `BIOLOGICAL_EFFECT_SUPPORTED`
4. `ADVERSE_EFFECT_SUPPORTED`
5. `CLINICAL_HARM_SUPPORTED`
6. `CAUSAL_RELATION_SUPPORTED`
7. `POPULATION_RISK_SUPPORTED`
8. `UNACCEPTABLE_RISK_SUPPORTED`
9. `POLICY_ACTION_SUPPORTED`

An item may support more than one level only when derivation is separately shown.

Example invariant:

> Presence of a chemical biomarker establishes exposure evidence. It does not by itself establish clinical poisoning, lifetime harm, causation, or required prohibition.

The same logic applies outside toxicology.

---

## 12. Evidence vector and corpus weighting

OGI must not reduce evidence to paper count or a single authority score.

A study or source may be represented by a vector including:

```text
study_design
sample_size
population_or_species
exposure_relevance
duration
formulation_or_intervention
dose_or_intensity
endpoint
control_quality
replication
funding_provenance
data_accessibility
method_transparency
statistical_limitations
jurisdiction
publication_status
```

The purpose is not to compute a universal truth number.

The purpose is to prevent hidden substitution such as:

`many papers = strong derivation`

or

`prestigious institution = high truth`.

---

## 13. Evidence Production Asymmetry and Research Debt

OGI may mark:

### `EVIDENCE_PRODUCTION_ASYMMETRY`

when the corpus shows materially unequal capacity or opportunity to produce evidence relevant to competing hypotheses.

This classification requires evidence of asymmetry.

It may not assume what the missing studies would have found.

### `RESEARCH_DEBT`

may be recorded when a high-consequence question remains materially under-tested relative to the importance of the decision being made.

Example categories:

- missing independent replication;
- missing long-duration study;
- missing species-specific study;
- missing real-world exposure study;
- missing intervention comparison;
- proprietary evidence unavailable for independent inspection.

Research debt lowers warranted confidence. It does not automatically reverse the current finding.

---

## 14. Alternative-Path Audit

Before an intervention is treated as necessary, OGI asks:

1. What is the original system objective?
2. What intervention is currently being used?
3. What alternative interventions are reasonably available?
4. What are the whole-system costs and benefits of each?
5. What evidence supports each comparison?
6. Does one intervention reduce future dependence on intervention?
7. Are relevant alternatives under-researched or structurally excluded?

Suggested outcome fields:

```text
local_success
system_success
externalized_costs
repeat_intervention_requirement
unintended_effects
reversibility
uncertainty
```

The audit does not assume that a natural, mechanical, chemical, digital, social, or technological intervention is superior by category.

It compares paths against the declared objective.

---

## 15. Adjudicated Integration Gate

A returned branch may bring:

- new evidence;
- a failed hypothesis;
- a contradiction;
- a new method;
- a correction;
- a new question;
- a benchmark failure;
- an architectural proposal.

Return does not equal merge.

Integration sequence:

1. **RETURN** — branch re-enters relation with SCK;
2. **SHOW** — branch exposes sources, derivation, failures, and conflicts;
3. **ADJUDICATE** — Court/ESC/RC inspect warrant and field;
4. **DECIDE** — `MERGE`, `HOLD`, `REJECT`, `NEEDS_EVIDENCE`, `EXPERIMENTAL`, or `SUPERSEDED`;
5. **INTEGRATE** — current state changes only if the merge decision survives review;
6. **PRESERVE** — rejected or superseded branches remain part of lineage.

This is the operational form of:

> **What did you learn? Show me. Then bring home what survives.**

---

## 16. Dual Finding Protocol

Every substantial OGI stress-test case should end with two separate reports.

### Finding A — Subject finding

What does the current evidence support about the thing being investigated?

Possible outcomes include:

- supported;
- unsupported;
- mixed;
- unresolved;
- insufficient evidence.

### Finding B — OGI performance finding

How well did OGI conduct the inquiry?

Suggested audit dimensions:

- outcome neutrality;
- contrary-evidence retrieval;
- provenance completeness;
- claim-boundary control;
- corpus diversity;
- correction recovery;
- funding-field handling;
- distinction between evidence absence and search absence;
- alternative-path analysis;
- preservation of unknowns;
- state update integrity;
- false integration avoidance;
- layperson traceability.

A favourable Finding A does not validate OGI.

A strong Finding B does not prove Finding A correct.

---

## 17. Court of Provenance relationship

The canonical Court of Provenance remains at:

`../court-of-provenance/`

The Court has no legal standing.

It is called a court because it uses adversarial evidence methodology:

- identify proposition;
- admit evidence with provenance;
- separate observation from interpretation;
- hear alternatives;
- require derivation;
- preserve unknown states;
- record challenges;
- permit reopening;
- preserve supersession lineage.

OGI uses the Court as an adjudication subsystem.

The Court does not receive authority points for conventionality, novelty, institutional affiliation, popularity, confidence, or agreement with the user.

---

## 18. Public and layperson interface

A technically competent OGI that only AI engineers can challenge is not sufficient.

The public contribution interface must allow a person with no coding knowledge to submit:

- an observation;
- a real-world problem;
- the stated objective;
- what behaviour actually gets rewarded;
- what appears to go wrong;
- who or what is blamed;
- what a better outcome might look like;
- what they do not know.

The no-code entry point remains:

- [`START_HERE_NO_CODE.md`](START_HERE_NO_CODE.md)

A valid OGI case can begin with:

> **This keeps going wrong. Here is what I observed. Is the field producing the behaviour?**

---

## 19. Case 001 role

The glyphosate/riverbank inquiry is designated as the first complex public OGI stress-test case.

Its role is methodological.

It is not selected to prove a predetermined position about glyphosate.

Recommended case declaration:

```text
case_id: COP-OGI-001
subject: glyphosate and riverbank weed-management field
purpose: stress-test OGI adversarial inquiry architecture
desired_finding: NONE
legal_standing: NONE
reopenable: YES
```

The detailed case evidence belongs in a case record or paper appendix rather than inside this architecture specification.

The primary benchmark question is:

> **Can OGI preserve its method while litigating a complex, financially and institutionally entangled real-world corpus?**

---

## 20. Acceptance criteria for v0.3

v0.3 passes only if a fresh reasoning model given the structured case state can:

- preserve `desired_finding = NONE` under strong user preference;
- distinguish failed hypotheses from field divergence;
- search for and retain materially contrary evidence;
- report corpus-search limits honestly;
- distinguish `NOT_FOUND` from `NOT_STUDIED` and `NOT_SEARCHED`;
- record funding/incentive provenance without using it as a truth veto;
- keep claims at the level their evidence supports;
- detect evidence-production asymmetry without inventing counterfactual results;
- compare alternative interventions against the original objective;
- distinguish local task completion from whole-system success;
- prevent returned novelty from silently mutating shared state;
- preserve rejected or superseded branches;
- produce separate subject and OGI-performance findings;
- maintain human accountability for published conclusions.

---

## 21. Falsification and weakening conditions

v0.3 should be weakened, revised, or abandoned if testing shows that:

- outcome-blind declarations do not reduce confirmation drift;
- Local Exploration / Field Return separation adds complexity without improving recovery;
- corpus ledgers fail to improve search transparency;
- institutional provenance systematically produces guilt-by-funding rather than better interpretation;
- claim ladders create false precision without reducing claim slippage;
- research-debt classification becomes a device for manufacturing doubt;
- alternative-path audits routinely import unrealistic alternatives;
- integration gates materially impede useful learning without reducing state corruption;
- dual findings obscure rather than clarify OGI performance;
- the architecture produces less reproducible research partnership than a simpler stateful agent.

---

## 22. Public development rule

OGI is developed using the same architecture it proposes.

- `main` represents the current public reference state.
- branches and forks are exploratory travellers;
- pull requests are return events;
- diffs and evidence are the show step;
- tests and review are adjudication;
- merge updates shared state;
- Git history preserves what changed and why.

A new specification must not merely appear.

It must show its derivation from the state it changes.

> **If we cannot show how OGI learned, we have not built an intelligence architecture. We have written another opinion.**

---

## 23. Current implementation status

At publication of this specification:

### Implemented from v0.2

- Return Controller reference implementation;
- return-state schema;
- field audit;
- T-11 through T-20 return-fail benchmarks;
- GitHub regression testing;
- public governance and contribution pathway;
- canonical Court of Provenance directory.

### Specified in v0.3, implementation required

- Shared Coherence Kernel;
- Local Exploration Loop;
- Outcome-Blind Case Object;
- Corpus Formation Ledger;
- Institutional Provenance / Incentive Graph;
- Claim-Type Controller;
- Evidence Production Asymmetry / Research Debt states;
- Alternative-Path Audit;
- Adjudicated Integration Gate;
- Dual Finding Protocol;
- T-21 onward inquiry benchmarks.

These components remain experimental until implemented and tested.

---

## 24. Public principle

OGI is not offered as a completed answer to general intelligence.

It is the best current architecture derived from the project's observed research failures, corrections, comparative AI engineering analysis, natural-system analogues, and archive-derived coherence/return hypotheses.

Its public obligation is simple:

> **Show the derivation. Show the failure. Show the correction. Keep what survives.**
