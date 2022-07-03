"""add new

Revision ID: 88e3074483b6
Revises: 87c926430c6f
Create Date: 2022-07-03 18:29:06.819675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88e3074483b6'
down_revision = '87c926430c6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'Teams', 'Users', ['user_id'], ['id'])
    op.drop_column('Teams', 'user')
    op.drop_column('Teams', 'Users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Teams', sa.Column('Users', sa.INTEGER(), nullable=True))
    op.add_column('Teams', sa.Column('user', sa.VARCHAR(length=8), nullable=True))
    op.drop_constraint(None, 'Teams', type_='foreignkey')
    # ### end Alembic commands ###
