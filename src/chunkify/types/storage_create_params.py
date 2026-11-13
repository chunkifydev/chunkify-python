# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .storage_aws_create_params import StorageAwsCreateParams
from .storage_chunkify_create_params import StorageChunkifyCreateParams
from .storage_cloudflare_create_params import StorageCloudflareCreateParams
from .storage_s3_compatible_create_params import StorageS3CompatibleCreateParams

__all__ = ["StorageCreateParams", "Storage"]


class StorageCreateParams(TypedDict, total=False):
    storage: Required[Storage]
    """The parameters for creating a new storage configuration."""


Storage: TypeAlias = Union[
    StorageAwsCreateParams, StorageChunkifyCreateParams, StorageCloudflareCreateParams, StorageS3CompatibleCreateParams
]
