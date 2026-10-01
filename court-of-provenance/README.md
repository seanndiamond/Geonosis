# Court of Provenance

**Status:** canonical public adjudication subsystem  
**Date:** 2026-09-06

The Court of Provenance is the reusable evidentiary and challenge engine used across Geonosis and OGI.

It exists to answer a simple question:

> **What has actually been shown, at what evidentiary depth, and what would change the current finding?**

The Court is not a truth machine and does not create authority by declaration. It is a run-sheet for keeping claims, evidence, derivation, contradiction, supersession, and reopening visible.

## One Court, many callers

The Court has one canonical home in this directory.

Systems that may call it include:

- OGI / Oggy;
- Geonosis research cases;
- archaeological and visual-archive prosecutions;
- AI architecture disputes;
- contributor challenges;
- replication disputes;
- provenance and transformation audits.

Projects should reference the Court rather than copying its rules into private local versions.

## Core burden

The same evidentiary burden applies to:

- conventional scholarship;
- unconventional scholarship;
- Geonosis;
- OGI;
- contributors;
- institutions;
- AI systems;
- the Court itself.

No claim receives automatic promotion because it is familiar, institutional, novel, unpopular, elegant, or confidently stated.

## Evidence staircase

The Court distinguishes at minimum:

`CITED != LOCATED != RETRIEVED != INSPECTED != MAPPED != DERIVED != REPRODUCED != CHALLENGED != SURVIVED`

A claim may not be stated at a deeper evidentiary level than the record supports.

## Court operating rules

1. **SHOW ME.** Consequential claims require an inspectable path back to source.
2. **NO INVISIBLE RUNG.** Do not upgrade citation, transcription, classification, or authority into derivation.
3. **OBSERVATION BEFORE INTERPRETATION.** Preserve what is visibly present separately from what it is proposed to mean.
4. **NO CONSENSUS SUBSTITUTE.** Agreement may be relevant history; it is not derivation by itself.
5. **SUPERSESSION, NOT ERASURE.** Earlier states remain recoverable.
6. **OBJECTIONS HAVE HISTORY.** A previously prosecuted challenge does not automatically reopen.
7. **REOPEN ON QUALIFYING TRIGGERS.** New evidence, contradiction, failed prediction, provenance collapse, or methodological fault may reopen a finding.
8. **UNKNOWN IS LEGITIMATE.** `UNKNOWN`, `UNRESOLVED`, and `BLOCKED_PENDING_DERIVATION` are valid findings.
9. **EQUAL BURDEN.** The Court applies the same standard inward as outward.
10. **NO INVENTED BRIDGE.** Missing evidence remains missing.


## Philosophical posture: come prepared

The Court is not a declaration of certainty and it is not a stage for institutional deference.

Its posture is adversarial in the constructive sense: **bring your strongest case**.

A claimant should expect the Court to ask for the source, the derivation, every visible rung in the staircase, the contradiction test, and the conditions under which the claim would fail. A challenger should expect exactly the same burden.

Confidence in a current finding does not imply certainty that no stronger staircase can exist. The Court therefore welcomes the opponent who has read the record carefully and arrives with something better.

The governing spirit is:

> **OSTENDE MIHI. NESCIS CUM QUO CONTENDAS.**

In Court terms:

> **Show me. Come prepared. Do not assume the other side has exhausted its case, and do not expect authority, familiarity, novelty, status, or ridicule to substitute for derivation.**

A worthy opponent is not a problem for the Court. A worthy opponent is what the Court is built for.

## Relationship to OGI

OGI uses the Court as its adjudication layer for branch-return integration, architecture challenges, benchmark disputes, and state supersession.

In OGI terms:

> **RETURN → SHOW → ADJUDICATE → INTEGRATE**

The Court owns **SHOW** and **ADJUDICATE**.

## Directory plan

This directory will hold the canonical public forms of:

- Court constitution and operating rules;
- scoring / evidence rubric;
- current-state record;
- case index;
- finding template;
- reopening template;
- provenance audit template;
- migrated historical rulings suitable for public release.

Private working files, unresolved-rights material, or incomplete exhibits are not automatically public merely because the Court is public.

## Public observation notes

- [CUN-OBS-2026-001 — Global-Field Morphology in Clay Tablets](observations/CUN-OBS-2026-001-global-field-clay-tablets.md) — records the open observation that irregular/rough tablet zones can retain structured morphology and should be tested before being discarded as damage; manufacturing mechanism remains unresolved.
- [VIS-OBS-2026-001 — Transformation Persistence in Pictographic Systems](observations/VIS-OBS-2026-001-transformation-persistence.md) — records the cross-corpus finding that examined pictographic systems remain semantically productive across multiple geometric transformations while retaining local-corpus coherence.
- [LINB-OBS-2026-001 — Linear B Preliminary Hearing](observations/LINB-OBS-2026-001-linear-b-preliminary-hearing.md) — opens the Linear B phonetic-provenance hearing, records the absence of a bedrock acoustic derivation to Court standard, and logs the emerging transformation-surviving guardian / dog reading.

## Current public state

See `CURRENT_STATE.json` and `CONSTITUTION.md`.

**The Court does not ask who said it. The Court asks: show the staircase.**