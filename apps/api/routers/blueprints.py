from fastapi import APIRouter, HTTPException
from typing import List

from models.blueprint import Blueprint, BlueprintCreateInput
from services.blueprint_store import create_blueprint, get_blueprint, list_blueprints

router = APIRouter(prefix="/blueprints", tags=["blueprints"])


@router.post("", response_model=Blueprint, status_code=201)
def create(input_data: BlueprintCreateInput):
    return create_blueprint(input_data)


@router.get("", response_model=List[Blueprint])
def list_all():
    return list_blueprints()


@router.get("/{blueprint_id}", response_model=Blueprint)
def get_one(blueprint_id: str):
    blueprint = get_blueprint(blueprint_id)
    if blueprint is None:
        raise HTTPException(status_code=404, detail="Blueprint not found")
    return blueprint
