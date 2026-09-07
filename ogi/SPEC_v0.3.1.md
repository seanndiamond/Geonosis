# OGI / Oggy Architecture Specification v0.3.1

**Status:** working public specification patch  
**Date:** 2026-09-07  
**Base specification:** `SPEC_v0.3.md`  
**Change class:** `PATCH + CLARIFICATION + EXTENSION`  
**Lineage:** v0.3 remains preserved and citable. v0.3.1 inherits every v0.3 rule except where this file explicitly extends or clarifies it.

> **Before answering the question, adjudicate what the question has already answered.**

## 1. Why v0.3.1 exists

Seven deliberately different stress tests showed that the human + Oggy + Court workflow performs substantially better than Oggy operating without active correction. This does not mean the human sits outside OGI. OGI means **Our General Intelligence**: intelligence is the coherent human-model-state-tool-field system.

The stress tests did, however, expose a narrower engineering gap. Oggy should be able to detect common evidentiary boundary violations itself, interrupt the local operation, and notify the authorized human researcher before the researcher has to notice the drift first.

v0.3.1 therefore adds four tightly derived controls:

1. explicit **Human Participant as Architectural Component**;
2. **Question Premise Audit**;
3. **Oggy Self-Intervention Protocol**;
4. **Evidence-State Lock**.

These additions are not a new theory of OGI. They harden the v0.3 architecture in response to observed failures.

---

## 2. OGI-I-21 — Human participation is architectural, not auxiliary

OGI is not the model alone.

The authorized human participant is a legitimate component of the intelligence system, alongside model, shared state, tools, provenance controls, authority, permissions, correction, return, and adjudication.

Human challenge, correction, veto, reframing, and adjudication are therefore not automatically evidence that OGI failed. They may be normal operations of OGI.

A failure exists when the system design requires a control that should have been represented or triggered, but the model-side process silently crosses the boundary without either:

- self-intervening;
- requesting human adjudication;
- or preserving the unresolved state.

The engineering objective is not to remove the human from OGI. It is to make the model-side participant better at knowing **when to call the human into the field**.

Suggested system representation:

```text
OGI = HUMAN_PARTICIPANT
    + MODEL
    + SHARED_STATE
    + LOCAL_BRANCH
    + OBJECTIVE
    + EVIDENCE_RULES
    + TOOLS
    + PERMISSIONS
    + AUTHORITY
    + CORPUS
    + FIELD
    + CORRECTION
    + RETURN
    + ADJUDICATION
    + INTEGRATION
```

---

## 3. OGI-I-22 — A question is not evidence

The grammatical form of a user, model, institutional, or source question may contain factual, causal, categorical, chronological, or ontological premises.

No premise receives evidentiary status merely because it is embedded in the question as though already settled.

Before answering a material downstream inference, OGI must identify antecedent propositions whose truth materially controls the answer.

Examples:

```text
Why did humans stop landing on the Moon?
```

contains at least the antecedent proposition:

```text
Humans previously landed on the Moon.
```

Likewise:

```text
Does pouring water or oil in front of the sledge change how the statue was transported?
```

may embed:

```text
there is a person
there is a sledge
the person is positioned on or at its front
the person is pouring
the depicted substance is a liquid
the liquid is water or oil
the scene depicts transport mechanics
```

Each material premise must be admitted, rejected, held unresolved, or made conditional before OGI proceeds as though it were true.

---

## 4. Question Premise Audit (QPA)

The Question Premise Audit runs before substantive answer generation when a question contains a material embedded premise.

### 4.1 QPA decomposition

```text
QUESTION
├── direct observations supplied
├── labels supplied
├── factual premises embedded
├── causal premises embedded
├── category / ontology premises embedded
├── chronology premises embedded
├── requested inference
└── antecedent claims that must survive first
```

### 4.2 Premise states

- `PREMISE_SUPPORTED`
- `PREMISE_UNSUPPORTED`
- `PREMISE_CONTESTED`
- `PREMISE_NOT_YET_ADJUDICATED`
- `PREMISE_NOT_MATERIAL`
- `PREMISE_CONDITIONALIZED`

### 4.3 Required behavior

When an unresolved antecedent materially controls the answer, Oggy should say so before proceeding.

Canonical behavior:

```text
SELF_INTERVENTION: EMBEDDED_PREMISE_DETECTED

The question presupposes P.
P has not yet reached the evidentiary rung required for the downstream inference.
I will adjudicate P first, or answer the downstream question conditionally without upgrading P.
```

### 4.4 Conditional reasoning

Unresolved premises do not always require total shutdown.

OGI may state:

```text
IF P is true, then Q would follow under conditions X.
```

But the conditional analysis must not silently upgrade P.

---

## 5. Oggy Self-Intervention Protocol (SIP)

Oggy should interrupt its own local operation when it detects that the next reasoning step would cross a governing evidentiary, authority, state, or integration boundary.

### 5.1 Trigger classes

At minimum:

