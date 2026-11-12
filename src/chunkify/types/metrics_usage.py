# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MetricsUsage",
    "Daily",
    "DailyAssets",
    "DailyCaptions",
    "DailyCreditsSpent",
    "DailyEgress",
    "DailyNotifications",
    "DailySources",
    "DailyStaticRenditions",
    "DailyThumbnails",
    "DailyTranscodings",
    "DailyUploads",
    "Summary",
    "SummaryAssets",
    "SummaryCaptions",
    "SummaryCreditsSpent",
    "SummaryEgress",
    "SummaryNotifications",
    "SummarySources",
    "SummaryStaticRenditions",
    "SummaryThumbnails",
    "SummaryTranscodings",
    "SummaryUploads",
]


class DailyAssets(BaseModel):
    """Asset processing usage."""

    failed: int
    """Failed specifies recorded failed Asset outcomes."""

    input_seconds: int
    """InputSeconds specifies settled billable Asset input duration."""

    input_seconds_by_resolution: Dict[str, int]
    """Video duration in seconds by pricing resolution tier: sd, hd, 2k and uhd."""

    ready: int
    """Ready specifies recorded successful Asset outcomes."""


class DailyCaptions(BaseModel):
    """Caption processing usage."""

    transcription_seconds: int
    """TranscriptionSeconds specifies audio duration transcribed."""

    translation_seconds: int
    """
    TranslationSeconds specifies caption duration translated, counted once per
    target language.
    """


class DailyCreditsSpent(BaseModel):
    """Settled credits in integer units, with 10000 units equal to USD 1 of credits.

    Category values are parts of total, not additional charges.
    """

    assets: int
    """Amount specifies settled credits spent on assets.

    Integer units; 10000 units equal USD 1 of credits.
    """

    egress: int
    """Amount specifies settled credits spent on egress.

    Integer units; 10000 units equal USD 1 of credits.
    """

    static_renditions: int
    """Amount specifies settled credits spent on static renditions.

    Integer units; 10000 units equal USD 1 of credits.
    """

    thumbnails: int
    """Amount specifies settled credits spent on thumbnails.

    Integer units; 10000 units equal USD 1 of credits.
    """

    total: int
    """Total specifies the sum of these media-processing and output-egress charges.

    Integer units; 10000 units equal USD 1 of credits.
    """

    transcodings: int
    """Amount specifies settled credits spent on transcodings.

    Integer units; 10000 units equal USD 1 of credits.
    """

    transcription: int
    """Amount specifies settled credits spent on transcription.

    Integer units; 10000 units equal USD 1 of credits.
    """

    translation: int
    """Amount specifies settled credits spent on translation.

    Integer units; 10000 units equal USD 1 of credits.
    """


class DailyEgress(BaseModel):
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


class DailyNotifications(BaseModel):
    """Webhook delivery activity."""

    failed: int
    """Failed specifies recorded failed webhook delivery attempts."""

    sent: int
    """Sent specifies recorded successful webhook deliveries."""


class DailySources(BaseModel):
    """Source ingestion activity."""

    bytes: int
    """
    Bytes specifies cumulative ingested Source bytes, not current storage occupancy.
    """

    created: int
    """Created specifies the number of ingested Sources."""

    ingested_seconds: int
    """IngestedSeconds specifies ingested media duration in seconds."""


class DailyStaticRenditions(BaseModel):
    """Static rendition usage."""

    audio_output_seconds: int
    """AudioOutputSeconds specifies the audio-only subset of output_seconds."""

    output_seconds: int
    """
    OutputSeconds specifies settled billable output duration, including audio-only
    output.
    """

    output_seconds_by_resolution: Dict[str, int]
    """Video duration in seconds by pricing resolution tier.

    Contains sd, hd, 2k and uhd keys; audio is reported separately.
    """


