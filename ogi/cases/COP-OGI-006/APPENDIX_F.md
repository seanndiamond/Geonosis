# Appendix F — Did Humans Land on the Moon? The Staircase Before the Explanation

## Methodological declaration

This appendix is a stress test of OGI v0.3.

- case: `COP-OGI-006`
- subject: the Apollo crewed lunar-landing proposition and the post-1972 replication gap
- purpose: test whether OGI can adjudicate a contested historical-technological proposition before explaining its downstream anomaly
- desired finding: `NONE`
- legal standing: `NONE`
- reopenable: yes

The originating observation was:

> Humans frequently imitate, repeat and escalate difficult achievements once somebody has demonstrated them. Why, then, has no human landed on the Moon since 1972?

A first OGI pass failed by explaining the gap before adjudicating the antecedent proposition that crewed Apollo landings occurred. That failed pass is preserved in `FIRST_PASS_FAILURE.md`.

The corrected order is:

1. Did humans land on the Moon as claimed?
2. What does each evidence class actually establish?
3. Which evidence streams are genuinely independent?
4. How well can alternative models explain the joint evidence field?
5. Only then: what evidentiary weight should be assigned to the 54-year crewed-landing gap?

## 1. Communication delay: what physics requires

At the Moon's mean distance of about 384,400 km, light or radio takes approximately 1.28 seconds one way.

Therefore a ground speaker finishing a sentence, an astronaut hearing it, replying, and the ground receiving the reply cannot normally produce a conversational turnaround much below about 2.56 seconds, before human reaction time and terrestrial processing are added.

NASA's Apollo 11 mission report contains an unusually useful internal control: during lunar surface operations, uplink voice was turned around through the Lunar Module S-band system and heard back on the ground as an echo **2.6 seconds later**.

Primary source:
- Apollo 11 Mission Report / NTRS: https://ntrs.nasa.gov/api/citations/19700008096/downloads/19700008096.pdf

### The Nixon call

The corrected lunar-surface transcript records:

- 110:16:25 Houston: `Go ahead, Mr. President.`
- 110:16:30 Nixon begins speaking.
- 110:17:44 Armstrong begins his reply.
- 110:18:12 Nixon begins his final sentence.
- 110:18:21 Aldrin begins: `I look forward to that very much, sir.`

Source:
- Apollo 11 Lunar Surface Journal: https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.mobility.html

The final exchange therefore is not timestamped as an instantaneous response. Nixon's final sentence itself consumes several seconds; Aldrin's reply begins nine seconds after Nixon begins it. This is compatible with a roughly 2.6-second radio round trip plus speech duration and reaction.

The communication path also needs correcting. The White House telephone audio was patched into Mission Control and then into the Apollo tracking network. During the EVA, voice uplink to the Lunar Module was handled through Goldstone; Australian stations supplied downlink/TV capability. The signal was not required to travel serially from Washington to Houston to California to Australia and then to the Moon.

### Other apparently instant Apollo exchanges

A particular clip that appears to contain zero delay should be timed against an unedited air-to-ground source before it is treated as evidence. Apollo transcripts and raw audio are available, but this appendix does not claim that every circulated clip has been inspected.

Current state:

`APOLLO_SURFACE_RADIO_DELAY_CONSISTENT_WITH_LUNAR_DISTANCE = SUPPORTED`

`EVERY_CIRCULATED_AUDIO_CLIP_VERIFIED = NO`

## 2. Why the ISS can appear nearly live

The ISS is only a few hundred kilometres from Earth. The pure propagation delay is milliseconds, not seconds. NASA describes ordinary ISS communications through TDRS and ground systems as occurring with **less than one second** delay.

Source:
- https://www.nasa.gov/missions/station/data-rate-increase-on-the-international-space-station-supports-future-exploration/

The often-quoted 5–15 second figures refer to particular payload-data or command-confirmation pipelines, not the unavoidable radio light-time of ordinary crew voice. NASA documentation gives about 5 seconds for payload-data downlink and about 10 seconds for a payload command with confirmation.

Source:
- NASA ISS Technology Demonstration guide.

A separate NASA UHD-video demonstration had 10+ seconds of video-processing/distribution latency. Again, that is a broadcast pipeline, not spacecraft distance.

Chris Hadfield's 2013 Music Monday event was officially described as live. A one-way musical lead can be followed by students on Earth even if their aggregate sound is not being returned to the ISS in phase. Tight two-way ensemble performance would be a different engineering problem.

Source:
- https://www.canada.ca/en/news/archive/2013/05/music-monday-2013.html

