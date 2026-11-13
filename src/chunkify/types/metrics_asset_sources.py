# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["MetricsAssetSources"]


class MetricsAssetSources(BaseModel):
    """Source profiles count Assets, not unique Sources."""

    assets_by_codec: Dict[str, int]
    """
    AssetsByCodec specifies Asset counts by normalized source video codec, including
    unknown. All recorded codecs are returned.
    """

    assets_by_duration: Dict[str, int]
    """AssetsByDuration specifies Asset counts by source duration.

    Keys are under_1m, 1_to_5m, 5_to_10m, 10_to_30m, 30_to_60m, over_60m and
    unknown. Boundaries are 60, 300, 600, 1800 and 3600 seconds; exactly 3600
    belongs to 30_to_60m.
    """

    assets_by_resolution: Dict[str, int]
    """AssetsByResolution specifies Asset counts by source resolution.

    Keys are up_to_576, 577_to_720, 721_to_1080, 1081_to_2159, 2160_plus and
    unknown, using the shorter pixel edge.
    """
