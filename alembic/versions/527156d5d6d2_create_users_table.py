"""create users table

Revision ID: e9589bd7d619
Revises:
Create Date: 2023-11-24 08:32:27.745093

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9589bd7d619'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), unique=True, nullable=False),
        sa.Column('nickname', sa.String(50), nullable=False),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
    )


def downgrade() -> None:
    pass
