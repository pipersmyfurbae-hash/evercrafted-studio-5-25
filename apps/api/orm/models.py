"""SQLAlchemy ORM models — matches 21_DATABASE_SCHEMA.md."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID

from core.database import Base


def _now():
    return datetime.now(timezone.utc)


class BlueprintRow(Base):
    __tablename__ = "blueprints"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # blueprint_id is the deterministic EC UUID string (uuid5)
    blueprint_id = Column(String, unique=True, nullable=False, index=True)
    user_id = Column(UUID(as_uuid=True), nullable=True)
    name = Column(String, nullable=False)
    version = Column(String, default="1.0.0")
    formula_id = Column(String, nullable=True)
    emotion_quadrant = Column(String, nullable=True)
    # Full EC_CANON_V1 JSON stored as JSONB
    blueprint_json = Column(JSONB, nullable=False)
    created_at = Column(DateTime(timezone=True), default=_now, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=_now, onupdate=_now, nullable=False)


class BlueprintVersionRow(Base):
    __tablename__ = "blueprint_versions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    blueprint_id = Column(
        UUID(as_uuid=True),
        ForeignKey("blueprints.id", ondelete="CASCADE"),
        nullable=False,
    )
    version_num = Column(Integer, nullable=False)
    blueprint_json = Column(JSONB, nullable=False)
    note = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=_now, nullable=False)


class InventoryItemRow(Base):
    __tablename__ = "inventory_items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=True)
    role = Column(String, nullable=True)
    color = Column(String, nullable=True)
    quantity = Column(Numeric, default=0)
    unit_cost = Column(Numeric, default=0)
    metadata_ = Column("metadata", JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), default=_now, nullable=False)


class BuildSheetRow(Base):
    __tablename__ = "build_sheets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    blueprint_id = Column(
        UUID(as_uuid=True),
        ForeignKey("blueprints.id", ondelete="CASCADE"),
        nullable=False,
    )
    build_sheet_json = Column(JSONB, nullable=False)
    created_at = Column(DateTime(timezone=True), default=_now, nullable=False)
