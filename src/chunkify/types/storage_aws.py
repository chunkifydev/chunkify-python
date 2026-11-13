# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .aws_region import AwsRegion

__all__ = ["StorageAws"]


class StorageAws(BaseModel):
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

    provider: Literal["aws"]
    """Provider specifies the storage provider."""

    public: bool
    """Public indicates whether the storage is publicly accessible."""

    region: AwsRegion
    """Region specifies the region of the storage provider."""

    slug: str
    """Unique identifier of the storage configuration"""

    cdn_base_url: Optional[str] = None
    """
    Optional customer-managed HTTPS delivery origin used to build stable CDN URLs
    for objects in this storage.
    """
