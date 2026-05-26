# 09_PLACEMENT_ENGINE_SPEC

## Purpose

The Placement Engine generates deterministic wreath geometry. It translates formula and DNA into actual placement points.

## Canon Rule

> AI interprets. Geometry places.

## Coordinate System

```json
{"theta_deg": 215, "radius_norm": 0.72, "radius_in": 8.6}
```

- theta_deg: angle around wreath
- radius_norm: 0.0 center to 1.0 outer edge
- radius_in: physical radius in inches

## Inputs

base diameter, formula, DNA traits, material roles, desired density, inventory constraints.

## Output Example

```json
{
  "placement_id": "pl_001",
  "role": "focal",
  "layer": "focal_floral",
  "theta_deg": 215,
  "clock_position": "7:10",
  "radius_norm": 0.72,
  "rotation_deg": -18,
  "scale": 1.0,
  "z_index": 40
}
```

## MVP Algorithm

1. Read formula arc range.
2. Determine cluster anchors.
3. Allocate roles by DNA ratios.
4. Generate greenery placements first.
5. Generate focal placements.
6. Generate secondary/filler placements.
7. Apply spacing rules.
8. Apply rotation and stem direction.
9. Assign z-index.
10. Return deterministic placement array.

## Validation Rules

Prevent excessive symmetry, centered flower blobs, impossible overlap, no negative space, overcrowding, and non-buildable density.