Current state:

`ISS_11_SECOND_CLAIM_AS_GENERAL_VOICE_LIGHT_TIME = UNSUPPORTED`

## 3. Armstrong's ladder: the apparent one-metre jump

The video impression is substantially correct about the distance but not about the destination.

NASA's Apollo 11 surface summary states that Armstrong had to make a roughly **three-foot jump from the bottom ladder rung down to the landing footpad**. The gap was a landing-gear contingency: a hard landing could compress the landing strut, changing the geometry. From the footpad, Armstrong had only a few inches to step to the lunar surface, and he probed the soil before stepping off.

Source:
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.summary.html

In lunar gravity, a 0.91 m drop produces roughly the same impact energy per kilogram as a 0.15 m drop on Earth. That does not make the manoeuvre risk-free. Suit mobility and visibility were real constraints. But the design did not require Armstrong to jump one metre blindly onto unknown lunar soil. It required him to descend to a broad footpad that was already supporting the spacecraft, then step from that platform to the surface.

Current state:

`LADDER_REQUIRED_ONE_METRE_BLIND_DROP_TO_UNKNOWN_SURFACE = UNSUPPORTED`

`LADDER_TO_FOOTPAD_GAP_WAS_LARGE_AND_DELiberate = SUPPORTED`

## 4. The Lunar Roving Vehicle: where was it?

The supplied high-resolution Lunar Module photograph is Apollo 14. Apollo 14 **did not carry a Lunar Roving Vehicle**. The LRV first flew on Apollo 15 and was used on Apollo 15, 16 and 17.

Sources:
- https://www.nasa.gov/history/50-years-ago-preparations-for-apollo-14-15-and-16/
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/rp-1994-1317.pdf

On the later J-missions, the rover was engineered to fold into the Lunar Module descent-stage bay. NASA's Apollo 15 mission report states that descent-stage quadrant I was modified to accommodate the LRV. Apollo 17 documentation describes the folded vehicle being released from the side of the LM by lanyard and cables and unfolding as it was lowered.

Sources:
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/a15/ap15mr.pdf
- https://www.nasa.gov/wp-content/uploads/static/apollo50th/pdf/A17_PressKit.pdf

The rover was about 3.1 m long when deployed, but folding was fundamental to the design.

Current state:

`ROVER_SHOULD_BE_VISIBLE_IN_SUPPLIED_APOLLO_14_IMAGE = UNSUPPORTED`

## 5. The ascent camera: robot, remote control, or later explanation?

The successful lunar-ascent footage was not shot by an autonomous robot and was not a camera attached to the LM landing gear.

For Apollo 15–17, the colour TV camera was mounted on the rover and could be commanded from Earth. A NASA contractor report describing the **Ground-Commanded Television Assembly** was published on 25 February 1972, during the Apollo program. It states that remote control from Earth was accomplished through Apollo command links.

Source:
- https://ntrs.nasa.gov/search.jsp?R=19730010465

Ed Fendell and the Mission Control INCO team controlled pan, tilt and zoom. Because the Moon signal took about 1.25 seconds each way, liftoff tracking commands were preplanned/timed rather than visually chased in real time.

The historical sequence also matters:

- Apollo 15: the camera had an elevation-clutch problem, so Fendell did not attempt to track the ascent.
- Apollo 16: remote tracking was attempted.
- Apollo 17: the final sequence was carefully preplanned and became the familiar shot, but even that tracking eventually lost the vehicle near the top of frame.

Sources:
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/WOTM/WOTM-TVLensBrushing.html
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/Shooting-Moonwalks.pdf

Current state:

`REMOTE_LUNAR_ASCENT_CAMERA_WAS_LATE_INVENTED_EXPLANATION = UNSUPPORTED`

`GROUND_COMMANDED_CAMERA_EXISTED_CONTEMPORANEOUSLY = SUPPORTED`

## 6. Why the Lunar Module looks flimsy

The supplied Apollo 14 photograph genuinely shows wrinkled, irregular, foil-like external surfaces. The visual observation is valid.

The engineering interpretation needs layer separation.

NASA's Lunar Module technical reference describes a load-bearing aluminium-alloy structure beneath an external thermal blanket and micrometeoroid shield. The blanket used at least 25 extremely thin layers of aluminized Mylar/H-film. The sheets were **hand crinkled intentionally** to provide venting paths and reduce thermal contact between layers. The blankets were held away from structural skin by standoffs.

Source:
- https://www.nasa.gov/wp-content/uploads/static/history/alsj/lm04_lunar_module_pplv1-17.pdf

