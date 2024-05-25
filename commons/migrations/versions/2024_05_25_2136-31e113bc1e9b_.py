"""empty message

Revision ID: 31e113bc1e9b
Revises: b9f3f1fbb701
Create Date: 2024-05-25 21:36:48.867672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31e113bc1e9b'
down_revision: Union[str, None] = 'b9f3f1fbb701'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'description',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=10000),
               existing_nullable=True)
    op.alter_column('post', 'query',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=10000),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'query',
               existing_type=sa.String(length=10000),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=False)
    op.alter_column('post', 'description',
               existing_type=sa.String(length=10000),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=True)
    # ### end Alembic commands ###
