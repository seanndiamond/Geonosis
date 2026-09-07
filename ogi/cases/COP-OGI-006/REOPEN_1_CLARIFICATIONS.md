# COP-OGI-006 — Reopen 1: Engineering and provenance clarifications

**Date:** 2026-09-07  
**Change class:** `REOPENING / EVIDENCE / CORRECTION`  
**Desired finding:** `NONE`

This reopen was triggered by six researcher challenges after the first corrected Appendix F run:

1. Is the Lunar Module's visibly crinkled exterior genuinely unusual across spacecraft?
2. How exactly did the Lunar Roving Vehicle fold, and is deployment documented?
3. Do reported rover-track shapes match the actual chevron wheel geometry?
4. Did the Nixon-call delay analysis omit material terrestrial routing latency?
5. Did Armstrong actually descend to the footpad before stepping onto the lunar surface?
6. Does the non-NASA Chandrayaan-2 OHRC Apollo-site image actually exist in retrievable/public evidence?

## 1. Lunar Module crinkling: not unique, but unusually exposed

The Apollo LM technical reference explicitly describes an external thermal/micrometeoroid blanket of at least 25 layers of extremely thin aluminized polymer sheets. It states that the sheets were **hand crinkled before blanket fabrication** to provide vent paths and reduce conductive contact between layers.

Other spacecraft use flexible multilayer thermal blankets. The Space Shuttle also used flexible thermal-protection blankets, including AFRSI over large portions of its leeward surfaces. Those Shuttle blankets were quilted silica structures with coated outer surfaces because an orbiter had to survive atmospheric ascent/re-entry and aerodynamic loading. The LM, by contrast, operated as a vacuum-only lunar vehicle after being carried inside the launch adapter and could leave its lightweight blanket system visibly irregular.

**Current state:**
- `WRINKLED_THERMAL_BLANKETS_UNIQUE_TO_APOLLO = UNSUPPORTED`
- `LM_EXTERNAL_BLANKET_WAS_VISUALLY_MORE_EXPOSED_AND_IRREGULAR_THAN_SHUTTLE_TPS = SUPPORTED_AS_DESIGN_DIFFERENCE`

Sources:
- NASA Apollo LM News Reference: https://www.nasa.gov/wp-content/uploads/static/history/alsj/lm04_lunar_module_pplv1-17.pdf
- NASA AFRSI / reusable TPS: https://www.nasa.gov/general/thermal-protection-materials-branch-reusable-materials/

## 2. LRV folding and deployment

Apollo 15 documentation states that the aluminium chassis was divided into forward, centre and aft sections, with the **forward and aft chassis sections folding over the centre section** for LM stowage. The suspension/wheels were also folded inward as part of the stowed package.

The Apollo 15 mission report documents the actual deployment operation on the Moon, including reset walking hinges, deployment tapes, chassis hinge-lock pins, and the vehicle bouncing during deployment in a manner comparable with preflight one-sixth-g tests. A 1972 NASA/Boeing paper specifically describes the LRV deployment mechanism.

**Current state:**
- `LRV_FOLDING_MECHANISM_DOCUMENTED_CONTEMPORANEOUSLY = SUPPORTED`
- `LUNAR_DEPLOYMENT_OPERATION_DOCUMENTED = SUPPORTED`

Sources:
- Apollo 15 Press Kit: https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A15_PressKit.pdf
- Apollo 15 Mission Report: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a15/ap15mr.pdf
- NASA NTRS, Lunar roving vehicle deployment mechanism: https://ntrs.nasa.gov/citations/19730010149

## 3. Rover wheel and track morphology

The LRV wheel was a woven zinc-coated piano-wire mesh with titanium chevron treads riveted around the circumference. Contemporary NASA documentation does **not** show a separate continuous longitudinal centre rib. The chevron tread itself converges toward the wheel centreline.

