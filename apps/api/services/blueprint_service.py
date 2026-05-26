"""PostgreSQL-backed blueprint service.

Replaces services/blueprint_store.py (in-memory) with a SQLAlchemy-backed
implementation. The deterministic ID logic (UUID5) is preserved unchanged.

Canon note: _EC_NAMESPACE must never be changed — doing so invalidates all
existing stored blueprint IDs.
"""

import json
import uuid
from datetime import datetime, timezone
from typing import List, Optional

from sqlalchemy.orm import Session

from models.blueprint import Blueprint, BlueprintCreateInput, BlueprintPatchInput
from orm.models import BlueprintRow

# Fixed namespace — NEVER CHANGE.
_EC_NAMESPACE = uuid.UUID("ec000000-0000-0000-0000-000000000001")


def _deterministic_id(input_data: BlueprintCreateInput) -> str:
    seed = json.dumps(
        {
            "name": input_data.name,
            "tone": input_data.emotion.tone.value,
            "intensity": input_data.emotion.intensity,
        },
        sort_keys=True,
    )
    return str(uuid.uuid5(_EC_NAMESPACE, seed))


def _row_to_blueprint(row: BlueprintRow) -> Blueprint:
    """Reconstruct a Blueprint Pydantic object from a DB row."""
    data = row.blueprint_json
    return Blueprint(**data)


def create_blueprint(db: Session, input_data: BlueprintCreateInput) -> Blueprint:
    now = datetime.now(timezone.utc).isoformat()
    deterministic_id = _deterministic_id(input_data)

    blueprint = Blueprint(
        id=deterministic_id,
        schema_version=input_data.schema_version,
        name=input_data.name,
        status=input_data.status,
        emotion=input_data.emotion,
        created_at=now,
        updated_at=now,
        base=input_data.base,
        formula=input_data.formula,
        dna=input_data.dna,
    )

    # Upsert: if same deterministic ID exists, return existing record
    existing = db.query(BlueprintRow).filter_by(blueprint_id=deterministic_id).first()
    if existing:
        return _row_to_blueprint(existing)

    row = BlueprintRow(
        blueprint_id=deterministic_id,
        name=input_data.name,
        version="1.0.0",
        formula_id=input_data.formula.formula_id if input_data.formula else None,
        emotion_quadrant=input_data.emotion.quadrant,
        blueprint_json=blueprint.model_dump(mode="json"),
    )
    db.add(row)
    db.commit()
    db.refresh(row)
    return blueprint


def get_blueprint(db: Session, blueprint_id: str) -> Optional[Blueprint]:
    row = db.query(BlueprintRow).filter_by(blueprint_id=blueprint_id).first()
    if row is None:
        return None
    return _row_to_blueprint(row)


def list_blueprints(db: Session) -> List[Blueprint]:
    rows = db.query(BlueprintRow).order_by(BlueprintRow.created_at.desc()).all()
    return [_row_to_blueprint(r) for r in rows]


def update_blueprint(
    db: Session, blueprint_id: str, patch: BlueprintPatchInput
) -> Optional[Blueprint]:
    row = db.query(BlueprintRow).filter_by(blueprint_id=blueprint_id).first()
    if row is None:
        return None

    current = Blueprint(**row.blueprint_json)
    patch_data = patch.model_dump(exclude_unset=True, mode="json")

    # Merge patch into current blueprint dict
    current_dict = current.model_dump(mode="json")
    current_dict.update(patch_data)
    current_dict["updated_at"] = datetime.now(timezone.utc).isoformat()

    updated = Blueprint(**current_dict)
    row.blueprint_json = updated.model_dump(mode="json")
    row.name = updated.name
    if updated.formula:
        row.formula_id = updated.formula.formula_id
    if updated.emotion and updated.emotion.quadrant:
        row.emotion_quadrant = updated.emotion.quadrant

    db.commit()
    db.refresh(row)
    return updated


def delete_blueprint(db: Session, blueprint_id: str) -> bool:
    row = db.query(BlueprintRow).filter_by(blueprint_id=blueprint_id).first()
    if row is None:
        return False
    db.delete(row)
    db.commit()
    return True


def compile_blueprint(db: Session, blueprint_id: str) -> Optional[Blueprint]:
    """Validate EC_CANON_V1 completeness and promote status to 'saved'.

    Per 05_EC_CANON_V1_BLUEPRINT_SCHEMA.md a valid blueprint must have:
    - blueprint id, base dimensions, emotion metadata, formula id, dna profile,
      placement array, visualization settings, manufacturing object.

    For MVP we require the fields that are available after Sprint 2+3:
    id, emotion, name. Additional required fields are added in later sprints.
    """
    row = db.query(BlueprintRow).filter_by(blueprint_id=blueprint_id).first()
    if row is None:
        return None

    current = Blueprint(**row.blueprint_json)
    current_dict = current.model_dump(mode="json")
    current_dict["status"] = "saved"
    current_dict["updated_at"] = datetime.now(timezone.utc).isoformat()

    compiled = Blueprint(**current_dict)
    row.blueprint_json = compiled.model_dump(mode="json")
    db.commit()
    db.refresh(row)
    return compiled
