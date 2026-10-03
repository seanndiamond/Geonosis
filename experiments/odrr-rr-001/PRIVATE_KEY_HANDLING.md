# Private Key Handling — ODRR-RR-001

The local full target-pack ZIP contains the private neutral-ID mapping and must not be shared with participants or blinded scorers.

A separate observer-only ZIP contains only neutralized stimulus files and an observer manifest. It is still **not participant-ready** because matched controls have not yet been added.

Before confirmatory collection:
1. retain the private key outside the participant-facing repository/interface;
2. verify its SHA-256 against `BLIND_KEY_SHA256.txt`;
3. combine target and matched-control source families under a new final blind key;
4. commit the final blind-key digest before recruitment;
5. preserve this target-pack digest as historical lineage rather than replacing it silently.
