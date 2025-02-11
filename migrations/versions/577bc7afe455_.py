"""empty message

Revision ID: 577bc7afe455
Revises: 4ca7c43eca35
Create Date: 2023-03-13 01:41:17.667692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '577bc7afe455'
down_revision = '4ca7c43eca35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('added_properties', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.Integer(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('added_properties', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=80),
               existing_nullable=True)

    # ### end Alembic commands ###
