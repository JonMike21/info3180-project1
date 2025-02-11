"""empty message

Revision ID: 4ca7c43eca35
Revises: 
Create Date: 2023-03-08 23:11:58.776575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ca7c43eca35'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('added_properties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.Column('bedroomNum', sa.Integer(), nullable=True),
    sa.Column('bathroomNum', sa.Integer(), nullable=True),
    sa.Column('price', sa.String(length=80), nullable=True),
    sa.Column('type', sa.String(length=80), nullable=True),
    sa.Column('location', sa.String(length=80), nullable=True),
    sa.Column('photo', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('added_properties')
    # ### end Alembic commands ###
