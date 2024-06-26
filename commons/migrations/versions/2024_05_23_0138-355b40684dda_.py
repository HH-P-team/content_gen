"""empty message

Revision ID: 355b40684dda
Revises: 45fc6f158bf0
Create Date: 2024-05-23 01:38:25.771406

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '355b40684dda'
down_revision: Union[str, None] = '45fc6f158bf0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('image', 'uuid',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('image', 'uuid',
               existing_type=sa.UUID(),
               nullable=True)
    # ### end Alembic commands ###
