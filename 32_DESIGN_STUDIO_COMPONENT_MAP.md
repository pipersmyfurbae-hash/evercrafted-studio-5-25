# 32_DESIGN_STUDIO_COMPONENT_MAP

## Purpose

This document defines the Design Studio component map.

Design Studio is the main creator workspace where the engine becomes visible and editable.

---

## Design Studio Layout

```text
DesignStudioPage
├── StudioHeader
├── StudioLeftPanel
│   ├── BlueprintSummaryCard
│   ├── FormulaPanel
│   ├── LayerControls
│   ├── OverlayControls
│   └── ActionsPanel
├── StudioCanvasStage
│   ├── PlacementVisualizer
│   ├── RadialGridOverlay
│   ├── ZoneOverlay
│   ├── PlacementLayerRenderer
│   └── SelectionOverlay
├── StudioRightPanel
│   ├── PlacementInspector
│   ├── MaterialInspector
│   ├── BlueprintJSONInspector
│   └── ValidationPanel
└── StudioFooterBar
    ├── SaveStatus
    ├── RegeneratePlacementButton
    ├── ExportBlueprintButton
    └── GenerateBuildSheetButton
```

---

## Main Components

### DesignStudioPage

Owns route-level data loading and active blueprint context.

Responsibilities:
- load blueprint
- manage loading/error states
- provide blueprint to child components
- handle save/export actions

### StudioHeader

Shows:
- blueprint name
- formula
- current status
- save state
- primary actions

### StudioLeftPanel

Houses editing controls.

MVP sections:
- formula overview
- density preset
- visible layers
- overlays
- blueprint actions

### StudioCanvasStage

Main visual area.

Must support:
- blueprint preview
- radial grid
- selected placement highlight
- layer toggles
- fallback rendering if assets missing

### PlacementVisualizer

The mounted implementation of the Placement Visualization Engine.

Input:
```ts
{
  blueprint: Blueprint;
  visibleLayers: string[];
  selectedPlacementId?: string;
  showGrid: boolean;
  showZones: boolean;
}
```

Output:
- rendered wreath preview
- click events for placements

### PlacementInspector

Shows selected placement data:
- material
- role
- layer
- theta
- clock position
- radius
- rotation
- z-index
- cluster ID

### MaterialInspector

Allows simple material swap or assignment in MVP.

### BlueprintJSONInspector

Advanced panel for viewing canonical EC_CANON_V1.

### ValidationPanel

Shows:
- missing fields
- invalid placements
- warnings
- build readiness

---

## MVP Interactions

### Click Placement

1. User clicks placement.
2. Visualizer emits placement ID.
3. Store updates selected placement.
4. Inspector shows placement metadata.

### Toggle Layer

1. User toggles focal/floral/greenery layer.
2. Store updates visibleLayers.
3. Visualizer re-renders.

### Regenerate Placement

1. User clicks regenerate.
2. Frontend calls placement endpoint.
3. Blueprint draft updates.
4. Visualizer re-renders.

### Generate Build Sheet

1. User clicks Generate Build Sheet.
2. Frontend calls BuildBloom endpoint.
3. User navigates to build sheet view.

---

## MVP Component Priorities

Build in this order:

1. DesignStudioPage
2. PlacementVisualizer
3. LayerControls
4. PlacementInspector
5. Save/export actions
6. BlueprintJSONInspector
7. ValidationPanel
