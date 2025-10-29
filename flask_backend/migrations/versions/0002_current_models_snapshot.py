"""current models snapshot

Revision ID: 0002_current_models_snapshot
Revises: 0001_initial
Create Date: 2025-10-29 00:05:00.000000
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0002_current_models_snapshot'
down_revision: Union[str, None] = '0001_initial'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # No schema changes; this snapshot confirms the current model state.
    pass


def downgrade() -> None:
    # No-op; snapshot only.
    pass
