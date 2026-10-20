# Confirmatory Analysis Plan — ODRR-RR-001

## Frozen unit of inference

The primary unit is the **participant**, not the individual rating and not the image.

For participant `i`:
- compute each source mean ODRR across eligible orientation transitions;
- average source means within target condition;
- average source means within control condition;
- compute `D_i = target_i - control_i`.

This prevents trial count from masquerading as independent replication.

## Primary test

Two-sided paired sign-flip permutation test on the vector of `D_i`.

- alpha: 0.05
- Monte Carlo draws: 100,000
- random seed: 20260907 for analysis reproducibility
- statistic: absolute mean paired difference

## Effect estimate

Report:
- target mean and SD;
- control mean and SD;
- mean paired difference D;
- 95% bootstrap CI for D using 10,000 participant-level resamples;
- paired standardized effect `dz = mean(D_i)/sd(D_i)`.

## Practical-equivalence rule

Smallest effect of interest (SESOI): ±0.75 points.

If the 90% bootstrap CI for D is fully contained in [-0.75, +0.75], classify as `EQUIVALENT / DOWNGRADE`.

## Outcome precedence

1. If 95% CI is fully below 0: `CONTROL_ADVANTAGE / FALSIFIED_AT_TESTED_SCOPE`.
2. Else if 90% CI is fully inside the SESOI: `EQUIVALENT / DOWNGRADE`.
3. Else if p < .05, D >= .75, and 95% CI > 0: `SURVIVED_AT_TESTED_SCOPE`.
4. Else: `INCONCLUSIVE`.

This order prevents a small statistically significant effect from being mislabeled as substantive survival.

## Sensitivity analyses

Predeclared and non-rescuing:
- exclude Giza pair;
- exclude observers reporting substantial prior Geonosis familiarity;
- exclude source pairs recognized by the participant;
- raw-only sources;
- source-class summaries.

## Free-text

Free-text is not scored for the primary endpoint. If coded:
- coders remain blind to target/control status;
- codebook is frozen before coding;
- inter-rater agreement is reported;
- semantic convergence is secondary.

## Exclusions

A file named `EXCLUSIONS.csv` must list every excluded participant token, reason, decision date and whether the decision was made before unblinding.

No outcome-based exclusions are allowed.

## Laboratory log

Maintain a date/time log of:
- collection opening;
- each protocol amendment;
- technical incident;
- collection closure;
- data lock;
- blind-key reveal;
- analysis execution.

## No rescue clause

If the primary result fails, secondary analyses may explain or localize the failure but may not change the primary classification.
