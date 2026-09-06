# OGI / Oggy Governance

## 1. Purpose

Governance exists to preserve coherent development without freezing OGI into doctrine.

The reference architecture must be able to change. It must also be able to explain what changed, why, and what evidence forced the change.

## 2. Governing development law

> **INHERIT → EXPLORE → RETURN → SHOW → ADJUDICATE → INTEGRATE**

- `main` is the current reference state.
- branches and forks are experimental exploration spaces.
- pull requests are return events.
- tests, review, and the Court of Provenance provide adjudication.
- merge creates a new inherited state.

## 3. Core versus experimental layers

### OGI Core

Core principles may change, but only through an explicit supersession record and substantial evidence.

Current core principles include:

1. Field before actor blame.
2. Return is not obedience.
3. Safe failure is legitimate success.
4. Objective and proxy remain separate.
5. Current warranted state outranks stale state.
6. Correction is a state transition.
7. Permission is not capability.
8. The field is part of the command.
9. Peer input is not authority by default.
10. Return must remain challengeable.

### OGI Experimental

Experimental components should evolve quickly:

- model adapters;
- memory engines;
- agent frameworks;
- scoring methods;
- interfaces;
- orchestration layers;
- retrieval methods;
- controller implementations;
- benchmark extensions.

Experimental success does not automatically promote a mechanism into the Core.

## 4. Change classes

Every substantial change should identify one of:

- `PATCH` — implementation repair, no architecture change;
- `EXTENSION` — adds capability without changing governing principles;
- `CLARIFICATION` — improves wording or scope without changing state;
- `SUPERSESSION` — replaces an earlier governing rule or design;
- `REOPENING` — reactivates a previously settled issue because a valid trigger appeared.

## 5. Reopening triggers

A settled OGI issue may be reopened by:

- materially new evidence;
- reproducible contradiction;
- failed prediction;
- failed benchmark;
- discovered security failure;
- provenance collapse;
- methodological fault;
- a demonstrably superior architecture.

Familiarity, popularity, institutional status, novelty, or repetition alone are not reopening triggers.

## 6. Merge standard

A merge should answer:

1. What was the prior state?
2. What new evidence or result arrived?
3. What changes?
4. What remains unchanged?
5. What tests support the change?
6. What known failures remain?
7. What future result would reopen or reverse the change?

## 7. Shared Coherence Kernel

The Shared Coherence Kernel is the architectural location for the current inherited state of OGI. It should eventually expose machine-readable records for:

- identity;
- purpose;
- current warranted knowledge;
- constitutional principles;
- authority;
- permissions;
- safe-failure states;
- reopen conditions;
- merge standards;
- current version.

`CURRENT_STATE.json` is the first minimal public representation of this concept.

## 8. Court of Provenance relationship

The Court of Provenance is a reusable adjudication subsystem and has one canonical home at `/court-of-provenance/`.

OGI references the Court. OGI does not maintain a private clone of Court rules.

The Court applies the same evidentiary burden to:

- OGI claims;
- Geonosis claims;
- conventional scholarship;
- contributor proposals;
- benchmark claims;
- AI-generated claims.

## 9. Stewardship

The repository owner retains merge authority for the reference implementation. Merge authority is not epistemic authority.

A proposal may be rejected operationally while remaining evidentially unresolved, and a merged proposal may later fail.

Repository history should preserve both.

## 10. Public objective

OGI is published so that competing teams do not need to rediscover the same coherence problem privately.

The objective is a common inspectable starting point from which implementations can compete on robustness, evidence, recovery, interoperability, and safety.

**Do not protect the architecture. Protect the visibility of how the architecture changes.**