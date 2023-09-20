"""tirando telefone e end

Revision ID: 2bd5b5095977
Revises: 69e338a09e17
Create Date: 2023-09-20 14:05:52.971205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bd5b5095977'
down_revision = '69e338a09e17'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'telefone')
    op.drop_column('usuario', 'endereco')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('endereco', sa.VARCHAR(), nullable=True))
    op.add_column('usuario', sa.Column('telefone', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
