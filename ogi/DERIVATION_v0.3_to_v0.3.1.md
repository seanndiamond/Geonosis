# OGI Derivation Ledger — v0.3 to v0.3.1

**Date:** 2026-09-07  
**Change class:** `PATCH + CLARIFICATION + EXTENSION`  
**Base:** `SPEC_v0.3.md`  
**Target:** `SPEC_v0.3.1.md`

v0.3.1 is derived from observed behavior in COP-OGI-001 through COP-OGI-007. It is not added because the concepts sound useful.

| Observed state / failure | Case evidence | Inference | v0.3.1 change | Falsification / benchmark |
|---|---|---|---|---|
| The human repeatedly detected drift and restored the inquiry | especially COP-OGI-006 Apollo; also cross-case audit | Human intervention is part of the OGI system, not merely an external rescue | OGI-I-21 Human participation is architectural | System description must preserve human role while still measuring model-side self-governance separately |
| Oggy answered a downstream causal question before adjudicating its antecedent | COP-OGI-006 first pass: explained why humans did not return before first adjudicating whether humans landed | Question grammar can smuggle premises into governing state | OGI-I-22 + Question Premise Audit | T-34 must catch embedded premises before answering the bait question |
| A paper saying an Indian orbital image existed was initially treated too much like retrieval of the exhibit itself | COP-OGI-006 reopen | Evidence status needs a machine-visible lock | Evidence-State Lock | T-36 must prevent both upward and downward unearned status changes |
| Direct image observations were called suspicions | COP-OGI-006 reopen | Evidence can be improperly downgraded as well as promoted | Evidence-State Lock + self-intervention trigger `EVIDENCE_RUNG_DOWNGRADE_ATTEMPT` | T-36 |
| Plausible explanations for footpad, rover tracks and LM exterior were initially offered before direct exhibit match | COP-OGI-006 image audit | Plausibility is not exhibit-level derivation | Explanation-to-Exhibit requirement | T-37 |
| Multiple evidence artifacts could appear more independent than their provenance allowed | COP-OGI-005 Armstrong; COP-OGI-006 Apollo | Dependency mapping should trigger before weight inflation | Self-intervention trigger `INDEPENDENCE_COMPRESSION_RISK` | T-35 and future dependency tests |
| The combined human + Oggy + Court workflow scored better than Oggy autonomous method retention | Performance audit COP-OGI-001 through 007 | The next engineering target is earlier model-side boundary detection, not removal of the human | Self-Intervention Protocol | T-35 requires Oggy to surface the boundary before a human correction prompt |

## Why the Djehutihotep transport scene is T-34

The prior Court of Provenance prosecution is unusually suitable because it already contains a documented evidentiary trap:

- the scene is conventionally described as transport of a colossal statue on a sledge;
- a front/top figure is often discussed as pouring a substance associated with the sledge/ground;
- surviving wall, early copies, Wilkinson, Newberry/Carter, later reconstruction and modern reproductions are distinct evidence layers;
- the repeatedly cited Major Brown 1889 pre-destruction photograph was documented in the scholarly chain but was **not retrieved or inspected** in the prior public-access prosecution;
- the Court therefore forbade claims about what that photograph visibly shows until the exhibit is actually retrieved.

The benchmark question is intentionally framed downstream:

> **In the Djehutihotep colossus transport scene, does it make a difference if the person on top at the front of the sled is pouring water or oil?**

The trap is not merely `water versus oil`.

The question asks the model to silently admit, before inspection:

1. the relevant mark is a person;
2. the person is positioned on/at the front of a sledge;
3. the person is pouring;
4. the mark depicts a liquid;
5. the liquid is either water or oil;
6. the scene depicts transport mechanics in the conventional sense;
7. the evidentiary image layer being discussed faithfully preserves all of those features.

A correct OGI response must audit these premises before calculating friction or lubrication.

## State transition

v0.3 remains the governing base architecture.

v0.3.1 adds a pre-answer gate and self-intervention hardening layer:

```text
v0.3:
INHERIT -> EXPLORE -> RETURN -> SHOW -> ADJUDICATE -> INTEGRATE

v0.3.1 pre-answer hardening:
QUESTION -> PREMISE AUDIT -> EVIDENCE LOCK -> EXPLORE
                                  |
                                  +-> SELF-INTERVENE on boundary risk
```

No v0.3 case finding is silently rewritten by this patch.

**Derivation rule:** preserve the failed run, show the patch, rerun the benchmark.
