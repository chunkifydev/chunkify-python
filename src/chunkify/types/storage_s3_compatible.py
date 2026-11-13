# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .storage_location import StorageLocation

__all__ = ["StorageS3Compatible"]


class StorageS3Compatible(BaseModel):
    """A customer-owned storage connection using the standard S3 API."""

    id: str
    """Unique identifier of the storage configuration"""

    addressing_style: Literal["virtual", "path"]
    """
    Addressing style detected during connection validation and used for later S3
    operations.
    """

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
    """Public HTTPS origin for the S3-compatible service.

    Credentials, paths, queries, fragments, and non-public destinations are
    rejected.
    """

    location: StorageLocation
    """Chunkify workload location.

    This is independent from the provider signing region.
    """

    provider: Literal["s3_compatible"]
    """Stable provider identifier for generic S3-compatible storage."""

    public: bool
    """Public indicates whether the storage is publicly accessible."""

    region: str
    """Provider region used for S3 request signing.

    This is independent from the Chunkify workload location.
    """

    slug: str
    """Unique identifier of the storage configuration"""

    cdn_base_url: Optional[str] = None
    """
    Optional customer-managed HTTPS delivery origin used to build stable CDN URLs
    for objects in this storage.
    """
