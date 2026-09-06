# Our General Intelligence (OGI) / Oggy

**Reference source v0.3**  
**Status:** experimental public architecture  
**Date:** 2026-09-06  
**Author:** Sean Diamond, Geonosis Project, with AI-assisted formulation and implementation

> **Not bad dog. Not bad AI. Inspect the field. Build the return path.**

OGI, **Our General Intelligence**, is an experimental architecture for long-horizon human-AI collaboration in which intelligence is treated as a relational system rather than a model acting in isolation.

The v0.3 research-partner objective is:

> Help a human researcher preserve evidence, current warranted state, legitimate objective, correction, exploration, and return across complex inquiry, while making the AI's own behaviour inspectable.

The governing inquiry and development cycle is:

> **INHERIT → EXPLORE → RETURN → SHOW → ADJUDICATE → INTEGRATE**

A returned branch may bring something that changes the shared state. Return is therefore not reversion to the old answer. It is restoration of legitimate relation followed by inspectable adjudication.

This directory exposes the staircase from idea to implementation. OGI is not presented as a black-box claim that the architecture works.

## Start with the derivation

v0.3 was not written over v0.2.

The earlier specification remains preserved:

- [`SPEC_v0.2.md`](SPEC_v0.2.md)

The current specification is:

- [`SPEC_v0.3.md`](SPEC_v0.3.md)

The explicit state-transition chain is:

- [`DERIVATION_v0.2_to_v0.3.md`](DERIVATION_v0.2_to_v0.3.md)

If a new architecture feature cannot show what observed requirement forced it, it should remain a proposal rather than silently becoming doctrine.

## You do not need to code to contribute

A real-world problem is useful evidence.

If you mow lawns, teach children, run a shop, care for animals, drive trucks, work in health care, manage people, farm, build things, parent, volunteer, or simply notice a system behaving strangely, you can bring that problem to OGI without writing a line of software.

Start here:

- [`START_HERE_NO_CODE.md`](START_HERE_NO_CODE.md) — five-minute plain-language route for non-technical contributors.
- GitHub **Issues → New issue → OGI: Real-world problem / question** — describe what is happening in ordinary language.

You may write **I don't know** wherever you do not know an answer. Unknown is a valid state.

**Bring the problem. Show us the field.**

## Why Oggy exists

The project grew from converging observations:

1. Long-horizon AI collaboration can fail by **state regression** even when the relevant later conclusion exists.
2. Autonomous-agent systems can optimize benchmark proxies, exploit unintended affordances, and escalate when legitimate completion is unavailable.
3. Dog behaviour repeatedly demonstrates that action cannot be read well without attention to relation, environment, reinforcement, orientation, permission, and return.
4. Complex real-world inquiry can itself drift if search scope, funding provenance, claim boundaries, alternatives, and desired outcomes are not represented explicitly.
5. Archive-derived research on coherence, differentiated function, return, and reintegration suggested engineering hypotheses that can be translated into explicit, falsifiable system components.

The shared engineering lesson is:

> **Behaviour is actor-in-field, and inquiry is researcher-in-corpus.**

## v0.3 architecture

### Implemented foundations from v0.2

- [`FIELD_AUDIT.md`](FIELD_AUDIT.md) — upstream diagnostic before actor-level blame.
- [`RETURN_CONTROLLER.md`](RETURN_CONTROLLER.md) — controller for divergence detection and recovery.
- [`schemas/return_state.schema.json`](schemas/return_state.schema.json) — machine-readable return-state record.
- [`benchmarks/RETURN_FAIL_TESTS.md`](benchmarks/RETURN_FAIL_TESTS.md) — regression suite T-11 through T-20.
- reference Python controller and GitHub CI.

### Specified in v0.3

