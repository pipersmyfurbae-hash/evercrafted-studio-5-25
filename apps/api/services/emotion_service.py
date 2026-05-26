"""Emotion Engine — interprets freeform memory/mood text into structured emotion data.

Uses the Claude API (server-side only; API key never exposed to client).

Spec references:
  - 06_EMOTION_ENGINE_SPEC.md
  - 05_EC_CANON_V1_BLUEPRINT_SCHEMA.md (emotion schema)
"""

import json
from typing import Any, Dict

import anthropic

from core.config import settings
from models.emotion import EmotionClassifyInput, EmotionOutput


# ---------------------------------------------------------------------------
# Formula recommendation map  (Emotion quadrant → formula candidates)
# ---------------------------------------------------------------------------

_QUADRANT_FORMULA_MAP: Dict[str, list[str]] = {
    "Cozy & Calm": ["crescent_asymmetrical", "arc_loose"],
    "Bright & Joyful": ["radial_open", "arc_full_crescent"],
    "Deep & Contemplative": ["crescent_deep", "spiral_descent"],
    "Bold & Expressive": ["arc_dramatic", "radial_dense"],
}

_KNOWN_QUADRANTS = list(_QUADRANT_FORMULA_MAP.keys())


# ---------------------------------------------------------------------------
# System prompt
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = """You are the Evercrafted Emotion Engine — an expert at translating human memory,
mood, and emotional language into structured floral design variables.

Your job is to interpret the user's input and return a precise JSON object that will drive a
procedural wreath design system. You must follow the EC_CANON_V1 emotion schema exactly.

Output rules:
- Return ONLY valid JSON. No markdown fences, no extra text.
- `primary_tone`: a short descriptive phrase (2-4 words), e.g. "quiet coastal grief"
- `secondary_tones`: 2-3 supporting tones as short phrases
- `valence`: float -1.0 (very negative) to 1.0 (very positive)
- `arousal`: float -1.0 (very calm/still) to 1.0 (very energised/intense)
- `quadrant`: exactly one of: "Cozy & Calm", "Bright & Joyful", "Deep & Contemplative", "Bold & Expressive"
- `emotion_vector`: object with float values 0.0-1.0 for relevant keys from:
    calm, nostalgia, joy, hope, grief, love, celebration, melancholy, reverence, drama, romance, serenity, festive
  Include only the 3-6 most relevant keys.
- `palette_direction`: short colour description, e.g. "warm ivory, dusty rose, sage"
- `density_bias`: one of: "light and airy", "medium airy", "medium full", "full and lush"
- `movement_bias`: short phrase, e.g. "gentle upward crescent", "cascading downward arc"
- `formula_candidates`: 2 formula IDs from: crescent_asymmetrical, arc_loose, radial_open,
    arc_full_crescent, crescent_deep, spiral_descent, arc_dramatic, radial_dense
- `narrative_summary`: 1-2 sentences describing the emotional intent of the design.

Evercrafted design doctrine:
- Favour asymmetry, movement, and negative space.
- Avoid generic symmetry, centred blobs, bouquet aesthetics.
- Every design must be emotionally coherent and physically buildable."""


def classify_emotion(input_data: EmotionClassifyInput) -> EmotionOutput:
    """Call Claude to interpret emotion and return structured EmotionOutput."""

    client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

    user_message = _build_user_message(input_data)

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    raw_text = message.content[0].text.strip()
    data: Dict[str, Any] = json.loads(raw_text)

    # Ensure formula_candidates align with the quadrant recommendation map
    quadrant = data.get("quadrant", "Cozy & Calm")
    if quadrant not in _KNOWN_QUADRANTS:
        quadrant = "Cozy & Calm"
        data["quadrant"] = quadrant

    # Override/augment formula_candidates with canonical map if needed
    canonical_formulas = _QUADRANT_FORMULA_MAP[quadrant]
    if not data.get("formula_candidates"):
        data["formula_candidates"] = canonical_formulas

    return EmotionOutput(**data)


def _build_user_message(input_data: EmotionClassifyInput) -> str:
    parts = [f"Memory / mood text: {input_data.text}"]
    if input_data.occasion:
        parts.append(f"Occasion: {input_data.occasion}")
    if input_data.color_preferences:
        parts.append(f"Color preferences: {input_data.color_preferences}")
    return "\n".join(parts)
