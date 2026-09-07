# Objective Control Matching — ODRR-RR-001

## Purpose

Control selection must not become a hidden investigator degree of freedom. Candidate controls are therefore characterized using image-level features before any participant outcomes exist.

## Pre-outcome features

The current draft matcher uses:
- source class / substrate class (exact categorical gate where possible);
- aspect ratio;
- mean luminance;
- RMS contrast;
- normalized gradient edge strength;
- grayscale entropy.

All numeric variables are standardized across the eligible target/control candidate pool before distance calculation.

## Deterministic matching rule

For each target in lexicographic `source_id` order:
1. retain unused control candidates from the same declared source class;
2. calculate equal-weight Euclidean distance in standardized feature space;
3. select the smallest-distance candidate;
4. break an exact tie by lexicographic control `source_id`;
5. remove that control from the available pool.

The algorithm does not ingest participant ratings or ODRR outcomes.

## Important boundary

This is a transparent **draft matching rule**, not a claim that these image statistics exhaust perceptual similarity. An independent vision/psychophysics reviewer is specifically invited to challenge the features and weighting **before preregistration is frozen**.

Once the protocol is frozen, matching criteria cannot be tuned using confirmatory outcomes.

## Rights-sensitive images

Source images with uncertain redistribution rights can be processed locally. The public archive may contain feature vectors and SHA-256 fingerprints without necessarily redistributing the underlying image.
