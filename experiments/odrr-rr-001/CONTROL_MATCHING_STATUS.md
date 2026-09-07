# Control Matching Status — ODRR-RR-001

**Current state:** target feature extraction implemented; target feature vectors computed; hard matching gates and deterministic matcher implemented; control candidate pool not yet assembled.

## What happens next

For each target family, build a source-class-specific candidate pool of at least three controls that meet the categorical gates. Compute the frozen feature vector for each candidate, apply the admissibility tolerances, then let the deterministic matcher choose the nearest unused control.

No human ODRR rating may be used to decide which control enters or leaves the pool.

## Current target strata

- SRC-A: provisional clay/incised/relief candidate.
- SRC-B: primary clay/incised/relief candidate.
- SRC-C: secondary enhanced clay/incised/relief candidate pending raw counterpart.
- SRC-D: provisional aerial/terrain candidate pending original figure file.
- SRC-E: provisional painted/plastered candidate pending full parent/source provenance.

The source-code mapping remains private until unblinding.
