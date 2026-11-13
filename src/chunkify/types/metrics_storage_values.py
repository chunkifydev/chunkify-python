# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MetricsStorageValues"]


class MetricsStorageValues(BaseModel):
    """Recorded storage activity in bytes."""

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
