# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..thumbnail import Thumbnail

__all__ = [
    "AssetOutput",
    "AssetCaptionOutput",
    "AssetCaptionOutputDetails",
    "AssetCaptionOutputDetailsError",
    "AssetStaticRenditionOutput",
    "AssetStaticRenditionOutputDetails",
    "AssetStaticRenditionOutputDetailsError",
    "AssetStaticRenditionOutputDetailsProgress",
    "AssetThumbnailOutput",
    "AssetTranscriptOutput",
    "AssetTranscriptOutputDetails",
    "AssetTranscriptOutputDetailsContent",
    "AssetTranscriptOutputDetailsContentSegment",
    "AssetTranscriptOutputDetailsError",
]


class AssetCaptionOutputDetailsError(BaseModel):
    """Reason caption processing failed."""

    code: str
    """Machine-readable processing error code."""

    message: str
    """Description of the processing failure."""

    stage: Literal["ingest", "analysis", "encoding", "packaging", "upload", "validation", "cleanup"]
    """Processing stage that failed."""


class AssetCaptionOutputDetails(BaseModel):
    """
    Details contains the canonical typed output resource, including its available delivery fields.
    """

    id: str
    """Unique Asset output ID, prefixed with aop\\__."""

    status: Literal["preparing", "ready", "failed", "expired"]
    """Caption processing status."""

    created_at: Optional[datetime] = None
    """Time this caption output was requested."""

    error: Optional[AssetCaptionOutputDetailsError] = None
    """Reason caption processing failed."""

    language_code: Optional[str] = None
    """Primary language of this subtitle track, such as en or fr.

    Omitted when no speech was detected or processing has not finished.
    """

    playlist_path: Optional[str] = None
    """Subtitle media playlist path in Storage. Available when speech was detected."""

    size: Optional[int] = None
    """Combined subtitle playlist and WebVTT size in bytes. Available when ready."""

    source_caption_id: Optional[str] = None
    """ID of the caption track translated to create this track.

    Omitted for speech transcription.
    """

    transcript_id: Optional[str] = None
    """
    TranscriptId identifies the original-language transcript used to generate this
    caption. Omitted for translated captions.
    """

    vtt_path: Optional[str] = None
    """WebVTT subtitle segment path in Storage. Available when speech was detected."""


class AssetCaptionOutput(BaseModel):
    """An Asset-owned caption output and its canonical resource details."""

    id: str
    """Id identifies the Asset output, prefixed with aop\\__.

    The type field identifies the output kind.
    """

    asset_id: str
    """AssetId identifies the owning Asset."""

    details: AssetCaptionOutputDetails
    """
    Details contains the canonical typed output resource, including its available
    delivery fields.
    """

    status: Literal["preparing", "ready", "failed", "expired"]
    """Status specifies the output processing state.

    Expired means temporary output files are no longer available.
    """

    type: Literal["caption"]
    """Type identifies the output kind."""


class AssetStaticRenditionOutputDetailsError(BaseModel):
    code: str
    """Machine-readable processing error code."""

    message: str
    """Description of the processing failure."""

    stage: Literal["ingest", "analysis", "encoding", "packaging", "upload", "validation", "cleanup"]
    """Processing stage that failed."""


class AssetStaticRenditionOutputDetailsProgress(BaseModel):
    """Progress specifies the current processing stage and encoding percentage.

    Omitted after processing ends.
    """

    stage: Literal["queued", "starting", "encoding", "finalizing", "uploading"]
    """Stage specifies the current preparation activity.

    Finalization and streaming publication can overlap encoding; finalizing is shown
    once encoding has completed.
    """

    percent: Optional[float] = None
    """Percent specifies the percentage of the video encoded so far.

    Present only during encoding when video duration is known. It may decrease if
    processing restarts. It does not estimate total preparation time.
    """


class AssetStaticRenditionOutputDetails(BaseModel):
    """
    Details contains the canonical typed output resource, including its available delivery fields.
    """

    id: str
    """Unique Asset output ID, prefixed with aop\\__."""

    asset_id: str
    """Parent Asset ID."""

    container: Literal["mp4"]
    """Media container."""

    created_at: datetime
    """When the rendition was created."""

    height: int
    """Output height in pixels."""

    path: str
    """MP4 path in Storage.

    Recreating the same resolution reuses this path and overwrites any retained
    file.
    """

    requested_resolution: Literal["highest", "240p", "360p", "480p", "540p", "720p", "1080p", "1440p", "2160p"]
    """Requested resolution selector."""

    resolution: str
    """Selected output resolution.

    May be smaller than 240p for small sources. Use width and height for pixel
    dimensions.
    """

    status: Literal["preparing", "ready", "failed", "expired"]
    """Processing status of this MP4, independent of streaming outputs."""

    storage_id: str
    """Storage containing this rendition, inherited from its Asset."""

    updated_at: datetime
    """When the rendition was last updated."""

    video_codec: Literal["h264"]
    """Video codec."""

    width: int
    """Output width in pixels."""

    audio_bitrate: Optional[int] = None
    """Measured audio bitrate in bits per second.

    Omitted until known or when there is no audio.
    """

    audio_codec: Optional[str] = None
    """Measured audio codec. Omitted until known or when there is no audio."""

    audio_samplerate: Optional[int] = None
    """Measured audio sample rate in Hz.

    Omitted until known or when there is no audio.
    """

    cdn_url: Optional[str] = None
    """Unsigned MP4 CDN URL.

    Available when ready and unexpired and Storage has a CDN URL.
    """

    duration: Optional[float] = None
    """Output duration in seconds. Omitted until ready."""

    error: Optional[AssetStaticRenditionOutputDetailsError] = None

    progress: Optional[AssetStaticRenditionOutputDetailsProgress] = None
    """Progress specifies the current processing stage and encoding percentage.

    Omitted after processing ends.
    """

    ready_at: Optional[datetime] = None
    """When the MP4 became available."""

    size: Optional[int] = None
    """File size in bytes. Omitted until ready."""

    url: Optional[str] = None
    """Signed MP4 download URL, available when ready and unexpired.

    Valid for up to ten minutes. Retrieve the output to refresh it. Independent of
    preview_enabled.
    """

    video_bitrate: Optional[int] = None
    """Measured video bitrate in bits per second. Omitted until ready."""

    video_framerate: Optional[float] = None
    """Measured video frame rate in frames per second. Omitted until known."""


