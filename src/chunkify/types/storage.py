# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Storage"]


class Storage(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the storage configuration"""

    bucket: Optional[str] = None
    """Name of the storage bucket"""

    created_at: Optional[str] = None
    """Created at timestamp"""

    endpoint: Optional[str] = None
    """Endpoint of the storage provider"""

    location: Optional[str] = None
    """Continent location of the storage (eg. US, EU, ASIA)"""

    provider: Optional[str] = None
    """Name of the storage provider (e.g. AWS, GCP)"""

    public: Optional[bool] = None
    """Whether the storage bucket is publicly accessible"""

    region: Optional[str] = None
    """Geographic region where the storage is located"""

    slug: Optional[str] = None
    """Unique identifier of the storage configuration"""
