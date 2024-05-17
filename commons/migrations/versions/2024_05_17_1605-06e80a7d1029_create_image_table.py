"""create Image table

Revision ID: 06e80a7d1029
Revises: d3393c03bec0
Create Date: 2024-05-17 16:05:49.638644

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06e80a7d1029'
down_revision: Union[str, None] = 'd3393c03bec0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