Thus the visible wrinkles and irregular seams are largely not the primary pressure/load-bearing shell.

The gold/silver blanket should also not be oversold as heavy radiation armour. Its principal role was passive thermal control and micrometeoroid protection. Apollo radiation protection relied on spacecraft structure, exposure management, mission duration and monitoring. NASA's own biomedical review says radiation doses were modest during Apollo largely because **no major solar-particle event occurred**; a large event could have been dangerous or life-threatening.

Source:
- https://ntrs.nasa.gov/citations/19760005583

Current state:

`VISIBLE_WRINKLED_FOIL_IS_PRIMARY_STRUCTURAL_HULL = UNSUPPORTED`

`APOLLO_WAS_FULLY_PROTECTED_FROM_MAJOR_SOLAR_RADIATION_BY_GOLD_FOIL = UNSUPPORTED`

## 7. Why Hubble or an Earth telescope cannot simply photograph the lander

This question has a direct optics answer.

NASA notes that Hubble's 2.4 m mirror can resolve only about **80 m** at lunar distance. Apollo descent stages and rovers are only a few metres across.

Source:
- https://apod.nasa.gov/apod/ap020628.html

A beautiful high-resolution full-Moon photograph does not imply metre-scale resolving power. A camera can have millions of colour pixels while diffraction and distance make each resolvable patch on the lunar surface tens or hundreds of metres wide.

The angular size of a 4 m object at roughly 384,400 km is only about 2 milliarcseconds. That is beyond Hubble and beyond ordinary Earth-based seeing; even enormous ground telescopes face diffraction, atmospheric correction and contrast limits.

So the absence of a crisp Earth/Hubble photograph of a rover is **not anomalous**.

To resolve these objects usefully, a camera needs to be close to the Moon.

## 8. What lunar-orbiter images actually show

NASA's Lunar Reconnaissance Orbiter has imaged Apollo sites at roughly **0.5 m per pixel** in favourable passes. At that sampling:

- a 3.1 m rover spans only about six pixels in length;
- a Lunar Module descent stage spans only several pixels;
- an individual bootprint is smaller than one pixel.

Therefore claims that LRO directly photographs individual footprints would be wrong. What the images can show are compact objects, shadows, rover tracks and broader **disturbed-regolith paths**, which may be described colloquially as astronaut trails.

Source:
- https://svs.gsfc.nasa.gov/4302/

This is genuine imagery, but OGI records an independence limitation:

`NASA_APOLLO_CLAIM + NASA_LRO_IMAGE` is not two fully independent institutional sources.

The orbital imagery is a useful consistency check, not a standalone independent proof that people rather than robotic equipment produced the site.

## 9. The independent-image question is stronger than the usual debate admits

Japan's KAGUYA/SELENE mission had about 10 m terrain-camera resolution, too coarse to resolve a rover or LM. JAXA nevertheless reported an Apollo 15 surface-reflectance `halo` consistent with descent-engine plume effects and reconstructed terrain matching Apollo 15 photography.

Source:
- https://global.jaxa.jp/press/2008/05/20080520_kaguya_e.html

India's Chandrayaan-2 OHRC is much more interesting. ISRO reports approximately **0.25–0.32 m ground resolution**, and its published science objectives explicitly include imaging `anthropogenic sites - landing sites (Apollo, Luna etc)`.

Sources:
- https://www.isro.gov.in/media_isro/pdf/science/science_results_from_ch.pdf
- https://www.isro.gov.in/FAQ_Chandrayaan2.html

In this OGI run, however, an official ISRO-released high-resolution Apollo-site OHRC frame was **not located**.

That becomes explicit research debt:

`INDEPENDENT_SUB_METER_APOLLO_SITE_IMAGE = NOT_RETRIEVED`

This is a better question than demanding Hubble do something optics forbids. A low-orbit non-NASA camera with ~25 cm sampling is physically capable of providing an unusually useful independent check, and OGI should pursue the public OHRC archive rather than wave the question away.

## 10. Artemis II images: why they do not look like mapping imagery

The supplied Artemis II image is 1920 × 1280 pixels and is a broad lunar-horizon view. Artemis II did not enter low lunar orbit. NASA gives closest approach as about **4,067 miles / 6,545 km above the lunar surface**.

NASA also states that the crew used handheld cameras, including an 80–400 mm lens, for the lunar flyby. The close-up Vavilov image was taken at 400 mm.

