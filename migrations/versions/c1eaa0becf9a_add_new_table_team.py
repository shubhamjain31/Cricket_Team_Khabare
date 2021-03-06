"""add new table team

Revision ID: c1eaa0becf9a
Revises: 59f5d2b892a2
Create Date: 2022-07-03 18:57:29.338676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1eaa0becf9a'
down_revision = '59f5d2b892a2'
branch_labels = None
depends_on = None


naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Teams', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.create_foreign_key(None, 'Users', ['user_id'], ['id'], ondelete='CASCADE')
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
