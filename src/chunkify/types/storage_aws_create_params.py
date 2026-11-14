# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .aws_region import AwsRegion

__all__ = ["StorageAwsCreateParams"]


class StorageAwsCreateParams(TypedDict, total=False):
    """Storage parameters for AWS S3 storage."""

    access_key_id: Required[str]
    """AccessKeyId is the access key for the storage provider.

    Required if not using Chunkify storage.
    """

    bucket: Required[str]
    """Bucket is the name of the storage bucket."""

    provider: Required[Literal["aws"]]
    """Provider specifies the storage provider."""

    region: Required[AwsRegion]
    """Region specifies the region of the storage provider."""

    secret_access_key: Required[str]
    """SecretAccessKey is the secret key for the storage provider.

    Required if not using Chunkify storage.
    """

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
