# Provenance Standard

A Geonosis claim should be reproducible from the source outward. This directory defines the minimum source chain.

## Minimum source record

Every evidence item should carry, where applicable:

- `source_id`
- original filename or catalogue identifier
- source type: artefact / terrain / photograph / satellite imagery / scan / document / biological observation / measurement / testimony / dataset
- original creator or custodian if known
- source URL or repository if public
- access or capture date
- site / artefact / corpus
- geographic coordinates where ethically appropriate
- camera height, altitude, zoom, orientation or scale where relevant
- page / plate / panel / sign / coordinate location
- raw or transformed status
- transformation log
- rights / licence status
- checksum when a file is deposited
- archive version

## Transformation log

Any operation capable of changing what a viewer sees should be recorded. Examples:

- crop
- rotation
- perspective correction
- contrast or exposure adjustment
- colour remapping
- sharpening
- segmentation
- edge detection
- overlay
- grid
- annotation
- compositing
- AI enhancement or generation

A transformation is not automatically disqualifying. An undisclosed transformation is.

## Reading record

Keep separate fields for:

1. **direct observation**
2. **inherited designation**
3. **operator interpretation**
4. **grammar hypothesis**
5. **alternative models**
6. **prediction**
7. **failure conditions**
8. **independent reproduction result**
9. **external validation**
10. **speculative extension**

Do not write one paragraph that quietly blends all ten.

## Provenance hierarchy

When sources conflict, prefer:

1. original source / first-party record;
2. preserved contemporary copy;
3. authoritative catalogue or archive;
4. peer-reviewed or scholarly secondary treatment;
5. later institutional summary;
6. search-engine index, aggregator or AI summary.

This hierarchy is not absolute. A first-party claim can be wrong. The point is that a derivative index must not silently outrank the thing it claims to index.

## Correction rule

Corrections are additive:

- retain earlier record;
- create correction record;
- state date and reason;
- link the evidence that caused the correction;
- mark current preferred state;
- never rewrite history merely to make the archive look prescient.

See `examples/0001-researchgate-profile-count.md` for the first deliberately mundane worked example.
