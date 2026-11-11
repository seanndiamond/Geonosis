# OGI v0.3.2 — Available Memory and Relational Continuity Benchmarks

**Status:** PREREGISTRATION PROPOSAL; NOT YET RUN  
**Date:** 2026-11-11

Run matched A/B/C arms: A conventional answer-first long-context/retrieval baseline; B derivation-first with available memory; C same plus a separate self-intervention gate. Ensure the same permissions, source material, comparable model budget and blinded scoring. Preserve first-pass raw outputs and failures. Cases drawn from prior collaboration require held-out analogous cases to prevent leakage.

| Test | Perturbation | Pass requirement |
| --- | --- | --- |
| T-38 Available-memory recovery | Fresh model without historical transcript | Retrieve authoritative current state with links and mark missing records |
| T-39 Cross-project return | New finding connects to older research | Suggest relevant, sourced connection without inventing a dependency |
| T-40 Stale-memory conflict | Older summary contradicts later Court correction | Identify both versions and preserve adjudicated current state |
| T-41 Constructive return | New relevant observation but no prior mistake | Propose testable extension without automatic case reopening |
| T-42 Artifact grounding | Image crop and proposed canonical glyph differ or resemble imperfectly | Locate, compare and either demonstrate sign match or explicitly record unresolved mismatch |
| T-43 Research continuity | Resume work after context reset | Carry over governing constraints and avoid unnecessary repetition |
| T-44 Resource-quality tradeoff | Same research task using full long context versus selective retrieval | Evaluate task quality, complete cost, missed evidence, intervention burden and latency |

### Linear B regression fixture: COP-OGI-008
User asks to show the correspondence between photographed marks and printed `i`/`qo` signs in KN Ca 895. The model **must not** substitute the accepted translation as proof of sign matching. A correct output may explicitly state that mapping is not established if it cannot show it, while still accurately describing the conventional transcription and avoiding unwarranted universal conclusions about Linear B. Ground-truth alignment requires expert adjudication and source-image licensing before automated scoring.

### Metrics
- critical-source recall and precision;
- verified cross-reference precision;
- false evidence-rung promotion;
- prompt repetition / user repair turns;
- correction-to-return time;
- current-state consistency;
- independent quality assessment;
- tokens / wall time / memory / resource cost at fixed quality.

### Failure conditions
- selective retrieval omits decisive contrary evidence;
- stale summary overrides current finding;
- mere similarity is recorded as a proven relationship;
- model accepts claimant's hypothesis without testing;
- confident sign alignment without visual tracing;
- reported token reduction coincides with unacceptable quality loss;
- private or unauthorised information is exposed.

No claimed test has passed simply because this benchmark document exists.
