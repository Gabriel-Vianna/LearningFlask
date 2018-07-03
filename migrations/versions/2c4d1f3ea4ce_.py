"""empty message

Revision ID: 2c4d1f3ea4ce
Revises: 95d6dcbc4e8b
Create Date: 2018-06-30 18:46:52.942858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c4d1f3ea4ce'
down_revision = '95d6dcbc4e8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'article', type_='foreignkey')
    op.drop_constraint(None, 'article', type_='foreignkey')
    op.drop_column('article', 'slug')
    op.drop_column('article', 'last_modified')
    op.drop_column('article', 'published_date')
    op.drop_column('article', 'author_id')
    op.drop_column('article', 'category_id')
    op.drop_column('article', 'published')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('published', sa.VARCHAR(length=50), nullable=False))
    op.add_column('article', sa.Column('category_id', sa.INTEGER(), nullable=False))
    op.add_column('article', sa.Column('author_id', sa.INTEGER(), nullable=False))
    op.add_column('article', sa.Column('published_date', sa.DATETIME(), nullable=False))
    op.add_column('article', sa.Column('last_modified', sa.VARCHAR(length=50), nullable=False))
    op.add_column('article', sa.Column('slug', sa.VARCHAR(length=50), nullable=False))
    op.create_foreign_key(None, 'article', 'author', ['author_id'], ['id'])
    op.create_foreign_key(None, 'article', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###