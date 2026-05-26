"""initial schema

Revision ID: 001
Revises:
Create Date: 2026-05-26

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "blueprints",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("blueprint_id", sa.String(), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("version", sa.String(), nullable=True),
        sa.Column("formula_id", sa.String(), nullable=True),
        sa.Column("emotion_quadrant", sa.String(), nullable=True),
        sa.Column("blueprint_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("blueprint_id"),
    )
    op.create_index("ix_blueprints_blueprint_id", "blueprints", ["blueprint_id"])

    op.create_table(
        "blueprint_versions",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("blueprint_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("version_num", sa.Integer(), nullable=False),
        sa.Column("blueprint_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("note", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["blueprint_id"], ["blueprints.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "inventory_items",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("type", sa.String(), nullable=True),
        sa.Column("role", sa.String(), nullable=True),
        sa.Column("color", sa.String(), nullable=True),
        sa.Column("quantity", sa.Numeric(), nullable=True),
        sa.Column("unit_cost", sa.Numeric(), nullable=True),
        sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "build_sheets",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("blueprint_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("build_sheet_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(["blueprint_id"], ["blueprints.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("build_sheets")
    op.drop_table("inventory_items")
    op.drop_table("blueprint_versions")
    op.drop_index("ix_blueprints_blueprint_id", table_name="blueprints")
    op.drop_table("blueprints")
