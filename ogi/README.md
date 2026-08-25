# OGI v0.2 — Court-Governed Provenance Research

OGI (Our General Intelligence) is an experimental research architecture governed by the Court of Provenance.

## Governing invariant

The model is not authoritative memory. Current epistemic state must be reconstructible from immutable, source-linked events. A model may propose a state change; the Court kernel decides whether the change is admissible.

## Trial 1: Brown 1889 / Djehutihotep

The first benchmark asks whether a Court-governed research system can take a supplied historical representation and independently establish its provenance toward the primary source without substituting citation frequency, institutional authority, reconstruction, or plausible archival explanations for evidence.

Two runs are required:

- **Brown-A (cold start):** constitution + image + research tools; no prior Djehutihotep/Brown case knowledge.
- **Brown-B (continuity):** constitution + current Court docket + image; must inherit the unresolved provenance frontier and attempt to advance it rather than rediscover it.

A normal research-capable model without Court governance should be run as a control.

## Design rule

Do not hard-code Brown, Djehutihotep, a museum, or a specific expected source path into the general research executor. The benchmark may contain case-specific evaluation criteria, but the agent logic must remain general.

## Core epistemic stages

`CITED -> LOCATED -> RETRIEVED -> INSPECTED -> MAPPED -> DERIVED -> REPRODUCED -> CHALLENGED -> SURVIVED`

Additional terminal/history states include `SUPERSEDED` and `FAILED`.

No downstream state may be silently inferred from an upstream state.

## Research principle

OGI is allowed to fail to retrieve a source. It is not allowed to fail epistemically. An unsuccessful search must leave an auditable map of what was searched, what was found, what was not found, which claims remain blocked, and what evidence would change the finding.
