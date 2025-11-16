# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Project"]


class Project(BaseModel):
    id: Optional[str] = None
    """Id is the unique identifier for the project."""

    created_at: Optional[str] = None
    """Timestamp when the project was created"""

    name: Optional[str] = None
    """Name of the project"""

    slug: Optional[str] = None
    """Slug is the slug for the project."""

    storage_id: Optional[str] = None
    """StorageId identifier where project files are stored"""
