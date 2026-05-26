# 39_SPRINT_2_CANON_AND_BLUEPRINT_TICKETS

## Purpose
Sprint 2 implements EC_CANON_V1 in code and storage.

## Sprint Goal
Create schemas, validation, save/load behavior, and Design Library foundation.

## Ticket 2.1 — Define EC_CANON_V1 Types
Tasks:
- Blueprint type/interface.
- Emotion schema.
- Formula schema.
- DNA schema.
- Placement schema.
- Visualization schema.
- Manufacturing schema.

Acceptance:
- Types match `05_EC_CANON_V1_BLUEPRINT_SCHEMA.md`.
- Invalid objects fail validation.

## Ticket 2.2 — Blueprint Validation Utility
Tasks:
- Check required fields.
- Validate placements.
- Validate formula ID.
- Validate base size.
- Return warnings/errors.

Acceptance:
- Valid blueprint passes.
- Missing required field fails.
- Invalid radius fails.

## Ticket 2.3 — Blueprint Database Model
Tasks:
- Blueprint table/model.
- Store full JSON.
- Store searchable metadata: name, formula, emotion quadrant, timestamps, user_id.

Acceptance:
- Blueprint can be saved/fetched.
- Ownership enforced.

## Ticket 2.4 — Blueprint CRUD API
Endpoints:
- `GET /api/v1/blueprints`
- `GET /api/v1/blueprints/{id}`
- `POST /api/v1/blueprints`
- `PATCH /api/v1/blueprints/{id}`
- `DELETE /api/v1/blueprints/{id}`

Acceptance:
- CRUD works.
- Auth required.
- Invalid blueprint rejected.

## Ticket 2.5 — Design Library MVP UI
Tasks:
- Library route.
- Saved blueprint list.
- Empty state.
- Open blueprint action.
- Export placeholder.

Acceptance:
- User can see saved blueprints.
- User can open a blueprint into Design Studio.

## Ticket 2.6 — Blueprint JSON Viewer
Tasks:
- Render formatted JSON.
- Copy to clipboard.
- Handle large objects.

Acceptance:
- Blueprint JSON can be inspected in Studio.

## Sprint 2 Done When
EC_CANON_V1 exists in code, blueprints save/load, and library works.
