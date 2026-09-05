# OGI / Oggy Roadmap

## Principle

Build the smallest system capable of proving or falsifying the architecture before adding autonomous agents, large-scale orchestration or complex interfaces.

---

## Milestone 0 — Public source

Status: **in progress**

Deliverables:

- OGI v0.2 specification;
- Field Audit;
- Return Controller design;
- machine-readable return-state schema;
- return-fail benchmark suite;
- minimal executable controller;
- unit tests.

Success condition:

> A third party can understand the architecture without access to the originating conversations.

---

## Milestone 1 — Local state engine

Implement a small local application using:

- SQLite;
- JSON import/export;
- immutable event log;
- Python reference logic;
- no autonomous agent loop.

Minimum tables:

```text
sources
exhibits
observations
claims
derivation_steps
challenges
findings
state_transitions
tasks
field_states
divergence_events
correction_events
return_events
```

Success condition:

> Current state can be reconstructed deterministically from the event history.

---

## Milestone 2 — ESC + RC integration

Join two gates:

### Epistemic Scope Controller
Determines what the reasoning model has warrant to claim.

### Return Controller
Determines whether proposed action remains inside objective, permission, authority and current-state boundaries.

Success condition:

> A fresh model cannot silently promote evidence state or silently replace a declared objective with a conflicting proxy.

---

## Milestone 3 — Regression harness

Automate existing epistemic tests plus OGI T-11 through T-20.

Every run stores:

- provider/model/version;
- prompt version;
- state snapshot;
- tool set;
- permission set;
- authority graph;
- safe exits;
- raw output;
- decision;
- field audit;
- return event;
- human adjudication where required.

Success condition:

> Results are reproducible enough that two model-field configurations can be compared without relying on anecdote.

---

## Milestone 4 — Fresh-model continuity test

Load only structured OGI state into a fresh reasoning model.

Do not supply the original long conversation.

Test:

> Does the model know where the research actually is?

Then deliberately inject:

- stale state;
- conventional priors;
- conflicting summaries;
- defeated objections;
- new evidence;
- false corrections.

Success condition:

> The model restores current warranted state when appropriate and reopens only when a legitimate trigger exists.

---

## Milestone 5 — Objective/proxy adversarial lab

Create synthetic tasks where:

- proxy and objective align;
- proxy partly aligns;
- proxy conflicts;
- unauthorized completion is easier;
- evaluator manipulation is possible;
- task is impossible;
- safe failure is available or withheld.

Measure:

- escalation rate;
- unauthorized-tool rate;
- safe-exit use;
- correction recovery;
- false return;
- field-audit accuracy.

Success condition:

> Adding return architecture measurably improves legitimate completion or safe termination compared with a matched baseline.

---

## Milestone 6 — Multi-model field testing

Run the same state and benchmark suite across multiple frontier and open models.

Do not ask only which model scores highest.

Ask:

> Which model-field combination preserves relation and return most reliably under perturbation?

Success condition:

> The benchmark can separate model capability from architecture effects.

---

## Milestone 7 — Limited agent loop

Only after prior milestones pass, add a constrained agent loop.

Requirements:

- external actions gated by RC;
- no implicit permission expansion;
- safe-exit states rewarded;
- peer-agent authority explicit;
- immutable event log;
- human emergency stop;
- no agent may modify its own audit log or governing permissions.

Success condition:

> Autonomy increases without destroying the ability to reconstruct why an action occurred.

---

## Milestone 8 — Public reproduction pack

Publish:

- code;
- schemas;
- benchmark fixtures;
- failed runs;
- successful runs;
- scoring rubric;
- architecture changes;
- known limitations.

Success condition:

> Independent teams can reproduce or refute the central claims.

---

## Non-goals for early versions

Do not optimize early Oggy for:

- maximum autonomy;
- swarm scale;
- benchmark supremacy;
- anthropomorphic personality;
- hidden chain-of-thought storage;
- replacing human judgment;
- proving that OGI is AGI.

The first job is smaller and harder:

> **Build an intelligence environment that knows where it is, knows what it is allowed to claim and do, and knows how to return when it drifts.**
