#
# This file is part of Invenio.
# Copyright (C) 2016-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Add refresh token to remote token table"""
from datetime import datetime

import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6da996f1c609'
down_revision = 'bff1f190b9bd'
branch_labels = ()
depends_on = None


def upgrade():
    """Upgrade database."""
    current_date = datetime.utcnow()

    # Add 'refresh_token' column to RemoteToken
    op.add_column('oauthclient_remotetoken', sa.Column('refresh_token', sqlalchemy_utils.EncryptedType()))


def downgrade():
    """Downgrade database."""
    # Remove 'refresh_token' column
    op.drop_column('oauthclient_remotetoken', 'refresh_token')
