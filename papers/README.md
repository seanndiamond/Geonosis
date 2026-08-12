# Public Paper Mirror

This directory is for full-text or archival mirrors of public Geonosis research outputs.

The goal is to make papers searchable, diffable and citable in GitHub while preserving the publication version and its provenance.

## Admission rule

A paper enters the full-text mirror when all of the following are known:

1. **Public status** — the work is demonstrably public, for example on ResearchGate or another public repository.
2. **Version identity** — the version being mirrored is identified by title, date and version where available.
3. **Rights status** — the author has the right to mirror the text, and third-party images/tables are handled according to their own rights.
4. **Source provenance** — the mirror identifies the source file or public publication record from which it was derived.
5. **No silent rewriting** — conversion to Markdown may repair layout artefacts but does not quietly revise substantive claims.

## Preferred package per paper

```text
papers/<slug>/
  README.md             # title, citation, public status, rights, source and evidence-room note
  manuscript.md         # searchable text where rights permit
  figures/              # only rights-cleared or original figures
  provenance.json       # source/version/checksum information
  evidence/             # claim records or figure ledgers when available
```

Original PDF/DOCX versions may also be mirrored where useful and rights-clear, but a binary file alone is not considered a reproducible research package.

## ResearchGate is a publication source, not a derivation substitute

The ResearchGate record establishes that a work was publicly posted. It does not by itself validate the paper's claims. Claim-level evidence lives in the source and evidence records.

## Current migration state

The repository currently contains the five-paper public research spine as navigational records. Full-text migration is being done from verified public versions rather than assuming every manuscript in the private project archive is identical to the ResearchGate version.

The historical ResearchGate list is preserved in `../publications/`, and evidence architecture is already available under `../method/`, `../schema/`, `../cases/` and `../provenance/`.

## Version correction

If a mirrored paper is later corrected:

- preserve the old version or its commit history;
- record the change;
- identify whether the correction affects wording, source provenance, data, interpretation or conclusion;
- link any affected evidence records.

Git history is useful here precisely because research has a history too.
