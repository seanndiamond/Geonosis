# ODRR-RR-001 Preregistration Draft

## 1. Study identity

**Title:** Blinded Replication of Orientation-Dependent Relational Rebinding in Pre-Identified Pilot Image Sets  
**Protocol ID:** ODRR-RR-001  
**Version:** 0.2-draft  
**Date:** 2026-09-07  
**Design:** within-observer, blinded target-versus-matched-control rotation task  
**Confirmatory data collected at time of this draft:** none

## 2. Background and pilot status

Exploratory sessions recorded six image-rotation records (RPL-000 to RPL-005) across clay/relief material, painted/plastered Egyptian material and an aerial landscape. The pilot records explicitly note lack of blinding, prior familiarity, enhancement, sequence priming, iconic-site recognition and mixed transformation variables as confounds.

The governing image standard states: **rotation tests structure; it does not manufacture or force recognition.** It also states that observed rebinding does not by itself establish intentional multi-orientation encoding.

The confirmatory study therefore tests only the perceptual effect at the specified stimulus scope.

## 3. Primary research question

In the pre-identified target image sets, is the observer-level mean ODRR score higher than in matched control image sets when source identity and target/control status are concealed, orientation order is randomized and presentation conditions are fixed?

## 4. Hypotheses

### H1 — directional scientific hypothesis
The mean participant-level ODRR score for target sources will exceed the mean participant-level ODRR score for matched controls.

### H0
The target-control mean difference is zero.

### Equivalence hypothesis
A target-control difference whose 90% confidence interval lies entirely inside the smallest-effect-of-interest interval of **[-0.75, +0.75] ODRR points** will be treated as evidence that any difference is too small to support the pilot claim at the tested scope.

## 5. Operational definition of ODRR

For orientation transitions 2 to 4 within each source sequence, observers rate:

1. **Current coherence**: “How coherent or organized does this view appear?” 0–10.
2. **Grouping change**: “Compared with the previous view of this same source, how much did your dominant grouping or interpretation change?” 0–10.
3. **Mere rotation**: “How much does this feel like the same organization simply turned?” 0–10.

For each eligible transition:

`ODRR_transition = (coherence + grouping_change + (10 - mere_rotation)) / 3`

Source ODRR is the mean of eligible transition scores. Participant condition ODRR is the mean across all sources in that condition.

This composite is fixed before confirmatory analysis. Free-text descriptions are secondary and are not used to change the confirmatory score.

## 6. Stimulus scope

### Confirmatory target set
The first confirmatory run is a **replication of pre-identified pilot families**, not a claim about all ancient images or landscapes.

Candidate pilot families, subject to source recovery and provenance completion:
- BM 102081 baseline source;
- “clamp hands” rotation sequence;
- civ0071–civ0074 source;
- civ0081–civ0084 enhanced source, with raw counterpart required;
- Giza001–Giza004 source;
- rek0071–rek0079 source, with rotation and render-mode factors separated.

A source family is not admitted to the confirmatory set unless the untransformed source, transformation history and rights/provenance status are documented.

### Controls
Each target source is paired with a control matched as closely as feasible on:
- substrate/source class;
- aspect ratio;
- luminance range;
- contrast;
- edge density;
- visual complexity/entropy;
- rendering mode;
- crop scale.

Control selection may not use observer ODRR outcomes.

### Iconic-source sensitivity
Because Giza is highly recognizable, the primary result will be accompanied by a preregistered sensitivity analysis excluding the Giza pair. Recognition rates will be reported.

## 7. Participants

### Target sample
**60 analyzable adult observers**.

A maximum of **72 participants** may be enrolled to allow for pre-specified exclusions. There is no optional stopping based on results.

### Power basis
For a two-sided paired comparison at alpha=.05, **N=60 gives approximately 86% power for a standardized within-participant effect of dz=0.40**. The exploratory pilot effect sizes are not used for powering because the pilot was unblinded and confounded. The separate smallest effect of interest is fixed at 0.75 points on the 0–10 ODRR scale. External Stage-1 reviewers are invited to challenge either assumption before confirmatory collection; any resulting amendment must be frozen before data collection.

### Inclusion
- age 18 or older;
- informed consent;
- able to view the image task on an adequate display;
- complete the required trials.

### Exclusion
A participant is excluded only if:
- they are under 18;
- consent is absent;
- the session is materially incomplete;
- the participant token is a confirmed duplicate;
- technical logging shows stimulus delivery failure;
- two or more of three predeclared attention/task-understanding checks fail.

Prior familiarity with Geonosis is recorded but is not an exclusion criterion. It is a preregistered subgroup/sensitivity variable.

## 8. Outcome-neutral quality controls

The study includes controls whose expected direction does not depend on the target/control hypothesis.

### QC-ROT-STABLE
A simple, unambiguous structured pattern is presented under rotation without internal rearrangement.

Study-level expectation:
- median `mere_rotation >= 7`; and
- median `grouping_change <= 4`.