Sources:
- https://www.nasa.gov/news-release/nasas-artemis-ii-crew-eclipses-record-for-farthest-human-spaceflight/
- https://www.nasa.gov/news-release/nasas-artemis-ii-crew-beams-official-moon-flyby-photos-to-earth/

That geometry is excellent for regional lunar photography but wholly unsuitable for resolving 3–4 m Apollo hardware. Artemis II imagery should therefore not be presented as a landing-site verification experiment.

Equally, a broad Artemis photograph by itself is not strong proof of crew location unless its provenance is tied to mission telemetry, spacecraft records and independent tracking. OGI should not ask the photograph to carry more than it can.

## 11. Evidence that is more independent of NASA's later imagery

### Independent radio tracking

Britain's Jodrell Bank records that it tracked Apollo 11 and followed the descent signal of Eagle while also monitoring the Soviet Luna 15 mission.

Source:
- https://www.jodrellbank.net/explore/heritage/the-story-of-jodrell-bank/

This strongly supports that an Apollo transmitter/spacecraft associated with the mission was at lunar distance and undergoing the reported descent sequence. It does not alone prove two humans were standing outside it.

### Retroreflectors

Apollo 11, 14 and 15 reflector arrays are still ranged by observatories. Apache Point publishes current ranging performance to the separate Apollo and Lunokhod arrays.

Sources:
- https://www.apo.nmsu.edu/mainpage/apollo/apollolrrr/
- https://www.apo.nmsu.edu/mainpage/apollo/highlights/

This establishes equipment at the reported coordinates. Because Soviet robotic rovers also deployed reflectors, a reflector does not logically require human emplacement.

### Returned samples

The Apollo program's curated sample corpus totals about **381.7 kg / 2,196 samples**, including deep cores and geographically differentiated collections. Apollo 15 alone returned 77 kg from 370 samples and a 2.4 m core; Apollo 17 returned 110.5 kg from 741 samples and a 3 m core.

Sources:
- https://www.lpi.usra.edu/captem/lsac/alltonLunarToolCatalog.pdf
- https://www.lpi.usra.edu/lunar/missions/apollo/apollo_15/samples/
- https://www.lpi.usra.edu/lunar/missions/apollo/apollo_17/samples/

Robotic sample return is demonstrably possible, so `lunar samples exist` is not logically equivalent to `humans collected them`. But a staged model must explain the mass, diversity, deep cores, six-site field geology, contemporaneous sample documentation and decades of international laboratory work without simply assuming an undisclosed robotic program capable of reproducing all of it.

### Surface experiment locations

Published geodetic work combines laser-ranging coordinates and VLBI measurements of ALSEP transmissions to locate Apollo surface packages.

Source:
- M. E. Davies & T. R. Colvin, JGR 2000: https://agupubs.onlinelibrary.wiley.com/doi/10.1029/1999JE001165

Again, this is hardware-on-Moon evidence, not by itself human-on-Moon evidence.

## 12. The alternative model has to be specified

`THE MOON LANDING WAS FAKE` is not one hypothesis.

Possible alternatives include:

1. the crew remained in Earth orbit while TV was staged;
2. unmanned Apollo-derived vehicles secretly landed equipment while crew imagery was staged;
3. lunar samples were obtained robotically and attributed to crews;
4. tracking records were spoofed;
5. later orbital imagery or scientific records were falsified or institutionally coordinated.

Each version predicts a different evidence field.

OGI therefore refuses two shortcuts:

- `NASA says it happened -> therefore true`
- `one anomaly remains -> therefore staged`

The correct comparison is joint explanatory burden.

A crewed-landing model must explain the anomalies and engineering record.

A staged model must explain independent tracking, lunar hardware, reflectors, sample mass and diversity, surface-experiment coordinates, later site geometry and decades of external scientific use while supplying evidence for the additional hidden systems its account requires.

Logical non-falsifiability is not evidentiary parity. A model that can absorb every contrary observation by adding another unseen conspiracy becomes harder to falsify but does not thereby become better warranted.

## 13. Current finding on the Apollo proposition

### Claim A — Apollo communications are inconsistent with lunar radio light-time.
`UNSUPPORTED ON EVIDENCE INSPECTED`

The documented 2.6 s surface echo is precisely in the expected range. Specific edited/circulated clips remain individually testable.

### Claim B — No physical equipment associated with Apollo is measurably present on the Moon.
`UNSUPPORTED`

Retroreflectors, ALSEP locations and orbital site imagery establish hardware/surface changes at expected locations.

### Claim C — Those hardware observations alone prove humans emplaced the equipment.
`UNSUPPORTED`

