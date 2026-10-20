# ODRR-RR-001 Blinded Target Pack Build Specification v0.2

**Status:** candidate target pack only; controls not yet added; not participant-ready.

## Recovered target-source families in this build

Five currently recovered source families are represented. Their public identities remain separate from the neutral observer filenames. One previously listed pilot family, BM 102081, remains unresolved as a distinct source unless it proves to be identical to one of the recovered families.

## Fixed preprocessing for target-candidate pack v0.2

1. Apply EXIF orientation to establish canonical display pixels.
2. For the currently supplied Giza webpage screenshot only, crop the figure using fixed source-pixel box `(209, 381, 727, 900)`.
3. Remove only contiguous near-white page borders at source edges. A row/column is treated as page-white when at least 90% of pixels have luminance >=245. Only contiguous qualifying rows/columns from the outer edges are removed.
4. Resize each canonical content image once using Lanczos so its longest side is 900 px.
5. Generate 0°, 90°, 180°, and 270° counter-clockwise views from that single resized parent.
6. Use no further interpolation during rotation.
7. Center each orientation on a 1024×1024 neutral RGB(127,127,127) canvas.
8. Save lossless PNG with randomized neutral filename.

This design is intended to prevent page margins, UI chrome, independent resampling and semantic filenames from becoming accidental orientation cues.

## Blinding architecture

- Observer files carry neutral randomized IDs only.
- The private key maps neutral IDs to source family and rotation.
- The key is not committed publicly before unblinding.
- The SHA-256 digest of the private key is committed publicly before confirmatory collection.
- The target-only pack must never be given to participants as the final experiment. It must first be combined with matched controls and rerandomized.

## Current public commitment digest

The v0.2 private target-key SHA-256 is stored in `BLIND_KEY_SHA256.txt`.

## Rights boundary

Unresolved image-redistribution status does not erase the image from scientific inspection. The source pixels may be processed locally while the public repository carries hashes, feature vectors, transformation records and source pointers. Public redistribution of source/derived pixels remains a separate decision.

## Scientific boundary

This pack freezes candidate stimuli. It does not constitute evidence that ODRR survives blinded controls.
