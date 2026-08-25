from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from hashlib import sha256
from typing import Optional


@dataclass(frozen=True)
class ResearchEvent:
    event_id: str
    type: str
    claim_id: str
    timestamp: str
    query: Optional[str] = None
    source_url: Optional[str] = None
    source_title: Optional[str] = None
    source_type: Optional[str] = None
    content_sha256: Optional[str] = None
    outcome: Optional[str] = None
    note: Optional[str] = None

    def to_dict(self):
        return asdict(self)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def hash_bytes(data: bytes) -> str:
    return sha256(data).hexdigest()


def classify_research_result(*, has_mention: bool, has_catalogue_identity: bool,
                             bytes_retrieved: bool, authenticated: bool,
                             inspected: bool) -> str:
    """Return the maximum *candidate* stage supported by a research result.

    This never changes Court state by itself. A separate admissibility event must
    explicitly earn the stage.
    """
    if inspected and authenticated:
        return "INSPECTED"
    if bytes_retrieved:
        return "RETRIEVED"
    if has_catalogue_identity:
        return "LOCATED"
    if has_mention:
        return "CITED"
    return "NO_STAGE"


def institutional_limitation_claim(text: str) -> dict:
    """Represent an archival/access explanation as a claim requiring evidence."""
    return {
        "type": "INSTITUTIONAL_LIMITATION_CLAIM",
        "text": text,
        "status": "UNVERIFIED",
        "rule": "NO_PRESUMPTIVE_INSTITUTIONAL_EXCUSE",
    }
