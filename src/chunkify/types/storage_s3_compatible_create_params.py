# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .storage_location import StorageLocation

__all__ = ["StorageS3CompatibleCreateParams"]


class StorageS3CompatibleCreateParams(TypedDict, total=False):
    """
    Storage parameters for a public S3-compatible service such as MinIO, Wasabi, or Backblaze B2.
    """

    access_key_id: Required[str]
    """Access key for the storage provider."""

    bucket: Required[str]
    """Bucket is the name of the storage bucket."""

    endpoint: Required[str]
    """Public HTTPS origin for the S3-compatible service.

    Credentials, paths, queries, fragments, and non-public destinations are
    rejected.
    """

    location: Required[StorageLocation]
    """Chunkify workload location.

    It controls where Chunkify processes the workload and is independent from the
    provider region.
    """

    provider: Required[Literal["s3_compatible"]]
    """Stable provider identifier for generic S3-compatible storage."""

    region: Required[str]
    """Explicit provider region used for S3 request signing.

    Vendor-specific identifiers are accepted.
    """

    secret_access_key: Required[str]
    """Secret key for the storage provider."""

    base_prefix: str
    """Object-key prefix for final job outputs.

    The API normalizes it without a leading slash and with one trailing slash. Omit
    it or send an empty string to use the bucket root.
    """

    cdn_base_url: Optional[str]
    """Optional customer-managed HTTPS delivery origin.

    It must not contain credentials, a path, query string, or fragment.
    """

    public: bool
    """Whether the bucket is publicly readable."""
