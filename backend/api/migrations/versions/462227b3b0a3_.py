"""empty message

Revision ID: 462227b3b0a3
Revises: 75c30e2921e8
Create Date: 2023-01-25 12:07:38.949567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '462227b3b0a3'
down_revision = '75c30e2921e8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('history', 'create_time')
    # ### end Alembic commands ###
