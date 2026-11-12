# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MetricsAssets",
    "Daily",
    "DailyAssets",
    "DailyOutputs",
    "DailySources",
    "DailyStreaming",
    "DailyTimings",
    "Summary",
    "SummaryAssets",
    "SummaryOutputs",
    "SummarySources",
    "SummaryStreaming",
    "SummaryTimings",
]


class DailyAssets(BaseModel):
    """Asset outcomes grouped by Asset creation date."""

    completed: int
    """Completed specifies Assets with a recorded ready timestamp."""

    failed: int
    """Failed specifies retained Assets currently in failed status."""

    processed_seconds: float
    """
    ProcessedSeconds specifies measured media duration of completed Assets,
    preserving fractional seconds.
    """

    saved: int
    """Saved specifies retained Assets created in the period."""


class DailyOutputs(BaseModel):
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


class DailySources(BaseModel):
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


class DailyStreaming(BaseModel):
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


class DailyTimings(BaseModel):
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


class Daily(BaseModel):
    """Asset measurements grouped by creation day."""

    assets: DailyAssets
    """Asset outcomes grouped by Asset creation date."""

    date: str
    """Date specifies the UTC Asset creation day."""

    outputs: DailyOutputs
    """Measured output sizes for completed Assets.

    Sample counts describe measurement coverage.
    """

    sources: DailySources
    """Source profiles count Assets, not unique Sources."""

    streaming: DailyStreaming
    """Streaming output distribution on completed Assets."""

    timings: DailyTimings
    """Lifecycle timing measurements.

    Period medians use all samples, not averages of daily medians.
    """


class SummaryAssets(BaseModel):
    """Asset outcomes grouped by Asset creation date."""

    completed: int
    """Completed specifies Assets with a recorded ready timestamp."""

    failed: int
    """Failed specifies retained Assets currently in failed status."""

    processed_seconds: float
    """
    ProcessedSeconds specifies measured media duration of completed Assets,
    preserving fractional seconds.
    """

    saved: int
    """Saved specifies retained Assets created in the period."""


class SummaryOutputs(BaseModel):
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


class SummarySources(BaseModel):
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


class SummaryStreaming(BaseModel):
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


class SummaryTimings(BaseModel):
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


class Summary(BaseModel):
    """Summary specifies the complete creation-date cohort."""

    assets: SummaryAssets
    """Asset outcomes grouped by Asset creation date."""

    outputs: SummaryOutputs
    """Measured output sizes for completed Assets.

    Sample counts describe measurement coverage.
    """

    sources: SummarySources
    """Source profiles count Assets, not unique Sources."""

    streaming: SummaryStreaming
    """Streaming output distribution on completed Assets."""

    timings: SummaryTimings
    """Lifecycle timing measurements.

    Period medians use all samples, not averages of daily medians.
    """


class MetricsAssets(BaseModel):
    """Measurements saved on retained Assets.

    Explicit deletion can change historical results; temporary media cleanup does not erase saved Asset measurements.
    """

    daily: List[Daily]
    """Daily specifies one record for each selected creation day, oldest first."""

    from_: str = FieldInfo(alias="from")
    """From specifies the inclusive UTC start date."""

    summary: Summary
    """Summary specifies the complete creation-date cohort."""

    to: str
    """To specifies the exclusive UTC end date."""
