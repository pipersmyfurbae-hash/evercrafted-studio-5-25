# 42_SPRINT_5_VISUALIZER_AND_DESIGN_STUDIO_TICKETS

## Purpose
Sprint 5 turns placement data into a visible Design Studio experience.

## Sprint Goal
User can open a blueprint and see a visual wreath layout with inspectable placements.

## Ticket 5.1 — PlacementVisualizer Component
Inputs:
- blueprint
- visible layers
- selected placement ID
- grid visibility
- zone visibility

Acceptance:
- Visualizer renders wreath base.
- Visualizer renders placement markers.
- Missing material images do not break rendering.

## Ticket 5.2 — Radial Grid Overlay
Tasks:
- Draw outer ring.
- Draw inner ring.
- Draw radial lines.
- Optional clock labels.

Acceptance:
- Grid can be toggled.
- Grid aligns with placement coordinates.

## Ticket 5.3 — Layer Controls
Tasks:
- Add layer toggles.
- Update visible layers state.
- Re-render visualizer.

Acceptance:
- Hidden layers disappear without changing blueprint data.

## Ticket 5.4 — Placement Selection
Tasks:
- Click placement marker.
- Set selected placement.
- Highlight selected marker.
- Show inspector data.

Acceptance:
- Inspector shows theta, clock position, radius, layer, role, z-index.

## Ticket 5.5 — Design Studio Page
Tasks:
- Left panel.
- Canvas stage.
- Right inspector.
- Footer actions.
- Save/export buttons.

Acceptance:
- User can open blueprint, inspect visual data, and save.

## Ticket 5.6 — Regenerate Placement Button
Tasks:
- Call placement endpoint.
- Update draft blueprint.
- Re-render visualizer.
- Warn about unsaved changes.

Acceptance:
- Regeneration works without overwriting saved blueprint until user saves.

## Sprint 5 Done When
A saved blueprint can be opened, rendered, inspected, and saved from Design Studio.
