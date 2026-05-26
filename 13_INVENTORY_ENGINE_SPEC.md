# 13_INVENTORY_ENGINE_SPEC

## Purpose

The Inventory Engine makes designs inventory-aware.

## Inventory Object

```json
{
  "material_id": "mat_001",
  "name": "Cream Peony",
  "type": "flower",
  "role": "focal",
  "color": "cream",
  "quantity": 8,
  "unit_cost": 2.75,
  "tags": ["spring", "romantic", "premium_faux"]
}
```

## Responsibilities

Store materials, classify roles, track stock, calculate cost, filter design choices, suggest substitutions, and support BuildBloom material counts.

## MVP Scope

Manual material entry, quantity, unit cost, type, role, color, and use in blueprint.
