# 21_DATABASE_SCHEMA

## Purpose

This file defines the MVP database schema.

## users

- id UUID primary key
- email text unique
- name text
- created_at timestamp

## blueprints

- id UUID primary key
- user_id UUID
- blueprint_id text
- name text
- version text
- formula_id text
- emotion_quadrant text
- blueprint_json JSONB
- created_at timestamp
- updated_at timestamp

## blueprint_versions

- id UUID primary key
- blueprint_id UUID
- version_num integer
- blueprint_json JSONB
- note text
- created_at timestamp

## inventory_items

- id UUID primary key
- user_id UUID
- name text
- type text
- role text
- color text
- quantity numeric
- unit_cost numeric
- metadata JSONB
- created_at timestamp

## build_sheets

- id UUID primary key
- blueprint_id UUID
- build_sheet_json JSONB
- created_at timestamp

## render_prompts

- id UUID primary key
- blueprint_id UUID
- prompt_text text
- mode text
- created_at timestamp
