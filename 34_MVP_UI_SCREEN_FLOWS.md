# 34_MVP_UI_SCREEN_FLOWS

## Purpose

This document defines exact MVP user flows.

It tells developers how the product experience should work from screen to screen.

---

## Flow 1 — First Design Creation

### Entry

User lands on Dashboard.

CTA:
- Create New Design
- Start With Memory Weaver

### Memory Weaver Screen

User enters:
- memory or mood
- season
- wreath size
- optional palette/style

User clicks:
- Generate Design

System returns:
- emotional summary
- formula recommendation
- palette direction
- density
- generated blueprint preview option

User clicks:
- Create Blueprint

System compiles blueprint and opens Design Studio.

---

## Flow 2 — Design Studio Review

### Design Studio Opens

User sees:
- visual wreath preview
- formula summary
- layer controls
- placement inspector
- save button
- build sheet button

### User Actions

User may:
- toggle radial grid
- toggle layers
- click placements
- inspect metadata
- regenerate placements
- save blueprint

---

## Flow 3 — Inventory Assignment

User opens Inventory Weaver.

User creates:
- material name
- material type
- role
- quantity
- cost
- color

In Design Studio, user can assign available materials to placement roles.

---

## Flow 4 — Save to Design Library

User clicks Save.

System:
- validates blueprint
- stores EC_CANON_V1 object
- creates/updates preview thumbnail if available

User can later open from Library.

---

## Flow 5 — Generate Build Sheet

User clicks Generate Build Sheet.

System:
- sends blueprint to BuildBloom
- returns build sheet
- displays build sequence and materials

User can:
- print
- export
- return to Studio

---

## Flow 6 — Render Studio Prompt

User opens Render Studio from blueprint.

System generates:
- product photo prompt
- lifestyle prompt
- white background prompt
- faux floral realism notes

---

## MVP Navigation Logic

Primary path:

```text
Dashboard → Memory Weaver → Design Studio → Save → Build Sheet
```

Secondary path:

```text
Design Library → Design Studio → Render Studio / Build Sheet
```

---

## Empty States

### No Blueprints

Show:
- “Create your first emotional blueprint”
- button to Memory Weaver

### No Inventory

Show:
- “Add materials now or continue with placeholders”
- do not block blueprint creation

### No Visual Assets

Show:
- placement markers
- do not block rendering
