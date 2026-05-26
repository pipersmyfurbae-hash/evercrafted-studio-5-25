# 40_SPRINT_3_MEMORY_WEAVER_TICKETS

## Purpose
Sprint 3 builds Memory Weaver and emotional intake.

## Sprint Goal
User can enter memory/mood text and receive structured emotional interpretation and design direction.

## Ticket 3.1 — Emotion Classification Endpoint
Endpoint:
`POST /api/v1/emotion/classify`

Request:
```json
{
  "text": "A quiet remembrance wreath for my grandmother",
  "season": "spring",
  "size_in": 24
}
```

Acceptance:
- AI key is server-side only.
- Response is strict JSON.
- Invalid text returns validation error.

## Ticket 3.2 — Formula Recommendation Service
Tasks:
- Formula rules.
- Return formula ID/name.
- Include arc/density/movement defaults.

Acceptance:
- Same emotion input returns same formula recommendation.

## Ticket 3.3 — Memory Weaver UI
Tasks:
- Text input.
- Season selector.
- Wreath size selector.
- Generate button.
- Loading/error state.

Acceptance:
- User can submit input.
- UI displays emotional summary and formula recommendation.

## Ticket 3.4 — Create Blueprint From Memory
Tasks:
- Add Create Blueprint button.
- Send emotion/formula data to compile flow.
- Navigate to Design Studio.

Acceptance:
- User can create blueprint draft from Memory Weaver result.

## Ticket 3.5 — Emotional Trace Metadata
Tasks:
- Save original prompt.
- Save emotion output.
- Save formula output.
- Attach trace to blueprint metadata.

Acceptance:
- Blueprint metadata includes source prompt and interpretation.

## Sprint 3 Done When
Memory text becomes emotion output, formula recommendation, and blueprint draft.
