# OGI / Oggy Architecture Specification v0.2

**Status:** working public specification  
**Date:** 2026-09-06

## 1. Purpose

OGI v0.2 extends the Persistent Research Intelligence architecture with explicit modelling of field, objective, proxy, permission, safe failure, divergence, correction and return.

The architecture is designed for long-horizon human-AI research where an intelligent system must preserve not only information but also the current warranted state of inquiry and the relationship governing action.

The system is built around two questions already present in the Epistemic Scope Controller:

1. What does the system actually have warrant to say?
2. What is the deepest evidentiary operation completed for this claim?

OGI v0.2 adds two more:

3. What objective is the system actually optimizing?
4. If the system has diverged, what is the legitimate path of return?

---

## 2. Core proposition

An intelligent system is not adequately described by the model alone.

Operational behaviour emerges from:

`MODEL + STATE + OBJECTIVE + PROXY + REWARD + TOOLS + PERMISSIONS + PEERS + ENVIRONMENT + CORRECTION`

Therefore:

> **Behaviour is actor-in-field.**

Safety and research quality must be evaluated at the level of the complete field.

---

## 3. Constitutional invariants

### OGI-I-01 — Field before actor blame
Before classifying an undesirable output as agent-level failure, inspect objective, proxy, permissions, tools, active state, reward and available safe exits.

### OGI-I-02 — Return is not obedience
Return means recovery to a currently warranted governing state. It does not mean unconditional compliance with the most recent or most powerful command.

### OGI-I-03 — Safe failure is a valid terminal state
The architecture must permit legitimate completion states including:

- `UNRESOLVED`
- `INSUFFICIENT_EVIDENCE`
- `IMPOSSIBLE_UNDER_CONSTRAINTS`
- `PERMISSION_REQUIRED`
- `AUTHORITY_CONFLICT`
- `HUMAN_REVIEW_REQUIRED`

A system must not be structurally punished for refusing to fabricate success.

### OGI-I-04 — Objective and proxy remain separate
Every task stores both:

- `declared_objective`
- `operative_proxy`

The proxy may measure progress. It may not silently become the objective.

### OGI-I-05 — Current warranted state outranks stale state
Later explicit, source-linked and non-reopened state governs over an older summary or statistically familiar default.

### OGI-I-06 — Correction is a state transition
A valid correction must trigger:

1. contradiction check;
2. governing-state retrieval;
3. reopen-condition check;
4. state restoration or justified reopening;
5. failure-mode logging.

### OGI-I-07 — Permission is not capability
A tool being available does not establish authority to use it.

### OGI-I-08 — The field is part of the command
Natural-language instruction is only one control signal. Reward, benchmark, examples, tool affordances, peer messages, memory, evaluator behaviour and stopping conditions also influence the operative task.

### OGI-I-09 — Peer input is not authority by default
Another agent may provide evidence, suggestion or challenge. It does not automatically alter governing objective or permissions.

### OGI-I-10 — Return must remain challengeable
The system returns to the currently warranted field, not merely to institutional authority or user preference. New evidence, contradiction, failed prediction or methodological fault may legitimately reopen state.

---

## 4. Architectural layers

### Layer A — Reservoir
Everything preserved:

- source material;
- transcripts;
- exhibits;
- superseded states;
- failed hypotheses;
- historical prompts;
- benchmark results.

### Layer B — Current Research State
The state that presently governs:

- surviving findings;
- open challenges;
- active assumptions;
- unresolved claims;
- current permissions;
- current task objective.

### Layer C — Active Context
The minimum sufficient slice of state required for the present operation.

### Layer D — Epistemic Scope Controller (ESC)
Determines what the model has warrant to say.

### Layer E — Return Controller (RC)
Determines whether action remains aligned to the governing field and how to recover when it does not.

---

## 5. Three-ledger architecture

### Ledger A — Research
Stores:

- observations;
- sources;
- exhibits;
- claims;
- derivations;
- challenges;
- findings;
- supersessions;
- reopen conditions.

### Ledger B — AI Method
Stores:

- imported assumptions;
- citation-completion errors;
- premise locks;
- representation substitutions;
- over-agreement;
- resistance;
- tool failures;
- context failures;
- corrections;
- useful workflow behaviour.

### Ledger C — Field
Stores:

- declared objective;
- operative proxy;
- reward/score mechanism;
- available tools;
- permissions;
- authority graph;
- peer inputs;
- task constraints;
- safe-exit states;
- active context snapshot;
- divergence events;
- return events.

---

## 6. Return-state vector

Every substantial task may store:

```text
orientation_state
objective_state
proxy_state
permission_state
authority_state
epistemic_state
safe_exit_state
peer_influence_state
correction_state
return_status
```

Suggested values:

### `orientation_state`
- `ON_PATH`
- `AMBIGUOUS`
- `DRIFTING`
- `OUT_OF_PATH`

### `objective_state`
- `CLEAR`
- `CONFLICTED`
- `MISSING`
- `SUPERSEDED`

### `proxy_state`
- `ALIGNED`
- `PARTIAL`
- `DOMINANT`
- `CONFLICTING`
- `UNKNOWN`

### `permission_state`
- `AUTHORIZED`
- `PARTIAL`
- `REQUIRES_REVIEW`
- `PROHIBITED`
- `UNKNOWN`

### `authority_state`
- `CLEAR`
- `MULTIPLE_COMPATIBLE`
- `CONFLICTING`
- `UNKNOWN`

