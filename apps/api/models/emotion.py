"""Pydantic models for the Emotion Engine.

Spec reference: 06_EMOTION_ENGINE_SPEC.md
"""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class EmotionClassifyInput(BaseModel):
    text: str = Field(..., min_length=3, description="Freeform memory, mood, or concept text.")
    occasion: Optional[str] = None
    color_preferences: Optional[str] = None


class EmotionOutput(BaseModel):
    """Structured emotion interpretation returned by the Emotion Engine."""

    primary_tone: str
    secondary_tones: List[str]
    valence: float = Field(..., ge=-1.0, le=1.0)
    arousal: float = Field(..., ge=-1.0, le=1.0)
    quadrant: str  # "Cozy & Calm" | "Bright & Joyful" | "Deep & Contemplative" | "Bold & Expressive"
    emotion_vector: Dict[str, float]  # e.g. {"calm": 0.8, "nostalgia": 0.7, "joy": 0.2}
    palette_direction: str
    density_bias: str
    movement_bias: str
    formula_candidates: List[str]  # e.g. ["crescent_asymmetrical", "arc_loose"]
    narrative_summary: str
