"""empty message

Revision ID: 2519b6d012d7
Revises: 56f989faf627
Create Date: 2021-06-09 19:56:32.259852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2519b6d012d7'
down_revision = '56f989faf627'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
