"""add new column

Revision ID: b2ebd7087dd6
Revises: 52315ce2502b
Create Date: 2022-07-03 16:30:03.926527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2ebd7087dd6'
down_revision = '52315ce2502b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('ip_address', sa.String(length=100), nullable=True))
    op.add_column('Users', sa.Column('user_agent', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'user_agent')
    op.drop_column('Users', 'ip_address')
    # ### end Alembic commands ###
