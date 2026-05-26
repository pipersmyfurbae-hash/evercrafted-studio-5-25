# 44_SPRINT_7_RENDER_LIBRARY_QA_TICKETS

## Purpose
Sprint 7 completes supporting workflows and prepares MVP for demo.

## Sprint Goal
Finish Render Studio, polish Design Library, and complete QA.

## Ticket 7.1 — Render Prompt Endpoint
Endpoint:
`POST /api/v1/render-prompt/generate`

Acceptance:
- Prompt includes faux floral realism.
- Prompt includes formula/layout detail.
- Prompt avoids fresh bouquet language.

## Ticket 7.2 — Render Studio UI
Tasks:
- Select prompt mode.
- Generate prompt.
- Copy prompt.
- Show blueprint summary.

Modes:
- white background product
- lifestyle scene
- close-up detail
- Etsy listing visual

Acceptance:
- User can generate and copy prompts.

## Ticket 7.3 — Design Library Polish
Tasks:
- Search by name.
- Filter by formula/mood.
- Duplicate blueprint.
- Export JSON.

Acceptance:
- User can find and reuse saved designs.

## Ticket 7.4 — End-to-End QA Flow
Required Flow:
Memory → Blueprint → Design Studio → Save → Build Sheet → Render Prompt

Acceptance:
- Flow completes without console errors.
- Data persists.
- User can reopen saved blueprint.

## Ticket 7.5 — Demo Dataset
Tasks:
- Add 3 demo memories.
- Add 3 demo blueprints.
- Add 20 sample inventory items.

Acceptance:
- Demo account looks populated and presentable.

## Sprint 7 Done When
The MVP can be demoed as a coherent product.
