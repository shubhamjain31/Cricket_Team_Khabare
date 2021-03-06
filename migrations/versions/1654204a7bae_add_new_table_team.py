"""add new table team

Revision ID: 1654204a7bae
Revises: 63814837855f
Create Date: 2022-07-03 18:06:28.763086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1654204a7bae'
down_revision = '63814837855f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'Teams', 'Users', ['user'], ['id'])
    op.drop_column('Teams', 'Users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Teams', sa.Column('Users', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'Teams', type_='foreignkey')
    # ### end Alembic commands ###
