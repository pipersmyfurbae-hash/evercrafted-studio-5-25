# 20_API_CONTRACTS

## Purpose

This file defines MVP API endpoints.

## Authentication

```http
POST /api/v1/auth/signup
POST /api/v1/auth/login
GET /api/v1/me
```

## Emotion

```http
POST /api/v1/emotion/classify
```

## Blueprint

```http
POST /api/v1/blueprints/compile
GET /api/v1/blueprints
GET /api/v1/blueprints/{id}
POST /api/v1/blueprints
PATCH /api/v1/blueprints/{id}
DELETE /api/v1/blueprints/{id}
```

## Placement

```http
POST /api/v1/placement/generate
```

## Inventory

```http
GET /api/v1/inventory
POST /api/v1/inventory
PATCH /api/v1/inventory/{id}
DELETE /api/v1/inventory/{id}
```

## BuildBloom

```http
POST /api/v1/build-sheet/generate
```

## Render Studio

```http
POST /api/v1/render-prompt/generate
```

## Security

All AI calls must be server-side.