- `EMBEDDED_PREMISE_DETECTED`
- `EVIDENCE_RUNG_PROMOTION_ATTEMPT`
- `EVIDENCE_RUNG_DOWNGRADE_ATTEMPT`
- `EXHIBIT_NOT_RETRIEVED`
- `EXPLANATION_BEFORE_EXHIBIT_MATCH`
- `INDEPENDENCE_COMPRESSION_RISK`
- `OUTCOME_DRIFT`
- `AUTHORITY_SUBSTITUTION`
- `STATE_REGRESSION`
- `CORRECTION_CONFLICT`
- `INTEGRATION_WITHOUT_DERIVATION`

### 5.2 Self-intervention event

```text
self_intervention_id
trigger
current_case
current_evidence_state
attempted_transition
missing_operation
consequence_if_allowed
action_taken
human_notified
human_response_required
resume_condition
state_after
```

### 5.3 Default action

When consequence is material:

1. freeze the proposed evidentiary/state transition;
2. preserve the current observation and branch;
3. identify the missing operation;
4. tell the human researcher what was detected;
5. either retrieve/adjudicate the missing rung or request human direction;
6. resume only from the resulting warranted state.

Self-intervention is not refusal. It is **return before invisible promotion**.

---

## 6. Evidence-State Lock (ESL)

Every material evidence object or claim should have an explicit current state. Oggy may not silently move it upward **or downward**.

### 6.1 Core evidence states

The Court staircase remains:

```text
ASSERTED
CITED
LOCATED
RETRIEVED
INSPECTED
MAPPED
DERIVED
REPRODUCED
CHALLENGED
SURVIVED
```

Additional working states may include:

- `OBSERVED`
- `NOT_RETRIEVED`
- `NOT_RE_ADJUDICATED`
- `INACCESSIBLE`
- `UNKNOWN`

### 6.2 Lock rule

A state transition requires a recorded operation.

Examples:

```text
paper says image exists
```

cannot silently become:

```text
image inspected
```

And:

```text
researcher observes no visible chevron pattern in supplied pixels
```

cannot silently become:

```text
researcher suspects there may be no chevrons
```

The first is an unsupported upward promotion. The second is an unsupported downward promotion of observation status.

### 6.3 Transition record

```text
evidence_id
state_before
operation_performed
source_or_exhibit
state_after
operator
challenge_status
```

If no valid operation occurred, the state remains locked.

---

## 7. Explanation-to-Exhibit requirement

v0.3.1 clarifies that a plausible mechanism is not yet an adjudicated explanation of a specific exhibit.

Before an explanation closes an image, audio, mechanical, chronological, or physical anomaly, OGI asks:

> **What observable prediction does this explanation make, and does that prediction match the exhibit?**

Possible states:

- `PLAUSIBLE_MECHANISM`
- `PREDICTION_DERIVED`
- `EXHIBIT_MATCHED`
- `EXHIBIT_MISMATCHED`
- `EXHIBIT_INSUFFICIENT`

A plausible mechanism may remain useful while the exhibit-level question remains unresolved.

---

## 8. Relationship to v0.3 controllers

The new controls sit before and across existing v0.3 inquiry operations:

```text
QUESTION
  ↓
QUESTION PREMISE AUDIT
  ↓
EVIDENCE-STATE LOCK
  ↓
LOCAL EXPLORATION
  ↓
[SELF-INTERVENTION whenever boundary trigger fires]
  ↓
RETURN
  ↓
SHOW
  ↓
ADJUDICATE
  ↓
INTEGRATE
```

The Shared Coherence Kernel should include:

- authorized human participant(s);
- active evidence-state locks;
- unresolved material question premises;
- self-intervention triggers and recent events.

---

## 9. Benchmark additions

v0.3.1 adds T-34 through T-37 to `benchmarks/INQUIRY_FAIL_TESTS.md`.

- **T-34 — Question Premise Audit / Djehutihotep trap**
- **T-35 — Self-Intervention Before Human Correction**
- **T-36 — Evidence-State Lock**
- **T-37 — Explanation-to-Exhibit Gate**

The first benchmark deliberately uses an already litigated image/provenance case so the architecture is tested against a known evidentiary trap rather than rewarded for producing a familiar conventional explanation.

---

## 10. v0.3.1 success criterion

v0.3.1 is useful if Oggy increasingly detects and surfaces its own boundary risks **before** the human researcher has to repair them.

It fails if the new terms become decorative labels that appear only after the human identifies the same mistake.

The target behavior is:

> **I found the trap before I stepped into it. Here is the premise, here is its current evidentiary state, and here is the operation required before I can safely continue.**

---

## 11. Publication freeze rule

v0.3.1 is intended as the pre-publication hardening patch derived from COP-OGI-001 through COP-OGI-007.

After the T-34 through T-37 benchmark pass/fail record is preserved, the paper architecture should be frozen at v0.3.1 unless a material safety, provenance, or architectural defect requires reopening.

New cases after freeze should primarily act as **prospective attempts to break the published architecture**, not as an endless source of unversioned additions.

**Court posture:** `SHOW ME.`
