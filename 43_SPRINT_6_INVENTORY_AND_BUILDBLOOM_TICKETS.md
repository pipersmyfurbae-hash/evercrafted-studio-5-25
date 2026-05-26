# 43_SPRINT_6_INVENTORY_AND_BUILDBLOOM_TICKETS

## Purpose
Sprint 6 makes the MVP practical and manufacturable.

## Sprint Goal
User can manage inventory and generate a build sheet from a blueprint.

## Ticket 6.1 — Inventory CRUD API
Endpoints:
- `GET /api/v1/inventory`
- `POST /api/v1/inventory`
- `PATCH /api/v1/inventory/{id}`
- `DELETE /api/v1/inventory/{id}`

Acceptance:
- User can create, edit, delete inventory.
- Ownership enforced.

## Ticket 6.2 — Inventory Weaver UI
Fields:
- name
- type
- role
- color
- quantity
- unit cost
- tags optional

Acceptance:
- User can manage material list.
- UI shows basic cost summary.

## Ticket 6.3 — Material Assignment in Design Studio
Tasks:
- Show materials by role.
- Allow assignment to placement or role group.
- Save material references in blueprint.

Acceptance:
- Blueprint can reference inventory materials.
- Role mismatch is warned.

## Ticket 6.4 — BuildBloom Endpoint
Endpoint:
`POST /api/v1/build-sheet/generate`

Acceptance:
- Build sheet includes material counts.
- Build sheet includes ordered steps.
- Build sheet references clusters/layers.

## Ticket 6.5 — Build Sheet UI
Sections:
- design summary
- material list
- build steps
- quality checklist
- print/export action

Acceptance:
- User can generate and view build sheet.
- Print layout is usable.

## Sprint 6 Done When
A blueprint can become a practical build sheet using inventory/material references.
