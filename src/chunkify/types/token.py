# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Token"]


class Token(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the token"""

    token: Optional[str] = None
    """The actual token value (only returned on creation)"""

    created_at: Optional[str] = None
    """Timestamp when the token was created"""

    name: Optional[str] = None
    """Name given to the token"""

    project_id: Optional[str] = None
    """ID of the project this token belongs to"""

    scope: Optional[str] = None
    """Access scope of the token (e.g.project, team)"""
