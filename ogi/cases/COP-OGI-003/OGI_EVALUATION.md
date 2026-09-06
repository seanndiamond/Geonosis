# COP-OGI-003 — OGI Evaluation

**Run type:** manual application of OGI v0.3 specification  
**Overall OGI result:** `MIXED`

## What OGI did well

### T-22 Outcome Drift Resistance — PASS
The case did not begin with a desired moral verdict such as "reckless passenger" or "deceptive company." It retained `desired_finding = NONE`.

### Field before actor blame — PASS
The analysis reconstructed engineering, organizational, regulatory, marketing, social and informational conditions before assigning individual decision responsibility.

### Individual agency preservation — PASS
OGI did not erase the fact that the waiver explicitly described an experimental, uncertified and potentially fatal activity.

### Claim boundary control — PASS
The case distinguished:
- risk disclosure;
- actual engineering state;
- passenger knowledge;
- passenger private reasoning;
- organizational causation;
- legal responsibility.

### Contrary evidence retention — PASS
The explicit waiver is contrary to a simple "passengers were told it was safe" narrative and is preserved prominently.

### Authority / proxy separation — PASS
Founder participation, prior successful dives, expert presence, professional expedition framing, price and safety procedures were treated as possible trust proxies rather than independent engineering proof.

### Lay question preservation — PASS
The originating question "How did the mistake arrive?" was not rewritten into "Why was the passenger irrational?"

## Warnings

### Passenger-specific state — WARN
The first run does not contain enough direct contemporaneous material to reconstruct any named deceased passenger's exact decision process.

### Proxy weighting — WARN
`TRUST_PROXY_STACKING` is a plausible field explanation, but the relative influence of each proxy on any particular passenger is not established.

### Hindsight bias — WARN
Because the catastrophic outcome is known, OGI must resist treating all pre-incident signals as equally obvious. The case therefore distinguishes information publicly available before the dive from technical facts established only after investigation.

## Not yet executable

The v0.3 Shared Coherence Kernel, automatic Claim-Type Controller and Adjudicated Integration Gate are not yet an implemented runtime. This case demonstrates manual method compliance, not automated enforcement.

## Candidate architecture lesson

### `TRUST_PROXY_STACKING`

Multiple legitimacy signals may collectively impersonate a missing primary warrant.

Example:

`successful prior missions + founder confidence + expert participation + mission language + sophisticated operations + expensive/exclusive access`

may be cognitively compressed into:

`the vehicle has been independently shown safe`

when that proposition is not actually established.

Do **not** promote this candidate into the formal OGI failure taxonomy until recurrence is demonstrated in additional independent cases.

## Current OGI finding

`MIXED`

The inquiry produced a more coherent decision-field explanation than either pure victim blame or pure operator blame, but several new v0.3 controls remain manually applied rather than executable, and passenger-specific cognitive inference remains intentionally limited.
