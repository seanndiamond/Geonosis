# Objective Control Matching — ODRR-RR-001

## Purpose

Control selection must not become a hidden investigator degree of freedom. Candidate controls are characterized from image-level features before any participant outcomes exist.

## Hard eligibility gates

1. Same broad source/substrate class as the paired target where feasible: clay/incised/relief, painted/plastered surface, or aerial/terrain.
2. Control must not be the same physical object, same crop, same site view, or a transformed derivative of the target.
3. No annotations, arrows, text labels, borders, UI chrome, captions, or researcher markings may remain in the stimulus region.
4. Rendering mode must match the paired target stratum: raw grayscale, raw colour, enhanced, etc.
5. Crop scale must be broadly comparable and documented.
6. Candidate controls may not be selected because an observer previously reported little or no rebinding. No outcome-informed control selection.
7. At least three eligible candidate controls should exist per target family before matching. If that cannot be achieved, the target is held out of the primary confirmatory set rather than force-matched.

## Pre-outcome numeric features

Measured on the canonical source-content region before the square display canvas is added:
- log aspect ratio;
- mean luminance (0–1);
- RMS contrast (0–1);
- grayscale Shannon entropy (bits);
- gradient edge density;
- mean gradient magnitude;
- 8-bin gradient-orientation histogram;
- horizontal/vertical orientation anisotropy.

## Draft admissibility tolerances

A candidate control is ordinarily eligible only if all hold:
- aspect-ratio ratio between 0.80 and 1.25;
- absolute mean-luminance difference <= 0.10;
- absolute RMS-contrast difference <= 0.10;
- entropy difference <= 0.75 bits;
- edge-density ratio between 0.75 and 1.33, unless both are near zero;
- mean-gradient ratio between 0.75 and 1.33, unless both are near zero;
- Jensen-Shannon divergence of the 8-bin orientation histograms <= 0.20.

These are Stage-1 draft thresholds. They may be challenged and amended before preregistration freeze, but any change remains in correction lineage.

## Deterministic selection

Among eligible controls in the same substrate/render stratum:
1. standardize the numeric features across the eligible candidate pool;
2. compute equal-weight Euclidean distance on log aspect ratio, luminance, contrast, entropy, edge density, mean gradient, orientation anisotropy and orientation-histogram bins;
3. select the smallest-distance unused candidate;
4. break exact ties lexicographically by source ID;
5. remove the selected control from the remaining pool.

Participant ratings and ODRR outcomes are never input to the matching algorithm.

## Failure to match

If no eligible control survives the hard gates and numeric tolerances, the target source is not allowed into the primary confirmatory comparison. It may remain exploratory.

## Important boundary

These image statistics are not claimed to exhaust perceptual similarity. An independent vision/psychophysics reviewer is explicitly invited to challenge the features, thresholds, and weighting before preregistration is frozen.

Once frozen, matching criteria cannot be tuned using confirmatory outcomes.

## Rights-sensitive images

Source images with uncertain redistribution rights can be processed locally. The public archive may contain feature vectors and SHA-256 fingerprints without necessarily redistributing the underlying image.
