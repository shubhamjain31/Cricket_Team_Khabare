"""add new table team

Revision ID: 87c926430c6f
Revises: 01ffb2f6522c
Create Date: 2022-07-03 18:24:58.555170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87c926430c6f'
down_revision = '01ffb2f6522c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'Teams', 'Users', ['user_id'], ['id'])
    op.drop_column('Teams', 'Users')
    op.drop_column('Teams', 'user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Teams', sa.Column('user', sa.VARCHAR(length=8), nullable=True))
    op.add_column('Teams', sa.Column('Users', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'Teams', type_='foreignkey')
    # ### end Alembic commands ###