Apollo mobility reports say the chevron pattern left distinct, sharp imprints in lunar soil. Because the tread is a repeated V/chevron, a photograph can show a sequence of centre-apex marks; soil deformation, lighting and image sampling can also visually merge repeated apexes. However, that general explanation is **not sufficient to adjudicate a specific photograph** alleging:

- one missing wheel track;
- a continuous central depression not present on the wheel;
- continuous rather than segmented chevron marks.

The current conversation attachments include an Apollo 14 LM photograph and an Artemis II Moon/Earth photograph. Apollo 14 did not carry an LRV. Therefore the exact rover-track image described by the researcher is not presently available for pixel-level adjudication in this reopen.

**Current state:**
- `LRV_SEPARATE_LONGITUDINAL_CENTRE_RIB = NOT_FOUND_IN_DESIGN_DOCUMENTATION`
- `CHEVRON_TREAD_GEOMETRY = SUPPORTED`
- `SPECIFIC_MISSING_SECOND_TRACK_CLAIM = NOT_ADJUDICATED_IMAGE_NOT_PRESENT`
- `SPECIFIC_CENTRE_DEPRESSION_MISMATCH = NOT_ADJUDICATED_IMAGE_NOT_PRESENT`
- `SPECIFIC_CONTINUOUS_VS_SEGMENTED_TREAD_MISMATCH = NOT_ADJUDICATED_IMAGE_NOT_PRESENT`

Sources:
- Apollo 15 Press Kit: https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A15_PressKit.pdf
- NASA LRV wheel/tire configuration: https://ntrs.nasa.gov/api/citations/19910005287/downloads/19910005287.pdf
- NASA Technical Report R-401 / LPI mirror: https://www.lpi.usra.edu/lunar/documents/NTRS/collection2/NASA_TR_R_401.pdf

## 4. Nixon-call routing: prior timing was incomplete

The prior Appendix F correctly used ~1.28 s as the Earth-Moon one-way light time and ~2.56 s as the minimum lunar radio round trip. That is **not the entire White House-to-astronaut-to-White House path**.

The Nixon Library preserves the original WHCA audio recording as an original 1/4-inch reel-to-reel source. The Nixon Foundation describes the call as travelling an estimated ~290,000 miles one way. If that path length is used, vacuum propagation alone is roughly 1.56 s one way or ~3.11 s round trip before human reaction, switching, analogue network, satellite/terrestrial relay or audio-processing latency.

The researcher's proposed serial path through Parkes requires correction. Apollo EVA communications records show that **Goldstone handled voice uplink to the LM throughout the EVA**, while Parkes became primarily a high-quality television downlink source. Thus Parkes should not simply be inserted as a serial voice-uplink node.

**Current state:**
- `2.56_SECONDS_AS_COMPLETE_NIXON_CALL_ROUND_TRIP = CORRECTED / TOO_LOW`
- `~3.1_SECONDS_AS_PURE_PROPAGATION_FLOOR_USING_290000_MILE_ONE_WAY_PATH = SUPPORTED_AS_APPROXIMATION`
- `PARKES_AS_SERIAL_VOICE_UPLINK_NODE_DURING_NIXON_CALL = UNSUPPORTED`
- `RAW_WHCA_AUDIO_PRECISE_TURNAROUND_TIMING = RESEARCH_DEBT`

Sources:
- Nixon Library WHCA original recording catalogue: https://www.nixonlibrary.gov/research/almanac/july-20-1969
- Nixon Foundation 290,000-mile description: https://www.nixonfoundation.org/2019/07/moon-landing-50th-anniversary-celebrated-nixon-library/
- Apollo EVA comm records / Goldstone uplink: https://www.honeysucklecreek.net/Apollo_11/TV_from_Moon.html

## 5. Footpad geometry and Armstrong's descent

The concern about the footpad geometry is legitimate to inspect because the pad is not a broad flat staircase landing. Apollo technical documentation describes it as a dish-shaped aluminium-honeycomb pad approximately **37 inches (94 cm) in diameter and ~7 inches deep**, attached to the primary strut by a ball-and-socket joint so it could conform to terrain.

