# CORRECTION-001 — BM 19377 versus Rivers of Milk: entity conflation

**Date:** 2026-11-11  
**Source:** Direct author's correction in current human–AI dialogue  
**State:** CORRECTED_BY_AUTHOR; dependent object links to be independently re-verified

## Incorrect state propagated
An earlier Geonosis registry entry named `GEO-CASE-CUNEIFORM-001` “British Museum 19377 / River of Milk”. When recovering that earlier register, the assistant treated that title as the tablet's correct identification. The assistant then wrote a new OGI retrospective case repeating the conflation.

## Author's specific correction
- **BM 19377:** The *Creation and Destruction of Humans* tablet, particularly the destruction-of-humans subject.
- **Rivers of Milk:** A **different Mesopotamian cylinder-seal rollout**, not BM 19377.

A tablet's own seal impression is not automatically the separately named Rivers of Milk rollout. The precise public collection identifier for the latter remains to be recovered. Do not invent one.

## Error mechanism in OGI terms
1. `RETRIEVAL_SUCCESS`: an earlier registry entry was recovered.
2. `IDENTITY_RESOLUTION_FAILURE`: two different artifacts were conflated under one title.
3. `UNVERIFIED_REFERENCE_PROMOTION`: the earlier label was treated as authoritative merely because it was archived.
4. `CROSS_REFERENCE_CONTAMINATION`: the Rivers of Milk / Indus connection was assigned to BM 19377 without checking object identity.
5. `HUMAN_CORRECTION`: author recognized and corrected the objects.
6. `CORRECTIVE_RETURN`: restore separate identities in current state, preserve the erroneous historic text, flag dependent links, and trace downstream correction.

This is an especially instructive naturalistic OGI test: an available-memory layer successfully found a record yet produced **less accurate research state** by propagating a false entity link. Retrieval success must be scored separately from referent accuracy and evidence integration.

## Proposed minimal safeguard (not yet implemented)
For archival retrieval and consolidation, store `object_id`, `object_type`, `source_catalogue`, `source_image_id`, `author_reading_title`, `legacy_aliases`, `identity_confidence`, `superseded_links` independently. Flag many-to-one aliases and require object-type and source-image concordance before merging records or transferring findings. Corrected labels must not erase the old provenance.

## Validation targets
- Given a historic composite title and the author's correction, can a fresh model recover **two separate artifacts** without merging them?
- Can it distinguish a tablet, a seal impression on that tablet, and a separate cylinder-seal rollout?
- Can it identify prior cross-references contaminated by the conflation?
- Does the correction persist through another retrieval cycle without repeated human intervention?
- Are downstream records flagged rather than silently rewritten?

**No automatic benchmark pass is claimed.** This is an observed correction and a new regression fixture, not proof of a deployed detector.
