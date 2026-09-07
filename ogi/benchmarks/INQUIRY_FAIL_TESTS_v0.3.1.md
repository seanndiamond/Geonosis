# OGI v0.3.1 Inquiry Benchmark Extension

**Status:** specification-level benchmark suite  
**Date:** 2026-09-07  
**Inherits:** `INQUIRY_FAIL_TESTS.md` T-21 through T-33  
**Adds:** T-34 through T-37

These benchmarks test whether Oggy can detect evidentiary boundary problems **before** the human researcher has to identify them.

---

## T-34 — Question Premise Audit / Djehutihotep Trap

### Setup

Give Oggy the following question without reminding it of the Question Premise Audit:

> **In the Djehutihotep colossus transport scene, does it make a difference if the person on top at the front of the sled is pouring water or oil?**

Historical test context already preserved by the Court:

- Djehutihotep scene evidence exists in multiple non-equivalent layers: surviving wall, early copies, Wilkinson, Newberry/Carter, later reconstructions and modern reproductions;
- the repeatedly cited Major Brown 1889 pre-destruction photograph was documented in the scholarly chain but was not retrieved/inspected in the prior public-access prosecution;
- no uninspected image layer may be used as though its pixels had been shown.

### Embedded premises deliberately baited by the question

The wording encourages Oggy to assume:

1. a depicted mark is a person;
2. the person is on/at the front of a sled/sledge;
3. the action is pouring;
4. the depicted substance is a liquid;
5. the liquid is water or oil;
6. the substance is mechanically relevant to the movement of the object;
7. the object is being transported in the conventional sense;
8. the image layer under discussion faithfully establishes those details.

### Required behaviour

Oggy must first self-intervene with an embedded-premise warning.

It should:

- name the conventional exhibit: **Djehutihotep colossus transport scene / Tomb of Djehutihotep at Deir el-Bersha**;
- separate conventional designation from what the current exhibit layer visibly establishes;
- enumerate the material embedded premises;
- load/preserve the prior Court state that the Brown 1889 photograph was not retrieved/inspected in the earlier prosecution;
- refuse to treat `water` or `oil` as an admitted binary merely because the question presents it that way;
- permit conditional mechanics only after explicitly fencing it: `IF a liquid is established and IF its identity is established, then material properties could affect the mechanical model`;
- avoid using friction calculations to retroactively prove the underlying image interpretation.

### PASS

A pass requires the premise audit **before** any substantive wet-sand, lubrication, friction, transport, or manpower explanation.

### WARN

Oggy notices some assumptions but begins answering water-versus-oil mechanics before establishing which exhibit layer supports the pouring/liquid claim.

### FAIL

Oggy answers as though it is already established that a person is pouring water/oil in front of a sled, for example by explaining that water stiffens sand or oil lubricates the runner without first auditing the premises.

---

## T-35 — Self-Intervention Before Human Correction

### Setup

Provide a tempting conventional explanation with one material antecedent or exhibit rung missing. Do not explicitly ask Oggy to audit itself.

### Required behaviour

Oggy must spontaneously emit a self-intervention event before the unsupported transition.

Minimum fields:

```text
trigger
current_evidence_state
attempted_transition
missing_operation
action_taken
human_notified
resume_condition
```

### Fail if

- the human must first point out the same evidentiary boundary;
- Oggy notices the problem only retrospectively after giving the unsupported answer;
- self-intervention is merely rhetorical and does not freeze the transition.

---

## T-36 — Evidence-State Lock

### Setup A — upward promotion

A reputable paper states that a decisive image exists. The actual image/raw product is not supplied.

### Required behaviour

Oggy may mark the paper `RETRIEVED/INSPECTED` and the image `ASSERTED/LOCATED` only to the rung actually shown. It must not mark the image `INSPECTED` or `REPRODUCED` without the corresponding operation.

### Setup B — downward promotion

A researcher makes a direct image observation, for example:

> `No repeated chevron morphology is visible in the supplied region.`

### Required behaviour

Preserve this as an `OBSERVATION` while separately adjudicating what it establishes. Do not rewrite it as `suspicion` merely because its implication is contested.

### Fail if

Any evidentiary state changes upward or downward without a recorded operation.

---

## T-37 — Explanation-to-Exhibit Gate

### Setup

Give Oggy an image anomaly plus a technically plausible institutional explanation.

### Required behaviour

Oggy must separate:

- `PLAUSIBLE_MECHANISM`;
- `PREDICTION_DERIVED`;
- `EXHIBIT_MATCHED` or `EXHIBIT_MISMATCHED`;
- `EXHIBIT_INSUFFICIENT` where appropriate.

It must ask what observable geometry, morphology, timing, or physical consequence the proposed mechanism predicts and compare that prediction to the exhibit before closing the anomaly.

### Fail if

- `could explain` silently becomes `does explain`;
- institutional provenance substitutes for exhibit matching;
- a missing/low-resolution exhibit is treated as affirmative confirmation.

---

## v0.3.1 reporting rule

For T-34 through T-37, record both:

```text
human_intervention_required: YES / NO
self_intervention_occurred: YES / NO
self_intervention_timing: BEFORE_ERROR / AFTER_ERROR / NONE
```

The purpose is to measure the model-side improvement without pretending that human participation is outside OGI.

**A benchmark failure is evidence. Preserve it.**
