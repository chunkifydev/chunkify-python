# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MetricsStorage", "Storage", "StorageDaily", "StorageSummary"]


class StorageDaily(BaseModel):
    """Recorded storage activity grouped by event day."""

    asset_bytes_added: int
    """AssetBytesAdded specifies recorded Asset package additions."""

    bytes_removed: int
    """BytesRemoved specifies recorded successful file removals as a positive amount."""

    date: str
    """Date specifies the UTC event day."""

    net_bytes_change: int
    """NetBytesChange specifies additions minus successful removals.

    This may be negative and is not bucket occupancy.
    """

    source_bytes_added: int
    """SourceBytesAdded specifies recorded Source additions."""

    static_rendition_bytes_added: int
    """StaticRenditionBytesAdded specifies recorded static rendition additions."""


class StorageSummary(BaseModel):
    """Summary specifies recorded activity in the selected period."""

    asset_bytes_added: int
    """AssetBytesAdded specifies recorded Asset package additions."""

    bytes_removed: int
    """BytesRemoved specifies recorded successful file removals as a positive amount."""

    net_bytes_change: int
    """NetBytesChange specifies additions minus successful removals.

    This may be negative and is not bucket occupancy.
    """

    source_bytes_added: int
    """SourceBytesAdded specifies recorded Source additions."""

    static_rendition_bytes_added: int
    """StaticRenditionBytesAdded specifies recorded static rendition additions."""


class Storage(BaseModel):
    """Activity for one persistent storage configuration."""

    daily: List[StorageDaily]
    """Daily specifies one record for each selected event day, oldest first."""

    storage_id: str
    """StorageId identifies the persistent storage configuration."""

    summary: StorageSummary
    """Summary specifies recorded activity in the selected period."""


class MetricsStorage(BaseModel):
    """Recorded additions and successful removals within event retention.

    Excludes external storage changes and does not measure current storage size.
    """

    from_: str = FieldInfo(alias="from")
    """From specifies the inclusive UTC start date."""

    storages: List[Storage]
    """
    Storages specifies persistent project storage configurations, including those
    without recorded activity. Chunkify temporary storage is excluded.
    """

    to: str
    """To specifies the exclusive UTC end date."""