### QC-REARRANGED
The same primitive elements are spatially rearranged rather than merely rotated.

Study-level expectation:
- median `grouping_change >= 7`.

### Participant attention/task checks
Three predeclared instructed-response or task-understanding checks are included. Failing two or more triggers the participant exclusion rule above.

### Quality-control failure rule
If either study-level QC-ROT-STABLE or QC-REARRANGED threshold fails, the primary confirmatory outcome is automatically classified **INCONCLUSIVE — TASK/MEASUREMENT VALIDITY FAILURE**, regardless of the target-control difference. Secondary/exploratory results may still be reported but cannot rescue the confirmatory claim.

## 9. Blinding

Participants are not told:
- which sources are targets;
- which are controls;
- the historical interpretation of any source;
- the specific Geonosis reading;
- which direction is expected to score higher.

Stimulus files presented to participants use neutral randomized identifiers.

The target/control/source key is stored separately and sealed before collection. Its SHA-256 digest is committed publicly. The key itself is revealed only after the confirmatory dataset and analysis script are locked.

## 10. Randomization

A published master seed is combined with a pseudonymous participant token to generate:
- source order;
- initial orientation;
- orientation sequence.

The algorithm is deterministic and versioned in `scripts/generate_randomization.py`.

Target/control labels are never passed to the participant-facing randomizer.

## 11. Presentation

Frozen presentation parameters for v0.2:
- four orientations per ordinary source: 0°, 90°, 180°, 270°, in randomized order;
- **8.0 seconds** image exposure per orientation;
- **1.5 seconds** blank interval between orientations of the same source;
- ratings are entered after each presentation and are not speed-scored;
- no return/backtracking to earlier views during a source sequence;
- fixed image viewport and fit policy;
- no annotations or semantic labels;
- no researcher coaching during the session.

Any technical implementation must reproduce these timing rules before collection starts.

## 12. Primary outcome

For each participant:

`D_i = mean_ODRR_target_i - mean_ODRR_control_i`

Primary effect:

`D = mean(D_i)`

## 13. Primary statistical test

- Two-sided paired sign-flip permutation test on `D_i`.
- alpha = 0.05.
- 100,000 Monte Carlo sign flips unless the exact sign space is smaller and computationally feasible.
- Report D, 95% confidence interval, paired standardized effect size dz, exact/Monte Carlo p-value, and condition means.

The analysis script is written before confirmatory data are unblinded.

## 14. Equivalence test

A 90% confidence interval for D entirely within **[-0.75, +0.75]** is treated as evidence of practical equivalence at the prespecified smallest effect of interest.

## 15. Confirmatory outcome classes

Quality-control failure is evaluated first.

### SURVIVED_AT_TESTED_SCOPE
All must hold:
- both study-level quality controls pass;
- D > 0;
- two-sided permutation p < .05;
- D >= +0.75;
- 95% confidence interval excludes 0.

### EQUIVALENT / DOWNGRADE
Both study-level quality controls pass and the 90% confidence interval lies entirely inside [-0.75, +0.75].

### CONTROL_ADVANTAGE / FALSIFIED_AT_TESTED_SCOPE
Both study-level quality controls pass and the 95% confidence interval lies entirely below 0.

### INCONCLUSIVE
Any other result, including study-level quality-control failure.

These labels apply only to the specified perceptual test and stimulus set.

## 16. Secondary analyses

Secondary analyses are reported as secondary and cannot rescue a failed primary result:
- first-pass coherence;
- re-entry/priming acceleration;
- raw versus enhanced rendering;
- color versus grayscale where applicable;
- Giza-excluded sensitivity;
- familiar versus unfamiliar observers;
- recognized versus unrecognized sources;
- source-class effects;
- free-text coding by blinded coders.

## 17. Missing data

No imputation is used for the primary analysis. A source score requires all predeclared transitions unless a technical failure is logged. Participant-level inclusion requires the predeclared completion threshold stated in the data dictionary before collection.

## 18. Deviations

Any post-freeze change is:
1. timestamped;
2. justified;
3. added to `CHANGELOG.md`;
4. labelled confirmatory-impacting or non-impacting;
5. never retroactively edited out of earlier versions.

## 19. Ethics and privacy

No confirmatory human data collection begins until an ethics/research-governance review pathway is documented. Data collection is designed to avoid names, email addresses, precise location, health information and other unnecessary identifying information.

## 20. Registration and publication

Before confirmatory collection:
- freeze this protocol in a time-stamped read-only preregistration repository;
- retain the Git commit SHA;
- publish the blind-key digest;
- archive analysis code and synthetic validation outputs/record as software validation only.

After collection and unblinding:
- publish anonymized raw data where ethically permissible;
- publish the revealed blind key;
- publish analysis output;
- retain negative and null findings.

## 21. Reopen conditions

The protocol itself is reopened only for:
- identified methodological flaw;
- ethics requirement;
- technical impossibility;
- external review identifying a material defect.

A protocol amendment does not erase the prior version.
