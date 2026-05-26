from typing import List, Literal
from enum import Enum
from pydantic import BaseModel, Field


class EmotionTone(str, Enum):
    JOY = "joy"
    GRIEF = "grief"
    LOVE = "love"
    NOSTALGIA = "nostalgia"
    CALM = "calm"
    CELEBRATION = "celebration"
    MELANCHOLY = "melancholy"
    REVERENCE = "reverence"


class EmotionInterpretation(BaseModel):
    tone: EmotionTone
    intensity: float = Field(..., ge=0.0, le=1.0)
    keywords: List[str]
    summary: str


class BlueprintStatus(str, Enum):
    DRAFT = "draft"
    SAVED = "saved"
    ARCHIVED = "archived"


class Blueprint(BaseModel):
    id: str
    schema_version: Literal["EC_CANON_V1"]
    name: str
    status: BlueprintStatus
    emotion: EmotionInterpretation
    created_at: str  # ISO 8601
    updated_at: str  # ISO 8601


class BlueprintCreateInput(BaseModel):
    schema_version: Literal["EC_CANON_V1"]
    name: str
    status: BlueprintStatus = BlueprintStatus.DRAFT
    emotion: EmotionInterpretation