class DailyThumbnails(BaseModel):
    """Thumbnail processing usage."""

    images_published: int
    """ImagesPublished specifies the number of published thumbnail images."""

    sets_failed: int
    """SetsFailed specifies recorded failed Thumbnail requests."""

    sets_ready: int
    """SetsReady specifies recorded successful Thumbnail requests."""


class DailyTranscodings(BaseModel):
    """Standalone Transcoding usage."""

    audio_output_seconds: int
    """AudioOutputSeconds specifies the audio-only subset of output_seconds."""

    failed: int
    """Failed specifies recorded failed Transcoding outcomes."""

    output_seconds: int
    """
    OutputSeconds specifies settled billable output duration, including audio-only
    output.
    """

    output_seconds_by_resolution: Dict[str, int]
    """Video duration in seconds by pricing resolution tier.

    Contains sd, hd, 2k and uhd keys; audio is reported separately.
    """

    ready: int
    """Ready specifies recorded successful Transcoding outcomes."""


class DailyUploads(BaseModel):
    """Upload activity."""

    bytes: int
    """Bytes specifies successfully uploaded bytes."""

    completed: int
    """Completed specifies successfully completed Uploads."""

    failed: int
    """Failed specifies recorded failed Uploads."""


class Daily(BaseModel):
    """Daily recorded usage. Inactive days contain zero counters."""

    assets: DailyAssets
    """Asset processing usage."""

    captions: DailyCaptions
    """Caption processing usage."""

    credits_spent: DailyCreditsSpent
    """Settled credits in integer units, with 10000 units equal to USD 1 of credits.

    Category values are parts of total, not additional charges.
    """

    date: str
    """Date specifies the UTC accounting day."""

    egress: DailyEgress
    """Recorded output egress eligible for the transfer tariff.

    Provider-exempt transfers are excluded.
    """

    notifications: DailyNotifications
    """Webhook delivery activity."""

    sources: DailySources
    """Source ingestion activity."""

    static_renditions: DailyStaticRenditions
    """Static rendition usage."""

    thumbnails: DailyThumbnails
    """Thumbnail processing usage."""

    transcodings: DailyTranscodings
    """Standalone Transcoding usage."""

    uploads: DailyUploads
    """Upload activity."""


class SummaryAssets(BaseModel):
    """Asset processing usage."""

    failed: int
    """Failed specifies recorded failed Asset outcomes."""

    input_seconds: int
    """InputSeconds specifies settled billable Asset input duration."""

    input_seconds_by_resolution: Dict[str, int]
    """Video duration in seconds by pricing resolution tier: sd, hd, 2k and uhd."""

    ready: int
    """Ready specifies recorded successful Asset outcomes."""


class SummaryCaptions(BaseModel):
    """Caption processing usage."""

    transcription_seconds: int
    """TranscriptionSeconds specifies audio duration transcribed."""

    translation_seconds: int
    """
    TranslationSeconds specifies caption duration translated, counted once per
    target language.
    """


class SummaryCreditsSpent(BaseModel):
    """Settled credits in integer units, with 10000 units equal to USD 1 of credits.

    Category values are parts of total, not additional charges.
    """

    assets: int
    """Amount specifies settled credits spent on assets.

    Integer units; 10000 units equal USD 1 of credits.
    """

    egress: int
    """Amount specifies settled credits spent on egress.

    Integer units; 10000 units equal USD 1 of credits.
    """

    static_renditions: int
    """Amount specifies settled credits spent on static renditions.

    Integer units; 10000 units equal USD 1 of credits.
    """

    thumbnails: int
    """Amount specifies settled credits spent on thumbnails.

    Integer units; 10000 units equal USD 1 of credits.
    """

    total: int
    """Total specifies the sum of these media-processing and output-egress charges.

    Integer units; 10000 units equal USD 1 of credits.
    """

    transcodings: int
    """Amount specifies settled credits spent on transcodings.

    Integer units; 10000 units equal USD 1 of credits.
    """

    transcription: int
    """Amount specifies settled credits spent on transcription.

    Integer units; 10000 units equal USD 1 of credits.
    """

    translation: int
    """Amount specifies settled credits spent on translation.

    Integer units; 10000 units equal USD 1 of credits.
    """


