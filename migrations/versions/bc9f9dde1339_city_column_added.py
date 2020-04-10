"""city column added

Revision ID: bc9f9dde1339
Revises: dd9d97f581a0
Create Date: 2020-04-06 23:56:00.633686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc9f9dde1339'
down_revision = 'dd9d97f581a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blood_banks', sa.Column('city', sa.String(length=65), nullable=False))
    op.create_index(op.f('ix_blood_banks_city'), 'blood_banks', ['city'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blood_banks_city'), table_name='blood_banks')
    op.drop_column('blood_banks', 'city')
    # ### end Alembic commands ###