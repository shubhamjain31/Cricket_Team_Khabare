"""add new table team

Revision ID: c4144561a781
Revises: da46645640fe
Create Date: 2022-07-03 18:13:29.317552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4144561a781'
down_revision = 'da46645640fe'
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
