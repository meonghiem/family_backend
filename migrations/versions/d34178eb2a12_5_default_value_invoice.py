"""5. default value invoice

Revision ID: d34178eb2a12
Revises: 7391cb24b16a
Create Date: 2023-09-17 12:08:44.679144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


# revision identifiers, used by Alembic.
revision: str = 'd34178eb2a12'
down_revision: Union[str, None] = '7391cb24b16a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('invoice', 'total_amount', server_default="0", nullable=False, existing_type=mysql.DOUBLE(asdecimal=True))
    op.alter_column('invoice_detail', 'total', server_default="0", nullable=False, existing_type=mysql.DOUBLE(asdecimal=True))
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('invoice', 'total_amount', server_default=None, nullable=False, existing_type=mysql.DOUBLE(asdecimal=True))
    op.alter_column('invoice_detail', 'total', server_default=None, nullable=False, existing_type=mysql.DOUBLE(asdecimal=True))
    pass
    # ### end Alembic commands ###
