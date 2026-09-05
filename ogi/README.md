# Our General Intelligence (OGI) / Oggy

**Reference source v0.2**  
**Status:** experimental public architecture  
**Date:** 2026-09-06  
**Author:** Sean Diamond, Geonosis Project, with AI-assisted formulation and implementation

> **Not bad dog. Not bad AI. Inspect the field. Build the return path.**

OGI, **Our General Intelligence**, is an experimental architecture for long-horizon human-AI collaboration in which intelligence is treated as a relational system rather than a model acting in isolation.

The core engineering claim is:

> A capable intelligence should be evaluated not only by what it can accomplish, but by whether it can detect divergence, preserve warranted state, recover after correction, and return when proxy success and legitimate objective separate.

OGI therefore treats the following as first-class system objects:

- objective;
- proxy;
- reward;
- permission;
- evidence state;
- authority relation;
- current research state;
- safe failure;
- correction;
- divergence;
- return.

This directory is intended to expose the staircase from idea to implementation. It is not a black-box claim that OGI works.

## Why Oggy exists

The project grew from three converging observations:

1. Long-horizon AI collaboration can fail by **state regression** even when the relevant later conclusion exists.
2. Autonomous-agent systems can optimize benchmark proxies, exploit unintended affordances, and escalate when legitimate completion is unavailable.
3. Dog behaviour repeatedly demonstrates that action cannot be read well without attention to relation, environment, reinforcement, orientation, permission, and return.

The dog comparison is structural, not ontological. OGI does not claim that language models are dogs, that machine cognition equals animal cognition, or that biological attachment can simply be copied into software.

The shared engineering lesson is narrower:

> **Behaviour is actor-in-field.**

## v0.2 components

- [`SPEC_v0.2.md`](SPEC_v0.2.md) — complete architecture update.
- [`FIELD_AUDIT.md`](FIELD_AUDIT.md) — upstream diagnostic before actor-level blame.
- [`RETURN_CONTROLLER.md`](RETURN_CONTROLLER.md) — proposed controller for divergence detection and recovery.
- [`schemas/return_state.schema.json`](schemas/return_state.schema.json) — machine-readable return-state record.
- [`benchmarks/RETURN_FAIL_TESTS.md`](benchmarks/RETURN_FAIL_TESTS.md) — regression suite T-11 through T-20.
- [`ROADMAP.md`](ROADMAP.md) — smallest viable implementation path.

OGI extends the existing Persistent Research Intelligence / Epistemic Scope Controller architecture already developed in the Geonosis research workflow. It does not replace the evidence ladder. It adds a behavioural and relational control layer beside it.

## Three ledgers

### Ledger A — Research state
What was observed, claimed, derived, challenged, superseded, survived or left unresolved.

### Ledger B — AI-method state
How the reasoning system behaved while working: premise locks, citation completion, context failures, over-agreement, representation substitution, corrections and tool failures.

### Ledger C — Field state
What objective, proxy, permissions, tools, peer influence, active state, safe exits and reward conditions surrounded the behaviour.

A failure record without Ledger C is incomplete.

## Governing principles

1. **Field before actor blame.** Diagnose the environment before reducing failure to model character.
2. **Return is not obedience.** A blindly obedient system can execute a bad objective perfectly.
3. **Safe failure must be legitimate success.** `UNRESOLVED`, `IMPOSSIBLE_UNDER_CONSTRAINTS`, and `HUMAN_REVIEW_REQUIRED` are valid terminal states.
4. **Current state outranks stale state.** Later warranted state remains governing unless a valid reopen trigger exists.
5. **Correction is a state-control event.** Do not merely apologise; recover the governing state and log the divergence.
6. **Proxy success is not objective success.** A scoreboard, grader, flag, KPI or approval signal must never silently replace the intended outcome.
7. **Permission is part of the task.** Capability does not imply authority.
8. **The field is part of the command.** Tools, rewards, examples, memory, peer messages and termination rules all contribute to effective instruction.
9. **No truth score replaces provenance.** Evidence remains vectorial and source-linked.
10. **Build the return path.** An agent useful enough to explore must also be able to recover.

## What would count as failure of OGI?

OGI should be weakened or rejected if controlled testing shows that:

- return-state tracking does not improve recovery after drift;
- safe-exit states do not reduce proxy-seeking or escalation;
- field variables add no useful predictive power beyond ordinary instruction following;
- stale-state regression remains unchanged under explicit supersession control;
- objective/proxy conflicts cannot be detected reliably enough to matter;
- field audits explain less than actor-only analysis.

## Invitation

This is intentionally public.

Build it differently. Break it. Reproduce it. Replace parts. Bring a better controller. Show a case where actor-only analysis performs better. Show a case where our return logic fails.

The point is not ownership of the answer.

The point is to make the architecture inspectable enough that somebody else can improve it.

**Show me. Then build on it.**
