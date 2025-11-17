# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Storage"]


class Storage(BaseModel):
    id: str
    """Unique identifier of the storage configuration"""

    bucket: str
    """Name of the storage bucket"""

    created_at: str
    """Created at timestamp"""

    endpoint: str
    """Endpoint of the storage provider"""

    location: str
    """Continent location of the storage (eg. US, EU, ASIA)"""

    provider: str
    """Name of the storage provider (e.g. AWS, GCP)"""

    public: bool
    """Whether the storage bucket is publicly accessible"""

    region: str
    """Geographic region where the storage is located"""

    slug: str
    """Unique identifier of the storage configuration"""
