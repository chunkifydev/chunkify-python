# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["Token"]


class Token(BaseModel):
    id: str
    """Unique identifier of the token"""

    token: str
    """The actual token value (only returned on creation)"""

    created_at: datetime
    """Timestamp when the token was created"""

    name: str
    """Name given to the token"""

    project_id: str
    """ID of the project this token belongs to"""

    scope: str
    """Access scope of the token (e.g.project, team)"""
