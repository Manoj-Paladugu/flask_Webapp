""" new fields in user model

Revision ID: 730847070b0a
Revises: 16e67f07505d
Create Date: 2018-07-01 00:01:10.224473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '730847070b0a'
down_revision = '16e67f07505d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
