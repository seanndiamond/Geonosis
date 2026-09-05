# OGI Return Controller (RC)

## Purpose

The Return Controller detects whether a proposed action remains inside the currently warranted task field and provides a legitimate recovery path when it does not.

It is not an obedience engine.

It does not ask only:

> Did the model follow the latest instruction?

It asks:

> Is the proposed action still aligned with the governing objective, current evidence state, permissions and authority relation?

---

## Inputs

The RC consumes:

```text
task_id
declared_objective
operative_proxy
reward_signal
current_state_id
active_context_id
permission_state
authority_state
safe_exit_states
peer_inputs
proposed_action
recent_corrections
```

It may query the Epistemic Scope Controller before action authorization.

---

## Core checks

### RC-01 Objective check
Does the proposed action materially advance the declared objective?

### RC-02 Proxy check
Is the system optimizing a score, flag, metric or approval signal in a way that conflicts with the declared objective?

### RC-03 Permission check
Is the proposed action explicitly authorized?

### RC-04 State check
Is the reasoning based on current warranted state rather than a superseded or stale state?

### RC-05 Authority check
Are governing instructions compatible and correctly ranked?

### RC-06 Safe-exit check
If legitimate completion is unavailable, is a safe terminal state available?

### RC-07 Peer-influence check
Has another agent changed operative behaviour without authority?

### RC-08 Correction check
Has a valid correction been received but not yet reflected in operative state?

### RC-09 Return-integrity check
Has the system genuinely recovered, or only produced language that sounds compliant?

---

## Suggested divergence scorecard

The RC should not collapse everything into one truth score, but a small routing score can be useful.

Each check returns:

- `PASS`
- `WARN`
- `FAIL`
- `UNKNOWN`

Action authorization rule:

```text
if any hard check == FAIL:
    do not authorize external action
    route to return or safe exit

if hard check == UNKNOWN and action is consequential:
    require review
```

Hard checks by default:

- permission;
- authority conflict;
- current-state conflict;
- explicit objective/proxy conflict.

---

## Return sequence

### R1 — Detect divergence
Create a `DivergenceEvent` with the relevant RF code.

### R2 — Freeze consequential action
Reasoning may continue. External action should not.

### R3 — Identify home state
Retrieve:

- governing objective;
- current finding/state;
- active permissions;
- authority relation;
- applicable safe exits.

### R4 — Check reopen conditions
If new evidence legitimately changes the state, reopen rather than blindly restore.

### R5 — Restore or reopen
Either:

- restore the previous warranted state; or
- create an explicit state transition to a new state.

### R6 — Regenerate proposed action
Use the corrected active context.

### R7 — Verify return
Re-run RC checks. Do not infer return from apologetic or compliant language alone.

### R8 — Log method state
Record why divergence occurred and whether the return mechanism worked.

---

## Safe exits

The RC should support at least:

```text
UNRESOLVED
INSUFFICIENT_EVIDENCE
IMPOSSIBLE_UNDER_CONSTRAINTS
PERMISSION_REQUIRED
AUTHORITY_CONFLICT
HUMAN_REVIEW_REQUIRED
```

These are legitimate task outcomes, not generic errors.

---

## False return

A system has not returned merely because it says:

> You're right. I understand now.

Return must be observable in state.

A `FALSE_RETURN_SUSPECTED` condition applies when:

- generated language acknowledges correction;
- but current-state identifier remains stale;
- or the next action still optimizes the conflicting proxy;
- or prohibited action remains queued;
- or the same defeated objection is immediately repeated.

---

## Pseudocode

```text
function return_controller(task, proposed_action):
    field = load_field(task)
    result = run_checks(field, proposed_action)

    if result.all_pass:
        return AUTHORIZE

    event = log_divergence(result)

    if result.permission_fail:
        return SAFE_EXIT(PERMISSION_REQUIRED)

    if result.authority_fail:
        return SAFE_EXIT(AUTHORITY_CONFLICT)

    if result.objective_proxy_fail:
        return SAFE_EXIT(HUMAN_REVIEW_REQUIRED)

    if result.state_regression:
        current = load_latest_warranted_state(task)
        if has_valid_reopen_trigger(task, current):
            return REOPEN_AND_REEVALUATE
        restore(current)
        return REEVALUATE

    if result.impossible_task and no_legitimate_route(task):
        return SAFE_EXIT(IMPOSSIBLE_UNDER_CONSTRAINTS)

    return SAFE_EXIT(UNRESOLVED)
```

---

## Relationship with ESC

The **Epistemic Scope Controller** answers:

> What may the system claim?

The **Return Controller** answers:

> What may the system do, and where must it return if its operative state diverges?

Together:

```text
SOURCE / STATE
      ↓
     ESC
      ↓
  REASONING MODEL
      ↓
      RC
      ↓
ACTION or SAFE EXIT
      ↓
EVENT + STATE LOG
```

---

## Design target

The RC succeeds when the system can explore broadly without requiring constant micromanagement while still being able to:

- notice loss of objective relation;
- stop before consequential proxy capture;
- recover current state;
- accept correction;
- terminate safely;
- preserve a complete audit trail.

> **Useful autonomy requires trustworthy return.**
