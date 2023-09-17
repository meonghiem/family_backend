"""4. modify quantity column of invoice detail table

Revision ID: 7391cb24b16a
Revises: 323269e09494
Create Date: 2023-09-17 00:47:31.330224

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7391cb24b16a'
down_revision: Union[str, None] = '323269e09494'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('invoice_detail', 'quantity',type_=sa.Double(), nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('invoice_detail', 'quantity',type_=sa.Integer(), nullable=False)
    pass
    # ### end Alembic commands ###