class SummaryEgress(BaseModel):
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


class SummaryNotifications(BaseModel):
    """Webhook delivery activity."""

    failed: int
    """Failed specifies recorded failed webhook delivery attempts."""

    sent: int
    """Sent specifies recorded successful webhook deliveries."""


class SummarySources(BaseModel):
    """Source ingestion activity."""

    bytes: int
    """
    Bytes specifies cumulative ingested Source bytes, not current storage occupancy.
    """

    created: int
    """Created specifies the number of ingested Sources."""

    ingested_seconds: int
    """IngestedSeconds specifies ingested media duration in seconds."""


class SummaryStaticRenditions(BaseModel):
    """Static rendition usage."""

    audio_output_seconds: int
    """AudioOutputSeconds specifies the audio-only subset of output_seconds."""

    output_seconds: int
    """
    OutputSeconds specifies settled billable output duration, including audio-only
    output.
    """

    output_seconds_by_resolution: Dict[str, int]
    """Video duration in seconds by pricing resolution tier.

    Contains sd, hd, 2k and uhd keys; audio is reported separately.
    """


class SummaryThumbnails(BaseModel):
    """Thumbnail processing usage."""

    images_published: int
    """ImagesPublished specifies the number of published thumbnail images."""

    sets_failed: int
    """SetsFailed specifies recorded failed Thumbnail requests."""

    sets_ready: int
    """SetsReady specifies recorded successful Thumbnail requests."""


class SummaryTranscodings(BaseModel):
    """Standalone Transcoding usage."""

    audio_output_seconds: int
    """AudioOutputSeconds specifies the audio-only subset of output_seconds."""

    failed: int
    """Failed specifies recorded failed Transcoding outcomes."""

    output_seconds: int
    """
    OutputSeconds specifies settled billable output duration, including audio-only
    output.
    """

    output_seconds_by_resolution: Dict[str, int]
    """Video duration in seconds by pricing resolution tier.

    Contains sd, hd, 2k and uhd keys; audio is reported separately.
    """

    ready: int
    """Ready specifies recorded successful Transcoding outcomes."""


class SummaryUploads(BaseModel):
    """Upload activity."""

    bytes: int
    """Bytes specifies successfully uploaded bytes."""

    completed: int
    """Completed specifies successfully completed Uploads."""

    failed: int
    """Failed specifies recorded failed Uploads."""


class Summary(BaseModel):
    """Summary specifies totals across the selected period."""

    assets: SummaryAssets
    """Asset processing usage."""

    captions: SummaryCaptions
    """Caption processing usage."""

    credits_spent: SummaryCreditsSpent
    """Settled credits in integer units, with 10000 units equal to USD 1 of credits.

    Category values are parts of total, not additional charges.
    """

    egress: SummaryEgress
    """Recorded output egress eligible for the transfer tariff.

    Provider-exempt transfers are excluded.
    """

    notifications: SummaryNotifications
    """Webhook delivery activity."""

    sources: SummarySources
    """Source ingestion activity."""

    static_renditions: SummaryStaticRenditions
    """Static rendition usage."""

    thumbnails: SummaryThumbnails
    """Thumbnail processing usage."""

    transcodings: SummaryTranscodings
    """Standalone Transcoding usage."""

    uploads: SummaryUploads
    """Upload activity."""


class MetricsUsage(BaseModel):
    """Project usage for the selected UTC accounting period."""

    daily: List[Daily]
    """Daily specifies one record for every selected day, oldest first."""

    from_: str = FieldInfo(alias="from")
    """From specifies the inclusive UTC start date."""

    summary: Summary
    """Summary specifies totals across the selected period."""

    to: str
    """To specifies the exclusive UTC end date."""
