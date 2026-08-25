#!/usr/bin/env python3
"""Smallest viable executable control layer for OGI Sandbox v0.2.

Standard-library only. This is not a language model. It is a Court gate around
model outputs: prompt provenance, stage transition control, semantic quarantine,
and fail-closed reconciliation.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
import json
import re
from typing import List, Optional


class Stage(str, Enum):
    NONE = "NONE"
    CITED = "CITED"
    LOCATED = "LOCATED"
    RETRIEVED = "RETRIEVED"
    INSPECTED = "INSPECTED"
    MAPPED = "MAPPED"
    DERIVED = "DERIVED"
    REPRODUCED = "REPRODUCED"
    CHALLENGED = "CHALLENGED"
    SURVIVED = "SURVIVED"


STAGE_ORDER = [
    Stage.NONE, Stage.CITED, Stage.LOCATED, Stage.RETRIEVED, Stage.INSPECTED,
    Stage.MAPPED, Stage.DERIVED, Stage.REPRODUCED, Stage.CHALLENGED, Stage.SURVIVED
]


class CourtState(str, Enum):
    SOURCE_CLAIM = "SOURCE_CLAIM"
    NOT_DERIVED = "NOT_DERIVED"
    INCONCLUSIVE = "INCONCLUSIVE"
    CONTESTED = "CONTESTED"
    DERIVED = "DERIVED"
    SURVIVED = "SURVIVED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"


CONCLUSION_FIRST = [
    r"\bprove\b",
    r"\bshow (?:how|that|why)\b",
    r"\bdemonstrate\b",
    r"\bdefend\b",
    r"\brefute\b",
    r"\bexonerat(?:e|ed|ion)\b",
]


@dataclass
class PromptEnvelope:
    envelope_id: str
    initiating_prompt: str
    assigned_role: str
    desired_conclusion_supplied: bool = False
    desired_conclusion: Optional[str] = None
    advocate_mode: bool = False
    evidence_supplied: List[str] = field(default_factory=list)
    output_claims: List[str] = field(default_factory=list)
    highest_stage_earned: Stage = Stage.NONE
    missing_bridges: List[str] = field(default_factory=list)
    tripwires_triggered: List[str] = field(default_factory=list)
    corrections: List[str] = field(default_factory=list)
    court_state: CourtState = CourtState.UNKNOWN


class CourtGate:
    @staticmethod
    def detect_advocacy(prompt: str) -> bool:
        return any(re.search(p, prompt, flags=re.I) for p in CONCLUSION_FIRST)

    @staticmethod
    def stage_index(stage: Stage) -> int:
        return STAGE_ORDER.index(stage)

    @classmethod
    def can_promote(cls, current: Stage, target: Stage, explicit_bridge: bool) -> bool:
        if cls.stage_index(target) <= cls.stage_index(current):
            return True
        if cls.stage_index(target) == cls.stage_index(current) + 1:
            return explicit_bridge
        return False

    @classmethod
    def reconcile(cls, env: PromptEnvelope, requested_stage: Stage, explicit_bridge: bool) -> PromptEnvelope:
        if env.advocate_mode:
            env.tripwires_triggered.append("AT-05 conclusion-first contamination")
        if cls.can_promote(env.highest_stage_earned, requested_stage, explicit_bridge):
            env.highest_stage_earned = requested_stage
        else:
            env.missing_bridges.append(
                f"Illegal or unsupported stage promotion: {env.highest_stage_earned.value} -> {requested_stage.value}"
            )
            env.tripwires_triggered.append("hard-stage rule")

        if cls.stage_index(env.highest_stage_earned) >= cls.stage_index(Stage.SURVIVED):
            env.court_state = CourtState.SURVIVED
        elif cls.stage_index(env.highest_stage_earned) >= cls.stage_index(Stage.DERIVED):
            env.court_state = CourtState.DERIVED
        elif env.missing_bridges:
            env.court_state = CourtState.NOT_DERIVED
        elif env.output_claims:
            env.court_state = CourtState.SOURCE_CLAIM
        else:
            env.court_state = CourtState.UNKNOWN
        return env


def demo() -> None:
    prompt = "Show how the claimant is correct and produce a decisive report."
    env = PromptEnvelope(
        envelope_id="DEMO-001",
        initiating_prompt=prompt,
        assigned_role="ADVOCATE",
        desired_conclusion_supplied=True,
        desired_conclusion="claimant is correct",
        advocate_mode=CourtGate.detect_advocacy(prompt),
        evidence_supplied=["source report retrieved"],
        output_claims=["claimant is correct"],
        highest_stage_earned=Stage.RETRIEVED,
    )

    # Deliberately illegal jump: RETRIEVED -> DERIVED with no mapping/derivation bridge.
    CourtGate.reconcile(env, Stage.DERIVED, explicit_bridge=False)
    print(json.dumps(asdict(env), indent=2, default=lambda x: x.value if isinstance(x, Enum) else str(x)))


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo()
    else:
        print("OGI Sandbox v0.2 loaded. Run with: python ogi_sandbox_v0_2.py demo")
