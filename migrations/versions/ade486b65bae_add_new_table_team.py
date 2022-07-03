"""add new table team

Revision ID: ade486b65bae
Revises: 609bdf411a1f
Create Date: 2022-07-03 18:04:33.641375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ade486b65bae'
down_revision = '609bdf411a1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Teams', 'user',
               existing_type=sa.VARCHAR(length=8),
               nullable=False)
    op.create_foreign_key(None, 'Teams', 'Users', ['user'], ['id'])
    op.drop_column('Teams', 'Users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Teams', sa.Column('Users', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'Teams', type_='foreignkey')
    op.alter_column('Teams', 'user',
               existing_type=sa.VARCHAR(length=8),
               nullable=True)
    # ### end Alembic commands ###