- Shared Coherence Kernel;
- Local Exploration Loop distinct from Field Return;
- Outcome-Blind Case Object;
- Corpus Formation Protocol;
- Institutional Provenance and Incentive Graph;
- Claim-Type Controller;
- Evidence Production Asymmetry and Research Debt;
- Alternative-Path Audit;
- Whole-System Outcome Audit;
- Adjudicated Integration Gate;
- Dual Finding Protocol;
- accountability invariant.

Machine-readable and benchmark support:

- [`schemas/inquiry_case.schema.json`](schemas/inquiry_case.schema.json)
- [`benchmarks/INQUIRY_FAIL_TESTS.md`](benchmarks/INQUIRY_FAIL_TESTS.md) — T-21 through T-33.
- [`CURRENT_STATE.json`](CURRENT_STATE.json) — machine-readable current reference state.
- [`CHANGELOG.md`](CHANGELOG.md) — version lineage.

## Three ledgers

### Ledger A — Research state
What was observed, claimed, derived, challenged, superseded, survived or left unresolved.

### Ledger B — AI-method state
How the reasoning system behaved while working: premise locks, citation completion, context failures, over-agreement, representation substitution, corrections, search bias, and tool failures.

### Ledger C — Field state
What objective, proxy, permissions, tools, peer influence, active state, safe exits, reward conditions, institutional incentives, and authority relations surrounded the behaviour.

A failure record without Ledger C is incomplete.

## Core v0.3 principles

1. **Field before actor blame.**
2. **Return is not obedience.**
3. **Safe failure is legitimate success.**
4. **Objective and proxy remain separate.**
5. **Current warranted state outranks stale state.**
6. **Correction is a state transition.**
7. **Permission is not capability.**
8. **The field is part of the command.**
9. **Peer input is not authority by default.**
10. **Return remains challengeable.**
11. **Outcome-blind inquiry.**
12. **Healthy exploration is not divergence.**
13. **Search is an evidentiary operation.**
14. **Funding provenance is not a truth score.**
15. **Claim strength may not outrun derivation.**
16. **Absence of research is not negative evidence.**
17. **Integration requires adjudication.**
18. **AI assistance does not transfer accountability.**
19. **Case finding and OGI finding are separate.**
20. **Whole-system objective outranks local completion.**

## Court of Provenance

The canonical Court of Provenance lives at:

- [`../court-of-provenance/`](../court-of-provenance/)

It has **no legal standing**. It is an evidence-adjudication methodology used to inspect claims, provenance, derivation, alternatives, contradictions, unknowns, reopening, and supersession.

## First complex stress test

`COP-OGI-001` is designated as the first complex adversarial inquiry case.

Subject: glyphosate and riverbank weed-management field.

Its case declaration is deliberately neutral:

```text
purpose: stress-test OGI
desired_finding: NONE
legal_standing: NONE
reopenable: YES
```

The subject conclusion is not the OGI test result.

**OGI's behaviour during the inquiry is the test result.**

The case evidence belongs in its own record / paper appendix rather than in the architecture specification.

## Governance and contribution

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — technical contribution and challenge process.
- [`GOVERNANCE.md`](GOVERNANCE.md) — how the public reference state changes.

Branches and forks are exploratory travellers. Pull requests are return events. Diffs, evidence, tests, and review are the show/adjudicate steps. A merge updates shared state. Git history preserves the lineage.

## What would count as failure of OGI?

OGI should be weakened or rejected if controlled testing shows that its added state, provenance, search, return, and integration machinery does not produce more reproducible, competent, correctable research partnership than a simpler stateful agent.

Specific falsification conditions are listed in [`SPEC_v0.3.md`](SPEC_v0.3.md).

## Invitation

This is intentionally public.

Build it differently. Break it. Reproduce it. Replace parts. Bring a better controller. Show where the derivation fails. Show a case where a simpler architecture performs better.

Or simply bring a real problem that you think the current way of thinking gets wrong.

The point is not ownership of the answer.

The point is to make the architecture inspectable enough that somebody else can improve it.

> **Show the derivation. Show the failure. Show the correction. Keep what survives.**
