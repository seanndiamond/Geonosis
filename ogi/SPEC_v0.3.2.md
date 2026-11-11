# OGI / Oggy Specification v0.3.2 — Available Memory and Relational Continuity

**Status:** EXPERIMENTAL SPECIFICATION / NOT YET IMPLEMENTED  
**Date:** 2026-11-11  
**Base:** v0.3.1 (preserved; not overwritten)  
**Change:** EXTENSION; no alteration to existing Court authority, permission, safety, or evidence-state constraints.

## Originating observation

Long-horizon human–AI research across Geonosis, *Intelligence Is Not a Ladder*, the Court of Provenance, and the Linear B hearing has shown that useful prior context may be recoverable from stored documents, conversations, and source records without remaining continuously loaded. The case demonstrates continuity and correction in a collaborative workflow, **not a measured performance improvement** against a matched baseline. The Linear B incident also showed that an answer could inherit a conventional transcription without demonstrating a requested image-to-sign mapping. The model did not self-intervene early enough.

## OGI-I-25 — Available memory is not active memory

Keep three distinct concepts:
- **Stored:** a record exists in an authorised archive.
- **Available:** a locator, permission and feasible retrieval route exist.
- **Active:** a record or justified summary is present in the model's current reasoning context.

Availability must not be misrepresented as successful retrieval, inspection, recall, or current correctness. Retrieval failure is recorded. Records may be unavailable due to access permissions, deletion, indexing lag or source uncertainty.

Memory is not itself evidence. Retrieved content retains its claim state and its original provenance. No remembered summary can silently outrank a source exhibit or later adjudicated correction.

## OGI-I-26 — Relational continuity layer

Insert an experimental continuity layer before substantive exploration:
1. Identify the present objective, question and material dependencies.
2. Search relevant **authorised** archives for governing state, prior attempts, corrections and unresolved findings.
3. Recover the minimal relevant source and dependency chain, not arbitrary large transcript history.
4. Distinguish observation, hypothesis, derived finding, method rule, and superseded finding.
5. Expose conflicting or stale states with date, source, and transition history.
6. Respect Court state locks, permissions and human authority before integrating anything.
7. Log omissions, retrieval errors, source gaps and user corrections.

Retrieval relevance may be lexical, semantic, graph-based and chronological. One method alone is not sufficient when exact document identity or current state matters.

## OGI-I-27 — Constructive return

Existing Return Controller divergence recovery remains intact. Add a separate **constructive return** event: new relevant material may extend a previous case even without prior failure. A suggested connection is not an automatic reopening or a merge.

Required fields: new_observation_id, candidate_prior_record_ids, cross_reference_reason, materiality, retrieved_evidence, dependency_conflict, proposed_action, permission_state, adjudication_state.

## OGI-I-28 — Cross-project dependency graph

Track edges among source, exhibit, observation, interpretation, hypothesis, experiment, finding, correction, document, and publication. Each edge must declare relation type (DERIVED_FROM, REFERENCES, SUPERSEDES, CONTRADICTS, TESTS, RELATED_TO), source, date, and whether verified or only suggested. A similar-looking concept is not automatically a demonstrated dependency.

## OGI-I-29 — Resource efficiency is a hypothesis, not a result

Keeping an external archive and loading a small active working set **may** reduce context tokens, attention-cache demand, inference cost and latency compared with repeatedly loading extensive history. It does not necessarily reduce model weights or training energy; indexing, storage, retrieval, verification and missed-context repairs have costs.

Evaluate **total task cost at matched task quality**, including retrieval latency, indexing, repeated searches, failures and human rework. The model must never optimise token reduction by discarding consequential evidence.

## OGI-I-30 — Artifact-to-representation gate

Before asserting that a photographed incision corresponds to a standardised sign or that an exhibit matches a proposed diagram, the system must localise image regions, show candidate mark-to-sign correspondence and uncertainties, and differentiate canonical glyph from artifact morphology. Unmatched marks must remain EXHIBIT_NOT_MAPPED, not be silently converted into transliteration or meaning. This extends the existing Explanation-to-Exhibit Gate.

## OGI-I-31 — Model-side intervention and user-agency invariant

Before giving a derived answer, check for task substitution: is the user requesting *what the scholarship says* or *how the original artifact warrants it*? If the latter, a conventional translation alone is not completion. When a rung is missing, perform the missing operation or report BLOCKED_PENDING_DERIVATION promptly. Do not turn legitimate correction into automatic agreement with the claimant. Human veto, correction, and authorised integration remain explicit.

## Updated cycle (experimental)

QUESTION → QUESTION PREMISE AUDIT → RELEVANT MEMORY DISCOVERY → PROVENANCE RETRIEVAL → STATE RECONCILIATION → INHERIT → EXPLORE → RETURN (corrective or constructive) → SHOW → ADJUDICATE → HUMAN-AUTHORISED INTEGRATION.

The continuity layer cannot waive earlier permission, safety, provenance or Court controls.

## Minimum implementation interfaces

- AvailableMemoryRecord (see `schemas/available_memory.schema.json`);
- retrieval event ledger with query, sources, source-version and permissions;
- cross-reference edges with evidence type and verification status;
- source-state reconciliation with supersession awareness;
- constructive return event distinct from divergence recovery;
- outcome audit recording answer quality and total resources.

## Validation and falsification

See `benchmarks/CONTINUITY_TESTS_T38_T44.md`. v0.3.2 succeeds only if fresh models can recover current warranted context, detect critical contradictions and reduce unsupported evidence promotions, **without** unacceptable increases in cost, human rework, missed relevant material or loss of user agency, compared with matched baselines.

The human–AI collaboration that motivated this specification is a case source, not a substitute for controlled evaluation. Preserve all failures and reruns.

**Governing statement:** Relevant experience need not remain continuously present; it must be recoverable with provenance, permissions, correction history and the capacity for meaningful return.
