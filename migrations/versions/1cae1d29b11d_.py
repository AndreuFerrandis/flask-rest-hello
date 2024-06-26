"""empty message

Revision ID: 1cae1d29b11d
Revises: c371ede3fa86
Create Date: 2024-04-24 19:09:48.684485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cae1d29b11d'
down_revision = 'c371ede3fa86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_name', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('people_name', sa.Integer(), nullable=True))
        batch_op.drop_constraint('favorite_people_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorite_user_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('favorite_planet_id_fkey', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite', schema=None) as batch_op:
        batch_op.create_foreign_key('favorite_planet_id_fkey', 'planet', ['planet_id'], ['id'])
        batch_op.create_foreign_key('favorite_user_id_fkey', 'user', ['user_id'], ['id'])
        batch_op.create_foreign_key('favorite_people_id_fkey', 'people', ['people_id'], ['id'])
        batch_op.drop_column('people_name')
        batch_op.drop_column('planet_name')

    # ### end Alembic commands ###
