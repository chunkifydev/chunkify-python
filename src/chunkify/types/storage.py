# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .storage_aws import StorageAws
from .storage_chunkify import StorageChunkify
from .storage_cloudflare import StorageCloudflare
from .storage_s3_compatible import StorageS3Compatible

__all__ = ["Storage"]

Storage: TypeAlias = Annotated[
    Union[StorageChunkify, StorageCloudflare, StorageAws, StorageS3Compatible], PropertyInfo(discriminator="provider")
]
