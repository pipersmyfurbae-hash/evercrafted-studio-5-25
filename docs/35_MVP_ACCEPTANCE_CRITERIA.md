# 35_MVP_ACCEPTANCE_CRITERIA

## MVP Completion Standard

The MVP is complete only when this full flow works:

Memory → Blueprint → Placement → Visualizer → Save → Build Sheet

## Acceptance Criteria

### 1. App Foundation

- App runs locally.
- Frontend and backend can be started.
- Project structure is clean.
- Environment variables are documented.

### 2. Memory Weaver

- User can enter memory or mood text.
- System returns structured emotional interpretation.
- Result can start blueprint creation.

### 3. Blueprint

- Blueprint follows EC_CANON_V1 structure.
- Blueprint can be saved.
- Blueprint can be reopened.

### 4. Placement Engine

- Placement is deterministic.
- Placement includes angle, radius, role, layer, and z-index.
- Same input returns stable output.
- Placement is not random AI-only.

### 5. Visualizer

- Blueprint placements render visually.
- Visualizer works even without floral images.
- User can inspect placement data.

### 6. Build Sheet

- System generates material list.
- System generates build steps.
- Build sheet is readable and useful.

## Not Accepted If

- It is only a mockup.
- Buttons do not work.
- Data is not saved.
- AI keys are exposed in frontend.
- Claude invents a new architecture.
- The system turns into a generic wreath prompt generator.