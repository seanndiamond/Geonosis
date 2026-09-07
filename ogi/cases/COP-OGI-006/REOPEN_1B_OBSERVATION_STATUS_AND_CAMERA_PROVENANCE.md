# COP-OGI-006 — Reopen 1B: Observation status, camera provenance, and negative visual evidence

**Date:** 2026-09-07  
**Change class:** `REOPENING / EVIDENCE / CORRECTION / CLARIFICATION`  
**Desired finding:** `NONE`

This reopen corrects a methodological error in prior discussion: exhibit-level observations were repeatedly described as the researcher's "suspicions." That wording improperly weakens their evidentiary status before adjudication.

## 1. Observation is not suspicion

The supplied images support direct exhibit-level observations, including:

- conspicuous boot impressions are visible in some frames;
- a clear continuous wheel-track pattern is not visible in the cited rover-area frame;
- the close LRV wheel image shows segmented chevron grousers and no obvious separate continuous longitudinal centre rib;
- the supplied retroreflector frame does not show an obvious continuous chain of boot impressions terminating at the instrument;
- the supplied Armstrong descent screenshots do not visually resolve boot contact with the footpad;
- the LM footpad is visibly dish-shaped rather than a broad flat platform;
- the supplied LM exterior is visibly irregular/crinkled while the supplied CSM image is comparatively smooth.

These are **observations from exhibits**. They may or may not ultimately establish a contradiction with the Apollo account, but they must not be demoted to "suspicions" merely because they challenge a conventional narrative.

Candidate OGI failure:

`OBSERVATION_DOWNGRADE`

> A direct observation from an admitted exhibit is relabelled as suspicion, concern, or belief before adjudication, reducing its evidentiary weight without a derivational basis.

## 2. Negative visual evidence and detectability

Absence can become evidentiary when the image demonstrates that comparable marks would be visible at the same scale and lighting.

In the supplied Apollo surface frames:

- bootprints can be sharply resolved;
- small rocks and soil disturbance are visible;
- therefore the non-appearance of an expected rover chevron trail or a clear approach trail near an instrument is not automatically trivial.

However, two distinct propositions must remain separate:

1. `MARK_NOT_VISIBLE_IN_FRAME` — direct image observation.
2. `MARK_SHOULD_BE_VISIBLE_AT_THIS_LOCATION_IF_EVENT_OCCURRED` — requires path, geometry, timing, illumination, and expected morphology.

Thus OGI records the cited missing marks as **negative visual evidence**, not as a completed contradiction.

Current states:

- `ROVER_TRACK_NOT_CONSPICUOUS_IN_SUPPLIED_FRAME = OBSERVED`
- `LRRR_APPROACH_BOOT_TRAIL_NOT_CONSPICUOUS_IN_SUPPLIED_FRAME = OBSERVED`
- `EXPECTED_ROVER_PATH_THROUGH_EXACT_PIXELS = NOT_YET_MAPPED`
- `EXPECTED_LRRR_APPROACH_PATH_THROUGH_EXACT_PIXELS = NOT_YET_MAPPED`
- `CONTRADICTION = NOT YET ADJUDICATED`

## 3. Apollo 11 first-step imagery used two different camera systems

The existence of two relevant viewpoints is contemporaneously documented before the landing.

### External television camera

The Apollo 11 press kit states that the black-and-white lunar TV camera was stowed in the LM's Modular Equipment Stowage Assembly (MESA). When Armstrong pulled the lanyard to deploy the MESA, the assembly swung down and the camera was automatically aimed at the ladder/foot-of-ladder area. The camera was later removed and placed on a tripod.

NASA's Apollo Television technical history likewise describes the TV camera as shock-mounted on the MESA and notes that the MESA deployment positioned it to record the first steps.

### Internal 16-mm camera

Apollo 11 also carried a Maurer Data Acquisition Camera inside the LM. NASA camera documentation states that the LM camera was mounted inside the LM, looking through the right-hand window, and that Armstrong was filmed during lunar-surface EVA by the lunar module pilot.

Thus two distinct viewpoints are physically documented:

- outside TV camera on the MESA;
- inside 16-mm film camera through the LM window.

