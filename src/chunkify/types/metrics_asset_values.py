# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .metrics_asset_counts import MetricsAssetCounts
from .metrics_asset_outputs import MetricsAssetOutputs
from .metrics_asset_sources import MetricsAssetSources
from .metrics_asset_timings import MetricsAssetTimings
from .metrics_asset_streaming import MetricsAssetStreaming

__all__ = ["MetricsAssetValues"]


class MetricsAssetValues(BaseModel):
    """Asset measurements for a creation-date cohort."""

    assets: MetricsAssetCounts
    """Asset outcomes grouped by Asset creation date."""

    outputs: MetricsAssetOutputs
    """Measured output sizes for completed Assets.

    Sample counts describe measurement coverage.
    """

    sources: MetricsAssetSources
    """Source profiles count Assets, not unique Sources."""

    streaming: MetricsAssetStreaming
    """Streaming output distribution on completed Assets."""

    timings: MetricsAssetTimings
    """Lifecycle timing measurements.

    Period medians use all samples, not averages of daily medians.
    """
