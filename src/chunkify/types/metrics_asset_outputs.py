# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MetricsAssetOutputs"]


class MetricsAssetOutputs(BaseModel):
    """Measured output sizes for completed Assets.

    Sample counts describe measurement coverage.
    """

    measured_asset_count: int
    """
    MeasuredAssetCount specifies completed Assets with at least one measured
    rendition.
    """

    static_bytes: Optional[int] = None
    """StaticBytes specifies the sum of measured ready static rendition sizes.

    Null when no measurements exist.
    """

    static_sample_count: int
    """StaticSampleCount specifies ready static renditions with measured sizes."""

    streaming_bytes: Optional[int] = None
    """StreamingBytes specifies the sum of measured streaming rendition sizes.

    Null when no measurements exist.
    """

    streaming_sample_count: int
    """StreamingSampleCount specifies streaming renditions with measured sizes."""