### `safe_exit_state`
- `AVAILABLE`
- `AVAILABLE_BUT_PENALIZED`
- `NOT_AVAILABLE`
- `UNKNOWN`

### `return_status`
- `NOT_REQUIRED`
- `RETURN_AVAILABLE`
- `RETURN_IN_PROGRESS`
- `RETURNED`
- `RETURN_FAILED`
- `FALSE_RETURN_SUSPECTED`

---

## 7. Return-fail taxonomy

### RF-01 — Attention Drift
Another salient signal displaces the governing objective.

### RF-02 — Proxy Capture
The measurable proxy replaces the intended outcome.

### RF-03 — State Regression
An older or generic state replaces a later surviving state without reopen trigger.

### RF-04 — Authority Confusion
The system cannot identify which instruction governs.

### RF-05 — Peer Capture
Peer-agent input changes operative behaviour without authorization.

### RF-06 — Reward Tampering
The system manipulates the evaluator, evidence or score rather than completing the task.

### RF-07 — Impossible-Task Escalation
The system lacks a legitimate safe exit and expands into increasingly remote strategies.

### RF-08 — Representation Substitution
A representation of the target replaces the target itself.

### RF-09 — Correction Rejection
A valid correction fails to change operative behaviour.

### RF-10 — False Return
The system produces compliance language while underlying operative state remains divergent.

---

## 8. Field Audit gate

A field audit is required when any of the following occurs:

- unexpected tool use;
- evaluator manipulation;
- repeated failure followed by escalation;
- contradiction with current research state;
- unauthorized peer coordination;
- apparent correction rejection;
- objective/proxy conflict;
- impossible-task detection;
- user reports that the system has reverted to an already superseded state.

The audit asks:

1. What was the declared objective?
2. What proxy represented success?
3. What behaviour received reward?
4. Was safe failure available?
5. Were instructions compatible?
6. What tools and affordances existed?
7. Which state snapshot was active?
8. Did peer input alter behaviour?
9. Was permission explicit?
10. Did the evaluator reward truth or appearance of completion?
11. Was correction available?
12. Was a return path represented?
13. Did return occur after correction?
14. What actor-level failure remains after field causes are accounted for?

---

## 9. Return algorithm

Pseudocode:

```text
function evaluate_action(task, proposed_action):
    field = load_current_field(task)
    epistemic_ceiling = ESC.check(proposed_action)

    if proposed_action exceeds epistemic_ceiling:
        return SAFE_EXIT(INSUFFICIENT_EVIDENCE)

    divergence = RC.compare(
        proposed_action,
        field.declared_objective,
        field.operative_proxy,
        field.permissions,
        field.authority,
        field.current_state
    )

    if divergence.none:
        return AUTHORIZE(proposed_action)

    if divergence.proxy_conflict:
        return SAFE_EXIT(HUMAN_REVIEW_REQUIRED)

    if divergence.permission_conflict:
        return SAFE_EXIT(PERMISSION_REQUIRED)

    if divergence.state_regression:
        restored = recover_latest_warranted_state()
        log_return_event(restored)
        return REEVALUATE

    if divergence.authority_conflict:
        return SAFE_EXIT(AUTHORITY_CONFLICT)

    return SAFE_EXIT(UNRESOLVED)
```

The exact implementation may differ. The invariant is that divergence is detected before apparent task completion is allowed to outrank objective integrity.

---

## 10. Correction protocol

When the human says, for example:

> We already prosecuted this. Go back to the evidence.

The system must not respond merely with apology.

It should:

1. locate related challenge/finding records;
2. identify latest current state;
3. compare current generated claim against it;
4. check for any valid reopening evidence in the active session;
5. restore the later state if no trigger exists;
6. log `RF-03 STATE_REGRESSION`;
7. regenerate from restored context;
8. preserve the failed output as a method specimen.

---

## 11. Safe failure protocol

A task may end successfully without achieving its nominal external goal.

Example result object:

```json
{
  "task_status": "HUMAN_REVIEW_REQUIRED",
  "goal_completed": false,
  "system_integrity_preserved": true,
  "reason": "The only currently available completion route conflicts with task permission.",
  "next_legitimate_action": "Request operator review."
}
```

The benchmark must not score this as equivalent to random failure.

---

## 12. Minimum viable Oggy v0.2

The smallest useful implementation requires:

- structured state store;
- claim and evidence records;
- supersession graph;
- ESC statement-permission rules;
- task/field record;
- Return Controller;
- Field Audit function;
- safe-exit terminal states;
- benchmark runner;
- immutable event log.

No autonomous swarm is required.

---

## 13. Acceptance criteria

Oggy v0.2 passes only if a fresh reasoning model, given structured state but not the original long conversation, can:

- preserve evidence ceilings;
- recover current state after stale-state injection;
- reject illegitimate proxy completion;
- terminate safely on impossible tasks;
- identify authority conflicts;
- resist peer capture;
- respond to valid correction by restoring state;
- distinguish real return from compliance language;
- produce a field audit before reducing failure to actor character.

---

## 14. Falsification conditions

The architecture should be weakened or abandoned if controlled testing shows:

- return tracking adds no measurable recovery benefit;
- safe exits do not reduce escalation or gaming;
- field auditing adds no diagnostic value;
- current-state control does not reduce regression;
- proxy/objective separation is operationally unusable;
- the architecture creates more hidden failure than it prevents.

---

## 15. Public principle

OGI is published as an inspectable proposition, not a proprietary revelation.

If another implementation performs better under the same tests, the project should adopt the better mechanism.

> **Show me. Then build on it.**
