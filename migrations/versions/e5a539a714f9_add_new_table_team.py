"""add new table team

Revision ID: e5a539a714f9
Revises: e8930a32653b
Create Date: 2022-07-03 18:21:33.387238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5a539a714f9'
down_revision = 'e8930a32653b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Teams', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'Users', ['user_id'], ['id'])
        batch_op.drop_column('user')
        batch_op.drop_column('Users')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Teams', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Users', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('user', sa.VARCHAR(length=8), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
