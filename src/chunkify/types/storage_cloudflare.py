# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .storage_location import StorageLocation

__all__ = ["StorageCloudflare"]


class StorageCloudflare(BaseModel):
    id: str
    """Unique identifier of the storage configuration"""

    base_prefix: str
    """
    Canonical object-key prefix prepended to every final job output in this
    customer-owned storage. An empty string means the bucket root.
    """

    bucket: str
    """Bucket is the name of the storage bucket."""

    created_at: datetime
    """Created at timestamp"""

    endpoint: str
    """Endpoint is the endpoint of the storage provider."""

    location: StorageLocation
    """Location specifies the location of the storage provider."""

    provider: Literal["cloudflare"]
    """Provider specifies the storage provider."""

    public: bool
    """Public indicates whether the storage is publicly accessible."""

    region: Literal["auto"]
    """Region specifies the region of the storage provider."""

    slug: str
    """Unique identifier of the storage configuration"""

    cdn_base_url: Optional[str] = None
    """
    Optional customer-managed HTTPS delivery origin used to build stable CDN URLs
    for objects in this storage.
    """
