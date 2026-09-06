# Contributing to OGI / Oggy

OGI is developed in public. Contributions are welcome from individuals, research groups, companies, independent developers, critics, and people with no technical background at all.

The governing development cycle is:

> **INHERIT → EXPLORE → RETURN → SHOW → ADJUDICATE → INTEGRATE**

Git branches and forks are treated as experimental travellers. The `main` branch represents the current reference state and is changed only through inspectable review.

## No coding required

If you have a real-world problem or observation but do not write software, start with [`START_HERE_NO_CODE.md`](START_HERE_NO_CODE.md).

You can contribute by opening a GitHub issue and choosing **OGI: Real-world problem / question**. Describe what is happening in ordinary language. You do not need to understand forks, branches, tests, schemas, or pull requests.

A useful contribution may be as simple as:

> **This keeps going wrong. Here is what people are told to do. Here is what actually gets rewarded. Here is what happens instead.**

Unknown is a valid state. If you do not know an answer, say **I don't know**.

## Technical contributors: start here

Read:

1. `README.md`
2. `SPEC_v0.2.md`
3. `FIELD_AUDIT.md`
4. `RETURN_CONTROLLER.md`
5. `benchmarks/RETURN_FAIL_TESTS.md`
6. `GOVERNANCE.md`

Then fork the repository or create a branch.

## Contribution lanes

### 1. REAL-WORLD PROBLEM / QUESTION
Use when you have an observation, workplace problem, animal-behaviour case, organizational failure, incentive problem, or other situation that may help test OGI.

No code is required.

Include as much as you can of:
- what is happening;
- who or what is being blamed;
- what the stated objective is;
- what actually gets rewarded or punished;
- what surrounds the behaviour;
- what a better outcome would look like;
- what would change your mind.

### 2. BUG / FAILURE
Use when the reference implementation, benchmark, schema, or architecture behaves incorrectly.

Include:
- component affected;
- minimal reproduction;
- expected behaviour;
- observed behaviour;
- test or evidence where possible.

### 3. REPLICATION
Use when you implement or test OGI elsewhere.

Include:
- implementation environment;
- model(s) and agent framework(s);
- exact OGI component tested;
- benchmark procedure;
- results, including failures;
- deviations from the reference architecture.

### 4. ARCHITECTURE CHALLENGE
Use when you think a current OGI principle or component is wrong, incomplete, or unnecessary.

Include:
- exact target claim or component;
- strongest counterexample or alternative;
- evidence;
- predicted consequence if your challenge is correct;
- what would make you withdraw or revise the challenge.

### 5. NEW PROPOSAL
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

The best contribution may be a successful implementation, a failed replication, a clean demonstration that an OGI assumption is wrong, or a real-world observation that gives us a better problem to solve.

**The objective is not to protect OGI from change. It is to make change inspectable.**
