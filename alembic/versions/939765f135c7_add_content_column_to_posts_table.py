"""add content column to posts table

Revision ID: 939765f135c7
Revises: 66b002abf532
Create Date: 2023-08-25 02:07:52.377516

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '939765f135c7'
down_revision: Union[str, None] = '66b002abf532'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
