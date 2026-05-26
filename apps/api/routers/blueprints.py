"""Blueprint CRUD + compile routes.

GET    /api/v1/blueprints            — list all
POST   /api/v1/blueprints            — create (Sprint 1 compatible)
POST   /api/v1/blueprints/compile    — validate + promote to 'saved'
GET    /api/v1/blueprints/{id}       — get one
PATCH  /api/v1/blueprints/{id}       — partial update
DELETE /api/v1/blueprints/{id}       — delete
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core.database import get_db
from models.blueprint import Blueprint, BlueprintCreateInput, BlueprintPatchInput
from services.blueprint_service import (
    compile_blueprint,
    create_blueprint,
    delete_blueprint,
    get_blueprint,
    list_blueprints,
    update_blueprint,
)

router = APIRouter(prefix="/blueprints", tags=["blueprints"])


@router.post("", response_model=Blueprint, status_code=201)
def create(input_data: BlueprintCreateInput, db: Session = Depends(get_db)):
    return create_blueprint(db, input_data)


@router.get("", response_model=List[Blueprint])
def list_all(db: Session = Depends(get_db)):
    return list_blueprints(db)


# /compile must come before /{blueprint_id} so FastAPI doesn't treat "compile" as an ID
@router.post("/compile", response_model=Blueprint)
def compile_one(blueprint_id: str, db: Session = Depends(get_db)):
    """Validate EC_CANON_V1 completeness and set status to 'saved'."""
    blueprint = compile_blueprint(db, blueprint_id)
    if blueprint is None:
        raise HTTPException(status_code=404, detail="Blueprint not found")
    return blueprint


@router.get("/{blueprint_id}", response_model=Blueprint)
def get_one(blueprint_id: str, db: Session = Depends(get_db)):
    blueprint = get_blueprint(db, blueprint_id)
    if blueprint is None:
        raise HTTPException(status_code=404, detail="Blueprint not found")
    return blueprint


@router.patch("/{blueprint_id}", response_model=Blueprint)
def patch_one(
    blueprint_id: str,
    patch: BlueprintPatchInput,
    db: Session = Depends(get_db),
):
    updated = update_blueprint(db, blueprint_id, patch)
    if updated is None:
        raise HTTPException(status_code=404, detail="Blueprint not found")
    return updated


@router.delete("/{blueprint_id}", status_code=204)
def delete_one(blueprint_id: str, db: Session = Depends(get_db)):
    deleted = delete_blueprint(db, blueprint_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Blueprint not found")
