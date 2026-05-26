# 35_MVP_ACCEPTANCE_CRITERIA

## Purpose

This document defines when the MVP is done.

Developers should use this as the pass/fail checklist.

---

## Global MVP Acceptance

The MVP is accepted when a user can complete this flow without developer assistance:

```text
Enter memory → Generate design → View blueprint → See visual placement → Save design → Generate build sheet
```

---

## Authentication

Accepted when:
- user can create account
- user can log in
- user can log out
- saved data belongs to correct user

---

## Memory Weaver

Accepted when:
- user can submit memory/mood text
- backend returns structured emotion JSON
- response includes emotional summary
- response includes formula recommendation
- user can create blueprint from result

---

## Blueprint Compiler

Accepted when:
- system returns valid EC_CANON_V1 object
- blueprint includes emotion, formula, DNA, placements, visualization, manufacturing shell
- blueprint can be saved to database
- malformed blueprint is rejected

---

## Placement Engine

Accepted when:
- placement generation is deterministic
- placements include theta, radius, role, layer, z-index
- placements remain inside wreath bounds
- visible negative space exists
- output is stable for same seed/input

---

## Visualization Engine

Accepted when:
- blueprint renders on canvas/SVG
- user can toggle grid
- user can toggle layers
- selected placement can be inspected
- missing assets do not break render

---

## Design Studio

Accepted when:
- blueprint opens in Studio
- visualizer displays placement data
- user can inspect placement details
- user can save blueprint
- user can generate build sheet

---

## Inventory Weaver

Accepted when:
- user can create material
- user can edit material
- user can delete material
- material can be assigned or referenced by blueprint

---

## BuildBloom

Accepted when:
- build sheet can be generated from blueprint
- build sheet includes materials list
- build sheet includes build steps
- output is printable or exportable

---

## Design Library

Accepted when:
- user can see saved blueprints
- user can open saved blueprint
- user can duplicate/export blueprint

---

## Non-Acceptance Conditions

MVP is not accepted if:
- placement is random AI-only
- AI API key is exposed in frontend
- blueprints only exist in local browser state
- visualizer breaks without floral images
- user cannot save/reopen design
- build sheet cannot be generated
