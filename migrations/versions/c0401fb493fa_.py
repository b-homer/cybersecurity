"""empty message

Revision ID: c0401fb493fa
Revises: 33a67e7296eb
Create Date: 2020-03-23 15:22:51.748428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0401fb493fa'
down_revision = '33a67e7296eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('tagline', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'tagline')
    # ### end Alembic commands ###