"""Password hash

Revision ID: 0f9b81020c7e
Revises: 410ef4c9d7be
Create Date: 2017-02-21 17:26:39.365121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f9b81020c7e'
down_revision = '410ef4c9d7be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###
