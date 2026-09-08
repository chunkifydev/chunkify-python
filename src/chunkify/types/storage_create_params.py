# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["StorageCreateParams", "Storage", "StorageAws", "StorageChunkify", "StorageCloudflare"]


class StorageCreateParams(TypedDict, total=False):
    storage: Required[Storage]
    """The parameters for creating a new storage configuration."""


class StorageAws(TypedDict, total=False):
    """Storage parameters for AWS S3 storage."""

    access_key_id: Required[str]
    """AccessKeyId is the access key for the storage provider.

    Required if not using Chunkify storage.
    """

    bucket: Required[str]
    """Bucket is the name of the storage bucket."""

    provider: Required[Literal["aws"]]
    """Provider specifies the storage provider."""

    region: Required[
        Literal[
            "us-east-1",
            "us-east-2",
            "us-central-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "eu-north-1",
            "ap-east-1",
            "ap-east-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
        ]
    ]
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


class StorageChunkify(TypedDict, total=False):
    """Storage parameters for Chunkify ephemeral storage."""

    provider: Required[Literal["chunkify"]]
    """Provider specifies the storage provider."""

    region: Required[
        Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "ap-northeast-1",
            "ap-southeast-1",
        ]
    ]
    """Region specifies the region of the storage provider."""

    cdn_base_url: Optional[str]
    """Unsupported for Chunkify-managed temporary storage.

    Requests that provide this field are rejected.
    """


class StorageCloudflare(TypedDict, total=False):
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


Storage: TypeAlias = Union[StorageAws, StorageChunkify, StorageCloudflare]
