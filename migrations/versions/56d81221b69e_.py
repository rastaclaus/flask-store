"""empty message

Revision ID: 56d81221b69e
Revises: 
Create Date: 2020-02-22 00:27:59.386614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56d81221b69e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_category_name'), 'product_category', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_category_name'), table_name='product_category')
    op.drop_table('product_category')
    # ### end Alembic commands ###