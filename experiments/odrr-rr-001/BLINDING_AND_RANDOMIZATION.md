# Blinding and Randomization — ODRR-RR-001

## Threat model

The original pilot involved investigators who knew the developing hypothesis and, in several cases, knew the sources. The confirmatory design therefore treats expectancy, source familiarity, sequence priming and transformation mixing as explicit threats.

## Blind key

Create a private CSV with:
- neutral stimulus ID;
- true source ID;
- condition (`TARGET` or `CONTROL`);
- pair ID;
- source class;
- source provenance pointer.

Before collection:

```bash
python scripts/seal_blind_key.py private_blind_key.csv BLIND_KEY_SHA256.txt
```

Commit `BLIND_KEY_SHA256.txt`.

Do **not** commit the private key before data lock.

After collection closes and the anonymized raw dataset plus analysis script are frozen:
1. commit the private key;
2. verify that its SHA-256 matches the precommitted digest;
3. unblind;
4. run the confirmatory analysis exactly once before exploratory additions.

## Participant-facing identifiers

Participants see identifiers such as `S013`, not `GIZA`, `REKHMIRE`, `TARGET`, `CONTROL`, `CUNEIFORM` or any interpretive label.

## Randomization

A deterministic per-participant seed is generated from:
- master seed `20260907`;
- pseudonymous participant token.

Randomization covers:
- source order;
- initial orientation;
- remaining orientation order.

The same algorithm is used for target and control sources.

## Separation of roles

Preferred:
- **stimulus curator** knows source identity and creates the blind key;
- **participant administrator** does not know condition mapping;
- **analyst** works on blinded labels until data lock;
- **key holder** reveals mapping after lock.

Where staffing does not allow full role separation, the limitation is recorded and the blind-key hash still prevents post-hoc relabeling.

## Blinding failure

At session end, participants record:
- whether they recognized any source;
- what they thought the study was testing;
- prior familiarity with Geonosis.

Recognition is reported, not quietly discarded.
