"""removed one table 

Revision ID: 71dee55663d6
Revises: 
Create Date: 2023-10-03 23:54:53.567121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71dee55663d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pet')
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'pets', ['pet_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'pet', ['pet_id'], ['id'])

    op.create_table('pet',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('pet_type', sa.VARCHAR(length=100), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
