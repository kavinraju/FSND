"""empty message

Revision ID: e05266d9d28c
Revises: 
Create Date: 2020-05-16 19:00:47.517056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e05266d9d28c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persons',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='persons_pkey')
    )
    op.create_table('table1',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('desp', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='table1_pkey')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('table1')
    op.drop_table('persons')
    # ### end Alembic commands ###
