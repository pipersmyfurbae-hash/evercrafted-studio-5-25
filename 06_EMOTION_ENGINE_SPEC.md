# 06_EMOTION_ENGINE_SPEC

## Purpose

The Emotion Engine translates memory, mood, user language, seasonal context, and psychographic signals into structured emotional variables. It interprets emotional intent; it does not place flowers.

## Inputs

- freeform memory text
- mood words
- customer request
- seasonal theme
- occasion
- color preferences
- home context
- image reference metadata in later versions

## Output Example

```json
{
  "primary_tone": "quiet gratitude",
  "secondary_tones": ["nostalgia", "soft hope"],
  "valence": 0.2,
  "arousal": -0.4,
  "quadrant": "Cozy & Calm",
  "emotion_vector": {"calm": 0.8, "nostalgia": 0.7, "joy": 0.2, "hope": 0.4},
  "palette_direction": "warm ivory, muted blue, soft sage",
  "density_bias": "medium airy",
  "movement_bias": "gentle upward crescent"
}
```

## Responsibilities

The Emotion Engine determines emotional tone, density tendency, palette direction, movement intensity, formula candidates, and symbolic material associations.

## Non-Responsibilities

It must not generate final placement, invent non-buildable compositions, override deterministic geometry, or bypass formula/placement systems.

## MVP Endpoint

`POST /api/v1/emotion/classify`
