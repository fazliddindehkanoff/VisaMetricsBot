"""message

Revision ID: fe2268005501
Revises: 5438aca558ab
Create Date: 2023-03-01 23:52:13.929028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe2268005501'
down_revision = '5438aca558ab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('ordered', sa.Boolean(), nullable=True))
    op.add_column('customers', sa.Column('plan', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customers', 'plan')
    op.drop_column('customers', 'ordered')
    # ### end Alembic commands ###