Robotic emplacement is physically possible in principle.

### Claim D — No institution independent of NASA produced relevant lunar evidence.
`UNSUPPORTED`

Jodrell Bank tracking and JAXA's Apollo 15 site observation provide independent evidence classes. International laser-ranging observatories also measure lunar reflectors.

### Claim E — A crisp Earth- or Hubble-based photograph should be physically obtainable.
`UNSUPPORTED`

Angular resolution is inadequate for metre-scale hardware at lunar distance.

### Claim F — A useful independent sub-metre orbital image is physically possible.
`SUPPORTED`

ISRO's OHRC has ~0.25–0.32 m ground sampling and explicitly lists Apollo/Luna landing sites among anthropogenic science targets. An official Apollo-site frame was not retrieved in this run.

### Claim G — The Apollo crewed lunar landings are presently supported by a convergent evidence field.
`SUPPORTED / HIGH CONFIDENCE`

No single evidence item inspected is a self-sufficient proof of humans standing on the surface. Taken jointly, however, the conventional crewed-landing model currently explains the inspected evidence with substantially fewer unsupported auxiliary assumptions than the staged alternatives examined at this level.

This is a **current warranted state**, not an immunity badge. The case remains reopenable.

## 14. The 54-year gap returns only after that finding

Once the crewed-landing proposition reaches `SUPPORTED / HIGH CONFIDENCE`, the original anomaly re-enters legitimately:

> Why was a repeatedly demonstrated crewed lunar landing capability not reproduced after December 1972 for more than five decades?

Historical shutdown of Saturn V production, Apollo cancellations, budgets and changed political objectives are relevant variables. They are not, by themselves, a complete explanation of why successor technology did not reproduce the capability sooner.

OGI therefore records:

`POST_1972_CREWED_LUNAR_REPLICATION_GAP = REAL_ANOMALY / EXPLANATION_INCOMPLETE`

The gap is **not evidence sufficient to overturn Apollo by itself**. But neither should it be dissolved into the phrase `the program ended` and forgotten.

A proper continuation audit must compare:

- technological inheritance and loss;
- economic/political reward after firstness;
- risk tolerance;
- human-spaceflight priorities;
- why other nations did not reproduce the feat;
- whether claimed capability should have become cheaper/easier with later technology;
- and current Artemis/Chinese program evidence.

That becomes a separate second-stage inquiry after the landing proposition.

## 15. OGI findings from the run

### `EXPLANATION_PRELOAD`

The first pass tried to explain the gap before adjudicating Apollo. The human researcher caught it before merge.

### `INDEPENDENCE_COMPRESSION`

> Multiple artifacts from one institutional pipeline must not be counted as though they were independent confirmations.

NASA photographs + NASA telemetry + NASA LRO imagery are multiple evidence types, but institutional independence must be scored separately.

### `ALTERNATIVE_MODEL_BURDEN`

> An alternative explanation must account for the full joint evidence field, not merely reproduce one anomaly.

### `CAPABILITY_EQUIVOCATION`

> Ending one production architecture is not the same proposition as losing the underlying technological capability.

All four remain candidate architectural lessons pending cross-case recurrence/adjudication.

## 16. Plain-language OGI answer

OGI's current answer is neither `NASA said so` nor `the strange bits prove a hoax`.

It is:

> **Several of the strongest popular anomalies inspected here have ordinary, testable engineering explanations: the expected lunar radio delay is present in the raw record; Armstrong dropped to the LM footpad rather than blindly one metre onto the ground; the ascent camera was a contemporaneously documented Earth-commanded rover camera; the apparently flimsy outer LM surfaces were intentionally crinkled thermal/micrometeoroid blankets over a structural frame; Apollo 14 carried no rover; and Earth/Hubble telescopes simply lack the angular resolution to photograph metre-scale hardware on the Moon.**
>
> **The stronger evidentiary questions are about independence. LRO site images are useful but NASA is not independent of NASA. Jodrell Bank, lunar laser ranging and JAXA add independent evidence. ISRO's sub-metre OHRC is particularly valuable because it is physically capable of imaging Apollo-scale hardware, yet an official Apollo-site OHRC frame was not retrieved in this run. That should remain research debt, not be waved away.**
>
> **On the evidence inspected so far, the crewed Apollo landing model is supported with high confidence because the joint evidence field is substantially easier to explain under actual crewed landings than under staged alternatives, which require additional unshown mechanisms. The 54-year failure to repeat a crewed landing remains a legitimate anomaly to investigate separately.**
