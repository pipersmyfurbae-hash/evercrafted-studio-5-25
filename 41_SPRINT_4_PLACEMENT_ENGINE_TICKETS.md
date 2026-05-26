# 41_SPRINT_4_PLACEMENT_ENGINE_TICKETS

## Purpose
Sprint 4 implements deterministic placement.

## Sprint Goal
Generate deterministic polar placement data from formula, DNA, and blueprint context.

## Ticket 4.1 — Polar Coordinate Utility
Functions:
- theta to clock position
- polar to Cartesian
- Cartesian to polar
- normalize radius
- degree wrapping

Acceptance:
- Utilities are tested.
- Clock position output is consistent.

## Ticket 4.2 — DNA Derivation Service
Tasks:
- Implement MVP DNA traits.
- Derive density profile.
- Derive cluster count.
- Derive greenery ratio.
- Derive silence arc.

Acceptance:
- Same input returns same DNA.

## Ticket 4.3 — Placement Generation Endpoint
Endpoint:
`POST /api/v1/placement/generate`

Acceptance:
- Returns deterministic placements.
- Every placement includes theta, radius, role, layer, z-index.
- Placements stay inside wreath bounds.

## Ticket 4.4 — Layer and Role Assignment
Roles:
- base
- greenery
- filler
- secondary_floral
- focal_floral
- accent

Acceptance:
- Role/layer exists on every placement.
- z-index follows canonical render priority.

## Ticket 4.5 — Spacing and Negative Space Validation
Tasks:
- Prevent close clustering.
- Preserve formula silence arc.
- Flag symmetry.
- Flag overcrowding.

Acceptance:
- Generated output has intentional negative space.

## Ticket 4.6 — Blueprint Compiler Integration
Tasks:
- Compile emotion + formula + DNA + placements into EC_CANON_V1.

Acceptance:
- Blueprint includes deterministic placement array and passes validation.

## Sprint 4 Done When
System generates a complete blueprint with deterministic placement data.
