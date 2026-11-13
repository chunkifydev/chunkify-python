# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .chunkify_region import ChunkifyRegion

__all__ = ["StorageChunkify"]


class StorageChunkify(BaseModel):
    id: str
    """Unique identifier of the storage configuration"""

    created_at: datetime
    """Created at timestamp"""

    provider: Literal["chunkify"]
    """Provider specifies the storage provider."""

    region: ChunkifyRegion
    """Region specifies the region of the storage provider."""

    slug: str
    """Unique identifier of the storage configuration"""
