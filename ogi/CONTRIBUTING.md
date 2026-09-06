# Contributing to OGI / Oggy

OGI is developed in public. Contributions are welcome from individuals, research groups, companies, independent developers, and critics.

The governing development cycle is:

> **INHERIT → EXPLORE → RETURN → SHOW → ADJUDICATE → INTEGRATE**

Git branches and forks are treated as experimental travellers. The `main` branch represents the current reference state and is changed only through inspectable review.

## Start here

Read:

1. `README.md`
2. `SPEC_v0.2.md`
3. `FIELD_AUDIT.md`
4. `RETURN_CONTROLLER.md`
5. `benchmarks/RETURN_FAIL_TESTS.md`
6. `GOVERNANCE.md`

Then fork the repository or create a branch.

## Contribution lanes

### 1. BUG / FAILURE
Use when the reference implementation, benchmark, schema, or architecture behaves incorrectly.

Include:
- component affected;
- minimal reproduction;
- expected behaviour;
- observed behaviour;
- test or evidence where possible.

### 2. REPLICATION
Use when you implement or test OGI elsewhere.

Include:
- implementation environment;
- model(s) and agent framework(s);
- exact OGI component tested;
- benchmark procedure;
- results, including failures;
- deviations from the reference architecture.

### 3. ARCHITECTURE CHALLENGE
Use when you think a current OGI principle or component is wrong, incomplete, or unnecessary.

Include:
- exact target claim or component;
- strongest counterexample or alternative;
- evidence;
- predicted consequence if your challenge is correct;
- what would make you withdraw or revise the challenge.

### 4. NEW PROPOSAL
Use for new controllers, schemas, tests, integrations, safety mechanisms, memory systems, or coherence methods.

Include:
- problem addressed;
- proposed mechanism;
- why existing OGI components are insufficient;
- tests;
- failure conditions;
- compatibility or conflict with current state.

## Pull requests

A pull request should state:

- **What changed?**
- **Why did it change?**
- **What evidence or failure forced the change?**
- **Which current OGI assumption is affected?**
- **What tests pass?**
- **What tests fail?**
- **What would falsify the proposed improvement?**
- **Does this supersede an earlier rule, or merely extend it?**

Do not silently remove failed ideas or superseded states. Preserve lineage.

## Outcome states

A contribution may be marked:

- `MERGE`
- `HOLD`
- `REJECT`
- `NEEDS_EVIDENCE`
- `EXPERIMENTAL`
- `SUPERSEDED`

Rejection is not deletion. Useful failed proposals remain part of the research history.

## Court of Provenance

Substantive architecture disputes may be referred to the repository's canonical `court-of-provenance/` subsystem.

The Court asks for derivation, evidence, alternatives, failure conditions, and current state. It does not award authority points for conventionality, novelty, affiliation, or confidence.

## Tone

Attack the mechanism, derivation, benchmark, or evidence. Do not attack the contributor.

The best contribution may be a successful implementation, a failed replication, or a clean demonstration that an OGI assumption is wrong.

**The objective is not to protect OGI from change. It is to make change inspectable.**