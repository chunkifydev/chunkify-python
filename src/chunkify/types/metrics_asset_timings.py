# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MetricsAssetTimings"]


class MetricsAssetTimings(BaseModel):
    """Lifecycle timing measurements.

    Period medians use all samples, not averages of daily medians.
    """

    completion_median_seconds: Optional[float] = None
    """
    CompletionMedianSeconds specifies the median elapsed time from creation to full
    readiness. Null when no samples exist.
    """

    completion_sample_count: int
    """CompletionSampleCount specifies Assets with a full readiness measurement."""

    playback_median_seconds: Optional[float] = None
    """
    PlaybackMedianSeconds specifies the median elapsed time from creation to
    playback readiness. Null when no samples exist.
    """

    playback_sample_count: int
    """PlaybackSampleCount specifies Assets with a playback readiness measurement."""
