# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Storage"]


class Storage(BaseModel):
    id: str
    """Unique identifier of the storage configuration"""

    bucket: str
    """Name of the storage bucket"""

    created_at: datetime
    """Created at timestamp"""

    location: Literal["US", "EU", "Asia"]
    """Continent location of the storage"""

    provider: Literal["aws", "chunkify", "cloudflare"]
    """Name of the storage provider"""

    public: bool
    """Whether the storage bucket is publicly accessible"""

    region: str
    """Geographic region where the storage is located"""

    slug: str
    """Unique identifier of the storage configuration"""

    endpoint: Optional[str] = None
    """Endpoint of the storage provider"""
