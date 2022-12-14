"""empty message

Revision ID: 85c2d9a52697
Revises: 
Create Date: 2022-10-12 19:56:03.557587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85c2d9a52697'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('diameter', sa.String(length=20), nullable=False),
    sa.Column('rotation_period', sa.String(length=30), nullable=False),
    sa.Column('gravity', sa.String(length=30), nullable=False),
    sa.Column('population', sa.String(length=30), nullable=False),
    sa.Column('climate', sa.String(length=30), nullable=False),
    sa.Column('terrain', sa.String(length=30), nullable=True),
    sa.Column('surface_water', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('species',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('classification', sa.String(length=20), nullable=False),
    sa.Column('designation', sa.String(length=20), nullable=False),
    sa.Column('average_height', sa.String(length=20), nullable=False),
    sa.Column('average_lifespan', sa.String(length=20), nullable=False),
    sa.Column('eye_colors', sa.String(length=20), nullable=False),
    sa.Column('hair_colors', sa.String(length=20), nullable=False),
    sa.Column('skin_colors', sa.String(length=20), nullable=False),
    sa.Column('language', sa.String(length=20), nullable=False),
    sa.Column('homeworld', sa.String(length=20), nullable=False),
    sa.Column('people', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('firstname', sa.String(length=20), nullable=False),
    sa.Column('lastname', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=8), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('username')
    )
    op.create_table('favoriteplanets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('birth_year', sa.String(length=20), nullable=False),
    sa.Column('eye_color', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('hair_color', sa.String(length=20), nullable=False),
    sa.Column('height', sa.String(length=20), nullable=False),
    sa.Column('homeworld', sa.String(length=20), nullable=False),
    sa.Column('mass', sa.String(length=20), nullable=False),
    sa.Column('skin_color', sa.String(length=20), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.Column('species_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['species_id'], ['species.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favoritepeople',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favoritepeople')
    op.drop_table('people')
    op.drop_table('favoriteplanets')
    op.drop_table('users')
    op.drop_table('species')
    op.drop_table('planets')
    # ### end Alembic commands ###
