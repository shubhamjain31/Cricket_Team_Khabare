"""add new table team

Revision ID: 56d0bf4122d2
Revises: 490d3fac8b7b
Create Date: 2022-07-03 17:57:58.051497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56d0bf4122d2'
down_revision = '490d3fac8b7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Teams', sa.Column('Users', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Teams', 'Users', ['Users'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Teams', type_='foreignkey')
    op.drop_column('Teams', 'Users')
    # ### end Alembic commands ###
