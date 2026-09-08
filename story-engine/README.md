# Geonosis Research-Narrative Continuity Engine

## Purpose

This directory is the persistent source of truth for long-form Geonosis narrative projects, beginning with the Trojan Horse trilogy.

The engine exists to prevent conversational drift, continuity loss, accidental retconning, premature revelation, unsupported narrative invention, and the separation of story from the research architecture that gives the story its meaning.

## Authority rule

`trojan-horse-ledger.json` is the canonical machine-readable continuity state for the Trojan Horse trilogy.

Chat memory, conversation summaries, manuscript fragments, and AI recollection are secondary. If they conflict with the ledger, the conflict must be surfaced and resolved. An AI must not silently choose one version.

The ledger may be changed only when:

1. Sean Diamond explicitly revises canon;
2. a new completed chapter establishes new canon;
3. new Geonosis research changes the evidentiary or philosophical architecture;
4. an identified contradiction is deliberately resolved.

Every substantive change should be committed to GitHub so the project has a recoverable history.

## Required workflow for every chapter

Before drafting a chapter, the AI should load the current ledger and establish:

- current book and chapter position;
- character locations and knowledge states;
- active research findings relevant to the scene;
- revelations already made to the reader;
- revelations that remain sealed;
- open threads requiring preservation or payoff;
- the incoming emotional and physical state from the previous chapter;
- voice and style constraints;
- any immutable canon that the proposed chapter could affect.

After drafting and approving a chapter, update the ledger with:

- events that became canon;
- character state changes;
- new knowledge gained by each character;
- reader revelations;
- new or resolved open threads;
- timeline changes;
- artefact state changes;
- new foreshadowing;
- the exact exit state that the next chapter inherits.

## Epistemic rule

Narrative invention must never silently become research evidence.

For important propositions, preserve this chain:

**SOURCE -> OBSERVATION -> INFERENCE -> PROJECT FINDING -> NARRATIVE USE**

The story may dramatise a research finding, but the drama does not upgrade the evidentiary status of that finding.

## Continuity rule

Continuity includes more than names, dates, locations, and character traits. It also includes causal continuity and epistemic continuity.

A chapter is invalid if it is narratively elegant but requires a character to know something they have not learned, reveals material reserved for a later book, contradicts established project findings, changes the causal architecture without explicit revision, or treats a speculative narrative bridge as established research.

## Versioning

The ledger uses semantic versioning.

- PATCH: wording, metadata, typo, or non-substantive clarification.
- MINOR: new chapter canon, new open threads, character-state changes, or new research entries that do not overturn existing canon.
- MAJOR: deliberate change to the trilogy architecture, immutable canon, or a major research finding that forces reinterpretation of existing story material.

GitHub commit history is the audit trail.

## AI handoff instruction

At the start of a new conversation, the preferred instruction is:

> Load `story-engine/trojan-horse-ledger.json` from the Geonosis GitHub repository as binding continuity for the Trojan Horse trilogy. Do not rely on chat memory where the ledger supplies an answer. Surface conflicts rather than silently reconciling them.

This makes continuity portable across ChatGPT conversations and, where the repository is accessible, across different AI systems.
