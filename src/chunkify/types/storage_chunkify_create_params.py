# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .chunkify_region import ChunkifyRegion

__all__ = ["StorageChunkifyCreateParams"]


class StorageChunkifyCreateParams(TypedDict, total=False):
    """Storage parameters for Chunkify ephemeral storage."""

    provider: Required[Literal["chunkify"]]
    """Provider specifies the storage provider."""

    region: Required[ChunkifyRegion]
    """Region specifies the region of the storage provider."""

    cdn_base_url: Optional[str]
    """Unsupported for Chunkify-managed temporary storage.

    Requests that provide this field are rejected.
    """
