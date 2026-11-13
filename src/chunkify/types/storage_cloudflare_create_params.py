# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StorageCloudflareCreateParams"]


class StorageCloudflareCreateParams(TypedDict, total=False):
    """Storage parameters for Cloudflare R2 storage."""

    access_key_id: Required[str]
    """AccessKeyId is the access key for the storage provider."""

    bucket: Required[str]
    """Bucket is the name of the storage bucket."""

    endpoint: Required[str]
    """Endpoint is the endpoint of the storage provider."""

    location: Required[Literal["US", "EU", "ASIA"]]
    """Location specifies the location of the storage provider."""

    provider: Required[Literal["cloudflare"]]
    """Provider specifies the storage provider."""

    region: Required[Literal["auto"]]
    """Region must be set to 'auto'."""

    secret_access_key: Required[str]
    """SecretAccessKey is the secret key for the storage provider."""

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
    """Public indicates whether the storage is publicly accessible."""