The Apollo 11 Surface Journal's documented sequence is nevertheless explicit: Armstrong made the roughly three-foot descent from the last rung to the footpad, remained supported by the ladder, stood on the pad, probed the soil with his boot, and then stepped the short remaining distance to the lunar surface. The mission summary describes only a couple of inches between the pad and surface after landing.

Therefore the visual hypothesis `Armstrong jumped directly from the ladder to the lunar soil` is not presently supported by the transcript/technical sequence. It remains falsifiable by frame-by-frame analysis of the original EVA footage, but the documentary state favours footpad-first.

**Current state:**
- `FOOTPAD_IS_DISH_SHAPED_AND_NOT_A_LARGE_FLAT_PLATFORM = SUPPORTED`
- `FOOTPAD_DIAMETER_APPROX_37_INCHES = SUPPORTED`
- `ARMSTRONG_DESCENDED_TO_FOOTPAD_BEFORE_SURFACE = SUPPORTED`
- `ARMSTRONG_DIRECT_LADDER_TO_SOIL_JUMP = UNSUPPORTED`

Sources:
- NASA LM landing-gear report: https://ntrs.nasa.gov/api/citations/19720018253/downloads/19720018253.pdf
- Apollo 11 Surface Journal summary: https://history.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.summary.html

## 6. Chandrayaan-2 OHRC Apollo 11 image: evidence state changed

The prior Appendix F recorded:

`INDEPENDENT_SUB_METRE_APOLLO_SITE_IMAGE = NOT_RETRIEVED`

That state is superseded.

A 2024 peer-reviewed paper in *Planetary and Space Science*, using Chandrayaan-2 OHRC data, states that on **2 April 2021** OHRC imaged the Apollo 11 landing site at approximately **0.26 m spatial resolution** and that the Apollo 11 LM is visible in the OHRC image. The paper used the same image to map more than 8,500 boulders around West crater.

ISRO independently documents OHRC's ~0.25 m nadir sampling and explicitly lists Apollo/Luna landing sites among the instrument's anthropogenic science targets. ISRO's PRADAN archive provides raw and calibrated OHRC data products.

The corrected state is therefore:

`INDEPENDENT_SUB_METRE_APOLLO_11_SITE_IMAGE = LOCATED / PUBLISHED`

but not yet:

`RAW_PRADAN_PRODUCT_ID_AND_PIXEL_CHAIN = FULLY_RETRIEVED_AND_INSPECTED`

The raw archive product identifier, calibrated binary and XML geometry/custody chain remain research debt if the Court is to climb from published description to direct pixel-level inspection.

Sources:
- Nagori et al., Planetary and Space Science 2024: https://www.sciencedirect.com/science/article/pii/S0032063323001976
- ISRO OHRC science objectives/specifications: https://www.isro.gov.in/media_isro/pdf/science/science_results_from_ch.pdf
- ISRO PRADAN archive: https://pradan.issdc.gov.in/ch2/

## OGI result of Reopen 1

This reopen is useful because it contains all three possible outcomes of a challenge:

- **challenge resolved against the objection:** LRV folding, general blanket uniqueness, direct ladder-to-soil interpretation;
- **challenge materially corrects OGI:** Nixon full-path propagation floor;
- **new retrieval materially upgrades evidence:** independent Indian Apollo 11 OHRC image from `NOT_RETRIEVED` to `LOCATED/PUBLISHED`.

The rover-track morphology question remains deliberately **UNRESOLVED at image level** until the exact alleged track photograph is supplied/retrieved.

The Apollo overall finding is not changed by this reopen:

- crewed Apollo landing proposition: `SUPPORTED / HIGH CONFIDENCE`
- post-1972 human lunar-landing replication gap: `REAL ANOMALY / EXPLANATION INCOMPLETE`

What changes is the derivation underneath that finding.
