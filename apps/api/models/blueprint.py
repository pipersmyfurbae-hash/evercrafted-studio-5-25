"""Pydantic models for the EC_CANON_V1 blueprint schema.

Spec references:
  - 05_EC_CANON_V1_BLUEPRINT_SCHEMA.md
  - 09_PLACEMENT_ENGINE_SPEC.md
"""

from typing import Any, Dict, List, Literal, Optional
from enum import Enum
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Shared enums
# ---------------------------------------------------------------------------


class EmotionTone(str, Enum):
    JOY = "joy"
    GRIEF = "grief"
    LOVE = "love"
    NOSTALGIA = "nostalgia"
    CALM = "calm"
    CELEBRATION = "celebration"
    MELANCHOLY = "melancholy"
    REVERENCE = "reverence"


class BlueprintStatus(str, Enum):
    DRAFT = "draft"
    SAVED = "saved"
    ARCHIVED = "archived"


class PlacementRole(str, Enum):
    FOCAL = "focal"
    SECONDARY = "secondary"
    FILLER = "filler"
    ACCENT = "accent"
    GREENERY = "greenery"


# ---------------------------------------------------------------------------
# EC_CANON_V1 sub-schemas
# ---------------------------------------------------------------------------


class EmotionInterpretation(BaseModel):
    """Simplified emotion block (Sprint 1 compatible). Extended fields optional."""

    tone: EmotionTone
    intensity: float = Field(..., ge=0.0, le=1.0)
    keywords: List[str]
    summary: str
    # Sprint 3 extended fields (populated by Emotion Engine)
    primary_tone: Optional[str] = None
    secondary_tones: Optional[List[str]] = None
    valence: Optional[float] = None        # -1.0 to 1.0
    arousal: Optional[float] = None        # -1.0 to 1.0
    quadrant: Optional[str] = None
    emotion_vector: Optional[Dict[str, float]] = None
    palette_direction: Optional[str] = None
    density_bias: Optional[str] = None
    movement_bias: Optional[str] = None
    narrative_summary: Optional[str] = None


class BaseSpec(BaseModel):
    """Physical base (wreath form + dimensions)."""

    form_factor: str = "circular"
    diameter_in: float = 24.0
    base_type: str = "grapevine"
    base_visibility_percent: float = 22.0


class FormulaSpec(BaseModel):
    """Structural composition archetype."""

    formula_id: str
    formula_name: str
    arc_start_deg: float
    arc_end_deg: float
    negative_space_deg: float
    flow_direction: str = "counterclockwise"


class WreathDNA(BaseModel):
    """Procedural trait set — drives density, rhythm, and negative space."""

    cluster_count: int = 3
    density_profile: float = Field(0.5, ge=0.0, le=1.0)
    cluster_spread_deg: float = 65.0
    greenery_direction: str = "outward"
    silhouette_bias: str = "organic"
    focal_ratio: float = 0.22
    silence_arc: float = 45.0
    style_signature: str = "editorial"


class PlacementEntry(BaseModel):
    """Single element placement — deterministic polar coordinates."""

    placement_id: str
    material_id: Optional[str] = None
    role: PlacementRole
    layer: str
    theta_deg: float = Field(..., ge=0.0, le=360.0)
    clock_position: Optional[str] = None
    radius_norm: float = Field(..., ge=0.0, le=1.0)
    radius_in: Optional[float] = None
    rotation_deg: float = 0.0
    scale: float = 1.0
    stem_direction: Optional[str] = None
    z_index: int = 0
    cluster_id: Optional[str] = None


# ---------------------------------------------------------------------------
# Top-level Blueprint
# ---------------------------------------------------------------------------


class Blueprint(BaseModel):
    """Full EC_CANON_V1 blueprint object.

    All fields beyond Sprint 1 basics are Optional — they are filled
    progressively as each engine stage runs.
    """

    id: str
    schema_version: Literal["EC_CANON_V1"]
    name: str
    status: BlueprintStatus
    emotion: EmotionInterpretation
    created_at: str  # ISO 8601
    updated_at: str  # ISO 8601

    # Extended EC_CANON_V1 fields (optional until respective engines run)
    base: Optional[BaseSpec] = None
    formula: Optional[FormulaSpec] = None
    dna: Optional[WreathDNA] = None
    zones: Optional[List[Dict[str, Any]]] = None
    anchors: Optional[List[Dict[str, Any]]] = None
    placements: Optional[List[PlacementEntry]] = None
    materials: Optional[List[Dict[str, Any]]] = None
    visualization: Optional[Dict[str, Any]] = None
    manufacturing: Optional[Dict[str, Any]] = None
    commerce: Optional[Dict[str, Any]] = None
    scores: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None


class BlueprintCreateInput(BaseModel):
    schema_version: Literal["EC_CANON_V1"]
    name: str
    status: BlueprintStatus = BlueprintStatus.DRAFT
    emotion: EmotionInterpretation
    # Optional extended fields can be supplied at creation time
    base: Optional[BaseSpec] = None
    formula: Optional[FormulaSpec] = None
    dna: Optional[WreathDNA] = None


class BlueprintPatchInput(BaseModel):
    """Partial update — only supplied fields are updated."""

    name: Optional[str] = None
    status: Optional[BlueprintStatus] = None
    emotion: Optional[EmotionInterpretation] = None
    base: Optional[BaseSpec] = None
    formula: Optional[FormulaSpec] = None
    dna: Optional[WreathDNA] = None
    placements: Optional[List[PlacementEntry]] = None
    materials: Optional[List[Dict[str, Any]]] = None
    scores: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None
