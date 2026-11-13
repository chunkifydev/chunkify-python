# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["MetricsAssetStreaming"]


class MetricsAssetStreaming(BaseModel):
    """Streaming output distribution on completed Assets."""

    asset_count: int
    """
    AssetCount specifies completed Assets, including those with no streaming
    renditions.
    """

    assets_by_highest_resolution: Dict[str, int]
    """
    AssetsByHighestResolution specifies counts by highest measured streaming
    resolution. Keys are up_to_576, 577_to_720, 721_to_1080, 1081_to_2159, 2160_plus
    and unknown, using the shorter pixel edge.
    """

    rendition_count: int
    """RenditionCount specifies streaming renditions on completed Assets."""

    renditions_per_asset: Optional[float] = None
    """RenditionsPerAsset specifies rendition_count divided by asset_count.

    Null when no completed Assets exist.
    """
