# 10_PLACEMENT_VISUALIZATION_ENGINE_SPEC

## Purpose

The Placement Visualization Engine renders placement data into visual wreath previews. This incorporates the uploaded visualizer and System Console rendering logic as a canonical engine.

## Role in Ecosystem

Placement Engine → Visualization Engine → Design Studio / BuildBloom / Render Studio.

It does not decide placement. It displays placement.

## Responsibilities

- render wreath base
- render placement points
- render material layers
- render z-index order
- show radial guides
- show quadrant overlays
- show build sequence animation
- preview EC_CANON_V1 blueprint data
- export visual previews

## Canonical Render Layers

1. base
2. greenery_base
3. greenery_extension
4. filler
5. secondary_floral
6. focal_floral
7. berries
8. accents
9. decorative_overlay

## MVP Scope

MVP visualizer should include blueprint preview, radial guides, layer rendering, placement dot fallback, material icon fallback, and PNG export if practical. Photorealistic rendering is not required for MVP.
