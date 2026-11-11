# OGI Available Memory and Relational Continuity

**Experimental design note — 2026-11-11**

## Thesis
Continuity is the ability to bring relevant prior work into a present inquiry with provenance, not the need to keep an entire history continuously in context.

## State distinctions
`STORED`: bytes or record retained.  
`DISCOVERABLE`: searchable index or locator exists.  
`AVAILABLE`: authorised retrieval path exists.  
`RETRIEVED`: source content obtained in this run.  
`INSPECTED`: relevant content or image directly examined.  
`MAPPED`: connection to current question shown.  
`ADJUDICATED`: claims assessed by Court procedure.  
`ACTIVE`: scoped context currently supplied to reasoning.

These states are dimensions, not a simplistic linear rank. For example, an ACTIVE summary may cite a source not yet RETRIEVED in this run. Do not promote such a source to INSPECTED.

## Data handling
Keep source locators, versions, permissions, timestamps, citation ranges and dependencies. Segregate user-supplied observations from derived interpretations; never store private content in a public repository without permission. The present GitHub documents contain architecture descriptions, not a dump of conversations or private data.

## Recall sequence
1. Resolve objective and source access.
2. Discover governing current state and related work.
3. Fetch exact records required to resolve dependencies.
4. Check supersession, contradiction and content integrity.
5. Build a small, explainable working context with source pointers.
6. Ask the Court or authorised human to adjudicate substantive changes.
7. Log successful retrievals, misses, corrections and cost.

## Return categories
`CORRECTIVE_RETURN`: recovery from an error, stale state or false inference.  
`CONSTRUCTIVE_RETURN`: new cross-project insight offering a testable extension.  
`REFERENCE_RETURN`: needed context recovered without changing a finding.  
`NO_RETURN`: relevance or authority insufficient; record why.

## Efficiency evaluation
Measure total tokens in/out; retrieved bytes; query counts; latency; peak process memory where observable; model KV-cache demand where measurable; total task energy where instrumented; human repair time; factual errors; missing critical dependencies; successful continuation. Never claim energy savings from token counts alone.

## Human agency
Human participants may challenge a retrieval, correct a link, reject incorporation, and request source inspection. An apparently convenient recovered summary never overrules observed source data.

## Boundaries
Availability is not perfect recall; semantic similarity is not provenance; an untested continuity module is not a demonstrated general intelligence.
