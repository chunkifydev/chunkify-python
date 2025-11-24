# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    id: str
    """Id is the unique identifier for the project."""

    name: str
    """Name of the project"""

    slug: str
    """Slug is the slug for the project."""

    storage_id: str
    """StorageId identifier where project files are stored"""

    created_at: Optional[datetime] = None
    """Timestamp when the project was created"""
