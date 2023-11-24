"""create posts table

Revision ID: 44023444bf88
Revises: e9589bd7d619
Create Date: 2023-11-24 09:07:38.254958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44023444bf88'
down_revision: Union[str, None] = 'e9589bd7d619'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.String(255), unique=True, nullable=False),
        sa.Column('likes', sa.Integer, default=0),
        sa.Column('comments', sa.Integer, default=0),

        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
    )
    op.create_table(
        'comments',

        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('description', sa.String(255), nullable=False),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('post_id', sa.Integer, nullable=False),

        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id']),

    )
    op.create_table(
        'likes',
         sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('post_id', sa.Integer, nullable=False),

        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id']),
    )


def downgrade() -> None:
    pass
