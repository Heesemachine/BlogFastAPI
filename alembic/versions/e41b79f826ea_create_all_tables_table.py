"""create all_tables table

Revision ID: e41b79f826ea
Revises: 44023444bf88
Create Date: 2023-12-14 20:35:53.939697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e41b79f826ea'
down_revision: Union[str, None] = '44023444bf88'
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
    
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('title', sa.String(50), nullable=False),
        sa.Column('description', sa.String(255),nullable=False),
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
