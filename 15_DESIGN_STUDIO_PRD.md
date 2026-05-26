# 15_DESIGN_STUDIO_PRD

## Purpose

Design Studio is the main creator workspace. It connects the Placement Engine, Placement Visualization Engine, EC_CANON_V1 blueprint data, material editing, and preview/export workflows.

## Core Role

Design Studio is where the abstract engine becomes visible and editable. It is not just a canvas. It is the user-facing orchestration layer for blueprint design.

## MVP Features

### Blueprint Preview
Render placement data visually.

### Layer Controls
Toggle base, greenery, filler, focal florals, and accents.

### Placement Inspector
Click a placement and inspect material, role, theta, radius, clock position, rotation, and layer.

### Basic Editing
Allow the user to change material, adjust density preset, regenerate placements, and save blueprint.

### Blueprint JSON View
Advanced users can inspect EC_CANON_V1 output.

### Export
Save to library, export JSON, generate build sheet.

## Visualizer Integration

Design Studio must use `10_PLACEMENT_VISUALIZATION_ENGINE_SPEC.md`. The visualizer is part of the product, not a disconnected prototype.

## MVP Acceptance Criteria

A user can open a generated blueprint, see a visual layout, inspect placement data, save the design, and generate a build sheet.