The 16-mm film was not a second live external television camera.

### Consequence for the supplied NTD 2012 video

The supplied screenshots come from a later edited video compilation. If that video cuts between the external TV source and the internal 16-mm source around the footpad moment, the edit itself is a **post-mission editorial choice** and must not be confused with live mission switching.

Therefore:

- `TWO_CAMERA_VIEWPOINTS_EXIST = SUPPORTED`
- `SECOND_VIEW_REQUIRED_ANOTHER_EXTERNALLY_DEPLOYED_CAMERA = UNSUPPORTED`
- `NTD_2012_EDIT_SHOWS_UNBROKEN_PAD_CONTACT = NO`
- `SUPPLIED_SCREENSHOTS_VISUALLY_RESOLVE_BOOT_CONTACT_WITH_PAD = NO`

Current image-level state for Armstrong remains:

`DOCUMENTARY ACCOUNT: FOOTPAD FIRST`

`SUPPLIED VIDEO FRAMES: FOOT/PAD CONTACT NOT VISUALLY RESOLVED`

## 4. Retroreflector footprints

NASA image sequence metadata identifies:

- AS11-40-5942: Aldrin carrying the PSEP and laser-ranging retroreflector toward deployment;
- AS11-40-5949: retroreflector already deployed while Aldrin works on the seismic package;
- AS11-40-5952: detail of the deployed retroreflector.

This sequence establishes a testable image-first path reconstruction.

The supplied reflector image itself shows high surface detail and visible boot impressions in the broader foreground, while no obvious continuous walking sequence terminates at the reflector in the supplied crop.

Current state:

- `NO_OBVIOUS_CONTINUOUS_BOOT_TRAIL_TERMINATING_AT_LRRR_IN_SUPPLIED_FRAME = OBSERVED`
- `ASTRONAUT_NEVER_APPROACHED_LRRR = NOT ESTABLISHED`
- `IMAGE_SEQUENCE_PATH_RECONSTRUCTION = REQUIRED`

The correct next operation is to register AS11-40-5942, 5948/5949, 5952 and nearby frames using stable rocks/craters, then map surface disturbance and approach geometry without beginning from the deployment narrative.

## 5. Hadfield / Barenaked Ladies video provenance

The supplied screenshot shows the CBC Music video titled `Chris Hadfield and Barenaked Ladies | I.S.S. (Is Somebody Singing)`.

The visible performance is tightly synchronized. That is a valid observation.

However, contemporary reports identify the February 2013 CBC release as a **prerecorded production**: Hadfield recorded his vocal/guitar part aboard the ISS and Robertson/Barenaked Ladies/Wexford performers recorded on Earth; the released video was then synchronized as a production.

Therefore the tight synchronization visible in that specific video does not measure real-time Earth-to-ISS round-trip latency.

A separate May 6, 2013 Music Monday event was explicitly advertised and documented as a **live** space-to-Earth singalong with Hadfield and students.

These two events must not be conflated.

Current state:

- `SUPPLIED_CBC_VIDEO_VISUALLY_SYNCHRONIZED = OBSERVED`
- `SUPPLIED_CBC_VIDEO_IS_PROOF_OF_ZERO_OR_SUBSECOND_TWO_WAY_MUSICAL_LATENCY = UNSUPPORTED`
- `FEB_2013_CBC_RELEASE_PRERECORDED = SUPPORTED`
- `MAY_6_2013_MUSIC_MONDAY_EVENT_LIVE = SUPPORTED`
- `MAY_LIVE_EVENT_TWOWAY_PHASE_LOCK_MECHANISM = NOT YET ADJUDICATED`

## 6. OGI methodological lesson

This reopen sharpens the Court rule:

> **Observation first. Expected consequence second. Explanation third. Adjudication last.**

OGI must neither promote an observation directly to contradiction nor demote it to suspicion because an institutional explanation exists.

The relevant candidate failure classes now include:

- `OBSERVATION_DOWNGRADE`
- `EXPLANATION_BEFORE_EXHIBIT_MATCH`
- `EXHIBIT_ASSERTION_SUBSTITUTION`

All remain candidates pending recurrence and formal promotion.
