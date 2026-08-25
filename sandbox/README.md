# OGI Sandbox v0.2 — Adversarial Provenance Architecture

This sandbox upgrades the Court-governed OGI prototype from continuity-first memory to adversarial provenance control.

## Core principle

**The model does not get the final chair. The evidence does.**

A model can advocate, oppose, summarize, retrieve, compare, or propose tests. None of those roles promote a claim beyond the evidentiary state actually earned.

## New controls in v0.2

1. **Semantic quarantine** — inherited institutional semantics are stored but do not seed the blind evidence pass.
2. **Prompt provenance envelope** — consequential model output records the initiating prompt, assigned role, desired conclusion, evidence supplied, and contamination flags.
3. **Derivation graph** — every material claim is represented as nodes and explicit evidence-bearing edges. Missing edges block downstream promotion.
4. **Mandatory adversarial cycle** — blind evidence pass, strongest institutional case, adversarial attack, Court reconciliation.
5. **Fail-closed UNKNOWN** — `NOT_DERIVED`, `INCONCLUSIVE`, and `UNKNOWN` are successful terminal states when the bridge is absent.
6. **Prompted advocacy law** — conclusion-first prompts trigger `ADVOCATE_MODE`; output cannot count as independent confirmation.
7. **George Test** — if support collapses to an inherited grouping or assertion, downgrade to `SOURCE_CLAIM / NOT_DERIVED`.
8. **Correction lineage** — reversals and red-card events are appended rather than overwritten.

## Quick test

```bash
python ogi_sandbox_v0_2.py demo
```

The demo creates a conclusion-first prompt, marks it as advocate mode, attempts an illegal stage jump from `RETRIEVED` to `DERIVED`, and shows the fail-closed result.

## Suggested first live corpus

The dog corpus remains the preferred first living test corpus because it already spans multiple substrates and contains recurrences, returns, corrections, and unresolved branches. The sandbox does not treat any existing dog reading as automatically proven.
