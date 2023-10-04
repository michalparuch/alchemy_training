"""moja 4 migracja

Revision ID: 805c5f4bac4d
Revises: b74656e462b6
Create Date: 2023-04-20 19:13:17.124596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '805c5f4bac4d'
down_revision = 'b74656e462b6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gry', sa.Column('test', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gry', 'test')
    # ### end Alembic commands ###