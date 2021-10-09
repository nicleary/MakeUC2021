"""Initial datatables
Revision ID: 5806179c97f8
Revises: 
Create Date: 2021-10-09 14:44:39.426860
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = '5806179c97f8'
down_revision = None
branch_labels = None
depends_on = None
def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prov_state',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('region',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('specificity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('terrorist_act',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('approx_date', sa.String(length=64), nullable=True),
    sa.Column('extended', sa.Boolean(), nullable=False),
    sa.Column('resolution', sa.Integer(), nullable=True),
    sa.Column('country', sa.Integer(), nullable=True),
    sa.Column('region', sa.Integer(), nullable=True),
    sa.Column('prov_state', sa.Integer(), nullable=True),
    sa.Column('city', sa.Integer(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('specificity', sa.Integer(), nullable=False),
    sa.Column('vicinity', sa.Boolean(), nullable=True),
    sa.Column('location', sa.Integer(), nullable=False),
    sa.Column('summary', sa.String(length=4096), nullable=True),
    sa.ForeignKeyConstraint(['city'], ['city.id'], ),
    sa.ForeignKeyConstraint(['country'], ['country.id'], ),
    sa.ForeignKeyConstraint(['location'], ['location.id'], ),
    sa.ForeignKeyConstraint(['prov_state'], ['prov_state.id'], ),
    sa.ForeignKeyConstraint(['region'], ['region.id'], ),
    sa.ForeignKeyConstraint(['specificity'], ['specificity.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('terrorist_act')
    op.drop_table('specificity')
    op.drop_table('region')
    op.drop_table('prov_state')
    op.drop_table('location')
    op.drop_table('country')
    op.drop_table('city')
    # ### end Alembic commands ###