class AssetStaticRenditionOutput(BaseModel):
    """An Asset-owned static rendition output and its canonical resource details."""

    id: str
    """Id identifies the Asset output, prefixed with aop\\__.

    The type field identifies the output kind.
    """

    asset_id: str
    """AssetId identifies the owning Asset."""

    details: AssetStaticRenditionOutputDetails
    """
    Details contains the canonical typed output resource, including its available
    delivery fields.
    """

    status: Literal["preparing", "ready", "failed", "expired"]
    """Status specifies the output processing state.

    Expired means temporary output files are no longer available.
    """

    type: Literal["static_rendition"]
    """Type identifies the output kind."""


class AssetThumbnailOutput(BaseModel):
    """An Asset-owned thumbnail output and its canonical resource details."""

    id: str
    """Id identifies the Asset output, prefixed with aop\\__.

    The type field identifies the output kind.
    """

    asset_id: str
    """AssetId identifies the owning Asset."""

    details: Thumbnail
    """
    Details contains the canonical typed output resource, including its available
    delivery fields.
    """

    status: Literal["preparing", "ready", "failed", "expired"]
    """Status specifies the output processing state.

    Expired means temporary output files are no longer available.
    """

    type: Literal["thumbnail"]
    """Type identifies the output kind."""


class AssetTranscriptOutputDetailsContentSegment(BaseModel):
    """A timed passage of recognized speech.

    Times are seconds from the start of the Asset.
    """

    end: float
    """End specifies the passage end time in seconds."""

    start: float
    """Start specifies the passage start time in seconds."""

    text: str
    """Text contains the recognized passage, including punctuation."""


class AssetTranscriptOutputDetailsContent(BaseModel):
    """Content contains the complete text and timed segments.

    Included when ready; omitted while preparing, failed or expired.
    """

    segments: List[AssetTranscriptOutputDetailsContentSegment]
    """Segments contains timed passages in chronological order.

    Individual word timestamps are not included.
    """

    text: str
    """Text contains the complete recognized speech in the original language."""


class AssetTranscriptOutputDetailsError(BaseModel):
    code: str
    """Machine-readable processing error code."""

    message: str
    """Description of the processing failure."""

    stage: Literal["ingest", "analysis", "encoding", "packaging", "upload", "validation", "cleanup"]
    """Processing stage that failed."""


class AssetTranscriptOutputDetails(BaseModel):
    """An original-language transcript.

    Content is included in ready output responses and lifecycle event snapshots. Transcripts have no download or CDN URL.
    """

    id: str
    """Id identifies the Asset output, prefixed with aop\\__."""

    status: Literal["preparing", "ready", "failed", "expired"]
    """Status specifies the output processing state.

    Expired means temporary output files are no longer available.
    """

    content: Optional[AssetTranscriptOutputDetailsContent] = None
    """Content contains the complete text and timed segments.

    Included when ready; omitted while preparing, failed or expired.
    """

    error: Optional[AssetTranscriptOutputDetailsError] = None

    language_code: Optional[str] = None
    """LanguageCode identifies the detected primary language, such as en.

    Omitted before recognition or when no speech is detected.
    """


class AssetTranscriptOutput(BaseModel):
    """An Asset-owned transcript output and its content."""

    id: str
    """Id identifies the Asset output, prefixed with aop\\__."""

    asset_id: str
    """AssetId identifies the owning Asset."""

    details: AssetTranscriptOutputDetails
    """An original-language transcript.

    Content is included in ready output responses and lifecycle event snapshots.
    Transcripts have no download or CDN URL.
    """

    status: Literal["preparing", "ready", "failed", "expired"]
    """Status specifies the output processing state.

    Expired means temporary output files are no longer available.
    """

    type: Literal["transcript"]
    """Type identifies the output kind."""


AssetOutput: TypeAlias = Annotated[
    Union[AssetCaptionOutput, AssetStaticRenditionOutput, AssetThumbnailOutput, AssetTranscriptOutput],
    PropertyInfo(discriminator="type"),
]
