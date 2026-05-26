# 07_FORMULA_ENGINE_SPEC

## Purpose

The Formula Engine maps emotional interpretation to composition archetypes. A formula is a structural pattern for wreath composition.

## Inputs

- emotion output
- base size
- desired density
- season
- style tags
- inventory availability
- user-selected constraints

## Output Example

```json
{
  "formula_id": "asymmetrical_crescent",
  "formula_name": "Asymmetrical Crescent",
  "arc_start_deg": 120,
  "arc_end_deg": 275,
  "negative_space_deg": 150,
  "primary_cluster_zone": "lower_left",
  "secondary_cluster_zone": "left_rise",
  "flow_direction": "counterclockwise"
}
```

## MVP Formula Set

1. Asymmetrical Crescent
2. Bottom-Weighted Crescent
3. Side Sweep
4. Open Arc
5. Full Halo
6. Split Garden

## Non-Responsibilities

The Formula Engine does not choose exact placements, render visuals, or generate build steps.
