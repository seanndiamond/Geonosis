# ODRR-RR-001 Source Intake Notes — 2026-09-07

## Scope

This record documents source files supplied by Sean Diamond for the ODRR pilot families. It does **not** convert uncertain copyright/licensing into unrestricted redistribution rights, and it does **not** treat missing provenance as a reason to discard an exhibit from scientific analysis.

Current operating rule: evidentiary provenance and copyright/licensing are separate questions. Files may be inspected, measured and used as research exhibits while rights status remains `UNKNOWN/UNVERIFIED`. Public redistribution decisions are made separately.

## Files received

See `SOURCE_INTAKE_2026-09-07.csv` for exact byte sizes and SHA-256 hashes.

Received families:

- `clamp hands.jpg` — candidate source for RPL-001.
- `civ0071.JPG` through `civ0074.JPG` — RPL-002 orientation series.
- `original civ0081.JPG` — user-supplied file named as the original parent for the RPL-003 enhanced series.
- `Screenshot 2026-09-07 221336.jpg` — provenance screenshot for the RPL-004 Giza source family.
- `original rek only cropped.jpg` — user-supplied cropped parent for the RPL-005 Rekhmire sequence.

## Strong technical finding: civ0071–civ0074

The four files `civ0071.JPG`, `civ0072.JPG`, `civ0073.JPG` and `civ0074.JPG` contain the **same decoded JPEG pixel matrix** before EXIF orientation is applied.

Raw decoded pixel SHA-256 for all four:

`2e51189c7279e2bbaf4f1bfdf05164301e10897ab1c53488b7ae3d766ce403ce`

The files differ in EXIF Orientation metadata:

| File | EXIF orientation | Display interpretation |
|---|---:|---|
| civ0071.JPG | 1 | normal |
| civ0072.JPG | 6 | 90° clockwise |
| civ0073.JPG | 3 | 180° |
| civ0074.JPG | 8 | 90° counter-clockwise |

### Consequence for RPL-002

This is stronger than an ordinary manually rotated image sequence. The underlying image content is pixel-identical and the orientation difference is carried by metadata, so the four-member set does not introduce separate crop, contrast, sharpening, resampling or JPEG-compression changes between orientations.

This substantially narrows a confound for the RPL-002 pilot observation. It does **not** by itself establish that any perceived rebinding is intentional encoding, nor that the target will outperform matched controls under blinding.

## RPL-003 relationship status

`original civ0081.JPG` is accepted provisionally as the user-supplied parent for the enhanced RPL-003 sequence. Its relationship to the RPL-002 source has not been established by exact pixel identity and must not be silently inferred.

## Giza source provenance recovered from the supplied screenshot

The supplied screenshot visibly records the following figure-level information:

- subject: Great Pyramids at Giza, Egypt;
- sensor/source description: panchromatic IKONOS image;
- stated spatial resolution: 1 m/pixel;
- stated acquisition date: 17 November 1999;
- figure caption credits: `Image courtesy of Space Imaging`;
- figure page identifies uploader: Lela Prashad;
- source publication page displayed: *Investigation of human modifications of landscape and climate in the Phoenix Arizona Metropolitan area using MASTER data* (Jan 2004).

A web retrieval on 2026-09-07 located the same ResearchGate figure page and matching caption. This upgrades the Giza item from source-unknown to `FIGURE_SOURCE_LOCATED`, but the exact original `Giza001–Giza004` derivatives used in the pilot are still not supplied.

ResearchGate figure URL:
https://www.researchgate.net/figure/Panchromatic-IKONOS-image-of-the-Great-Pyramids-at-Giza-Egypt-1-m-pixel-spatial_fig1_228827635

## Provenance still open

The following remain unresolved and must stay explicit:

1. Exact institutional/catalogue source for `clamp hands.jpg`.
2. Exact object identity and institutional source for the `civ` tablet imagery, unless separately established from an earlier case file.
3. Exact derivation chain from `original civ0081.JPG` to every enhanced RPL-003 image.
4. Exact derivation chain from the located IKONOS Giza figure to `Giza001–Giza004`.
5. Exact museum/page provenance for `original rek only cropped.jpg`.
6. BM 102081 source used for RPL-000, unless one of the above is later demonstrated to be that same source.

## Copyright / rights posture

For the confirmatory science:

- do not discard an image merely because its licensing record is incomplete;
- preserve the best provenance actually available;
- mark ownership, licence and redistribution rights as `UNKNOWN/UNVERIFIED` where they are not established;
- analyse the visible exhibit;
- do not invent licence status or ownership;
- prefer publishing hashes, measurements, provenance records and analysis code where redistribution of the source image itself remains unresolved.

This record therefore separates **scientific admissibility for analysis** from **public redistribution permission**.

## Evidence-state update

- Source files supplied: `RETRIEVED`.
- Pixel structure and metadata inspected: `INSPECTED`.
- RPL-002 orientation relationship: `MAPPED` at the image-file level.
- Confirmatory ODRR claim: remains **not independently reproduced**.

## Would reopen if

- source metadata contradicts a current mapping;
- an uploaded file is shown to be a derivative rather than the stated parent;
- the display software used in the pilot did not honor EXIF orientation as assumed;
- matched control testing shows equal or stronger rebinding;
- blinding, observer independence or quality-control gates remove the apparent effect.
