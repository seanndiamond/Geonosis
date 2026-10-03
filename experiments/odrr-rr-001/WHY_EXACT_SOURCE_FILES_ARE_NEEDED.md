# Why Exact Source Files Are Still Required — ODRR-RR-001

The experiment does not require perfect copyright paperwork before the pixels can be scientifically inspected. It does require exact source files for methodological reasons.

## What exact source files establish

1. **Parentage** — whether multiple orientations are the same pixels or separately edited descendants.
2. **Transformation history** — crop, contrast, enhancement, grayscale conversion, mirroring, sharpening, compression and annotation can themselves change perceptual grouping.
3. **Single-resampling rule** — the rotation series should come from one parent, not four independently resampled copies.
4. **Context/crop lock** — a crop can create or remove relations. The exact crop must be frozen before outcomes are collected.
5. **No pseudo-replication** — several files derived from one photograph are one source family, not several independent exhibits.
6. **Objective control matching** — luminance, contrast, entropy, edge structure and orientation statistics must be measured from the exact stimulus content.
7. **Hash commitment** — SHA-256 binds the preregistration to exact files so stimuli cannot be swapped after outcomes are known.
8. **Semantic-cue removal** — captions, UI chrome, labels, arrows and filenames can reveal source identity and break blinding.
9. **Rights/provenance separation** — provenance and redistribution status can be recorded without excluding the exhibit from scientific analysis.
10. **Independent reproduction** — another researcher must be able to reconstruct the same stimulus from the same parent or verify the exact hash.

## Current outstanding source requirements

- **BM 102081 baseline source**, if it is distinct from the recovered `civ` family.
- **Clamp-hands provenance:** institution/object/source-page identity for the supplied `clamp hands.jpg`.
- **civ0071–74 provenance:** institutional/object identity for the recovered tablet. File-level parentage is already established: the four files decode to the same underlying JPEG pixel matrix and differ in EXIF orientation.
- **civ0081 raw counterpart:** the pilot log records the 0081–0084 family as enhanced. A raw/unenhanced parent is required before this family can enter the primary confirmatory stratum; the supplied enhanced image can remain a secondary enhancement stratum.
- **Giza original figure file:** the current fixed crop is from a webpage screenshot. The original figure/image file is preferred to lock the source before confirmatory use.
- **Rekhmire full parent:** the supplied image is already cropped. The full uncropped parent and exact source/page provenance are required to lock context and separate crop from rotation/render-mode effects.

A missing item does not make the visible image unusable for analysis. It determines whether the family is PRIMARY, PROVISIONAL, SECONDARY or EXCLUDED from the confirmatory set.
