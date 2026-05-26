# 33_VISUALIZER_RENDER_PIPELINE

## Purpose

This document defines the technical rendering pipeline for the Placement Visualization Engine.

It converts EC_CANON_V1 placement data into a visual wreath preview.

---

## Render Philosophy

The visualizer does not create design logic.

It renders design logic.

The Placement Engine produces geometry. The Visualization Engine displays it.

---

## Coordinate Normalization

Canonical canvas:
- size: 600 x 600
- center: 300, 300
- outer radius: 240
- inner radius: 110 to 150 depending on base

Polar to Cartesian:

```ts
x = centerX + radiusPx * cos(thetaRad)
y = centerY + radiusPx * sin(thetaRad)
```

Clock-position conventions should be documented and consistent across frontend/backend.

---

## Render Input

```ts
type VisualizerInput = {
  blueprint: Blueprint;
  visibleLayers: string[];
  selectedPlacementId?: string;
  showGrid: boolean;
  showZones: boolean;
  showBuildSequence?: boolean;
};
```

---

## Render Pipeline

### Step 1 — Clear Stage

Reset canvas or SVG group.

### Step 2 — Draw Background

Optional:
- transparent background
- cream/studio surface
- dark OS console surface

### Step 3 — Draw Wreath Base

Render:
- outer ring
- inner opening
- grapevine texture placeholder
- base visibility

### Step 4 — Draw Grid Overlays

If enabled:
- radial lines every 30 degrees
- clock labels
- inner/outer rings
- quadrant boundaries
- formula arc zone

### Step 5 — Sort Placements

Sort by:
1. z_index
2. layer priority
3. placement order

### Step 6 — Render Materials

For each placement:
- convert polar coordinate
- apply rotation
- apply scale
- draw material asset or placeholder
- apply selected state if active

### Step 7 — Render Debug Metadata

Optional:
- placement IDs
- anchor points
- cluster labels
- density heat indicators

### Step 8 — Render Selection Overlay

Highlight selected placement with:
- outline
- small point marker
- connecting inspector reference if desired

### Step 9 — Export

Export options:
- PNG
- SVG
- JSON snapshot

---

## Layer Priority

```ts
const layerPriority = {
  base: 1,
  greenery_base: 10,
  greenery_extension: 15,
  filler: 20,
  secondary_floral: 30,
  focal_floral: 40,
  berries: 50,
  accent: 60,
  decorative_overlay: 70
};
```

---

## Asset Fallback

MVP does not require every floral asset image.

If no asset exists, render:
- role-colored circle
- material initials
- simple petal marker
- vector placeholder

This prevents development from blocking on asset collection.

---

## Build Sequence Animation

Optional MVP+.

If enabled:
1. base appears
2. greenery foundation appears
3. focal clusters appear
4. secondary florals appear
5. filler appears
6. accents appear

This supports BuildBloom education and assembly preview.

---

## Performance Requirements

MVP visualizer should support:
- 100 placements without major lag
- layer toggling under 100ms
- selected placement update under 100ms
- export under 3 seconds

---

## Validation

Visualizer should warn if:
- placement radius is outside range
- unknown layer
- missing material
- invalid theta
- duplicate placement ID
