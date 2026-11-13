# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MetricsUsageEgress"]


class MetricsUsageEgress(BaseModel):
    """Recorded output egress eligible for the transfer tariff.

    Provider-exempt transfers are excluded.
    """

    asset_preparation_bytes: int
    """Bytes specifies tariff-eligible output transfer bytes for Asset preparation."""

    asset_rendition_bytes: int
    """Bytes specifies tariff-eligible output transfer bytes for streaming renditions."""

    billable_bytes: int
    """BillableBytes specifies external output bytes charged after the allowance."""

    caption_bytes: int
    """Bytes specifies tariff-eligible output transfer bytes for captions."""

    included_bytes: int
    """IncludedBytes specifies external output bytes covered by the allowance."""

    static_rendition_bytes: int
    """Bytes specifies tariff-eligible output transfer bytes for static renditions."""

    thumbnail_bytes: int
    """Bytes specifies tariff-eligible output transfer bytes for Thumbnails."""

    total_bytes: int
    """TotalBytes specifies the sum of tariff-eligible output transfers."""

    transcoding_bytes: int
    """Bytes specifies tariff-eligible output transfer bytes for Transcodings."""
