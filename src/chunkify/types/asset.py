# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .asset_status import AssetStatus

__all__ = ["Asset", "SourceMetadata", "Error", "Poster", "TimelinePreviews"]


class SourceMetadata(BaseModel):
    """
    Original media metadata saved at Asset creation and preserved after Source deletion.
    """

    audio_bitrate: int
    """Original audio bitrate in bits per second, or zero when unavailable."""

    audio_codec: str
    """Original audio codec, or an empty string when there is no audio."""

    audio_samplerate: int
    """Original audio sample rate in Hz, or zero when unavailable."""

    duration: float
    """Original duration in seconds."""

    height: int
    """Original video height in pixels."""

    size: int
    """Original file size in bytes."""

    video_bitrate: int
    """Original video bitrate in bits per second, or zero when unknown."""

    video_codec: str
    """Original video codec."""

    video_framerate: float
    """Original video frame rate in frames per second."""

    width: int
    """Original video width in pixels."""


class Error(BaseModel):
    code: str
    """Machine-readable processing error code."""

    message: str
    """Description of the processing failure."""

    stage: Literal["ingest", "analysis", "encoding", "packaging", "upload", "validation", "cleanup"]
    """Processing stage that failed."""


class Poster(BaseModel):
    """Poster image, available once generated."""

    height: int
    """Image height in pixels."""

    path: str
    """Image path in Storage."""

    width: int
    """Image width in pixels."""

    cdn_url: Optional[str] = None
    """Unsigned image CDN URL.

    Available once the poster exists and Storage has a CDN URL.
    """

    preview_url: Optional[str] = None
    """Public poster preview URL.

    Available when the Asset is ready and preview_enabled is true.
    """

    size: Optional[int] = None
    """Image size in bytes."""

    time_seconds: Optional[float] = None
    """Position of the selected frame in seconds."""

    url: Optional[str] = None
    """Signed image URL, valid for up to ten minutes.

    Available once the poster exists, regardless of preview_enabled.
    """


class TimelinePreviews(BaseModel):
    """Timeline thumbnails.

    The WebVTT file maps video timestamps to image URLs and crop coordinates.
    """

    format: Literal["sprite"]
    """Thumbnail image layout."""

    vtt_path: str
    """WebVTT file path in Storage."""

    cdn_url: Optional[str] = None
    """Unsigned WebVTT CDN URL.

    Available when the Asset is ready and Storage has a CDN URL.
    """

    image_count: Optional[int] = None
    """Number of thumbnails."""

    interval_seconds: Optional[float] = None
    """Target thumbnail sampling interval in seconds.

    The WebVTT file provides actual cue timestamps.
    """

    preview_url: Optional[str] = None
    """Public WebVTT preview URL with signed image references.

    Available when the Asset is ready and preview_enabled is true.
    """

    size: Optional[int] = None
    """Combined WebVTT and sprite image size in bytes."""

    sprite_count: Optional[int] = None
    """Number of sprite images containing the thumbnails."""

    thumbnail_height: Optional[int] = None
    """Thumbnail height in pixels."""

    thumbnail_width: Optional[int] = None
    """Thumbnail width in pixels."""


class Asset(BaseModel):
    id: str
    """Unique Asset ID."""

    can_add_static_renditions: bool
    """Whether the Asset can accept new static rendition requests.

    Creation can still fail if the original video is no longer accessible.
    """

    created_at: datetime
    """When the Asset was created."""

    max_resolution: Literal["1080p", "2160p"]
    """Maximum streaming resolution selected at creation.

    Does not limit static renditions.
    """

    metadata: Dict[str, str]
    """String metadata attached to the Asset."""

    min_resolution: Literal["auto", "240p", "360p", "540p", "720p", "1080p", "1440p", "2160p"]
    """Minimum streaming resolution selected at creation.

    auto means no minimum; smaller sources are not upscaled.
    """

    playback_ready: bool
    """Whether HLS playback is available, including while the Asset is preparing."""

    preview_enabled: bool
    """Allow public preview access without an API token.

    Does not control CDN or static download access. Disabling it does not revoke
    signed URLs already issued.
    """

    source_metadata: SourceMetadata
    """
    Original media metadata saved at Asset creation and preserved after Source
    deletion.
    """

    status: AssetStatus
    """Status specifies the Asset preparation state.

    ready means the video is prepared for playback, with its poster and timeline
    previews available. Static renditions and captions have independent statuses.
    """

    storage_id: str
    """ID of the output Storage."""

    title: str
    """Asset title."""

    updated_at: datetime
    """When the Asset was last updated."""

    workflow_id: Optional[str] = None
    """Selected Workflow ID, or null."""

    workflow_revision: Optional[int] = None
    """Pinned Workflow revision, or null."""

    cdn_url: Optional[str] = None
    """Unsigned CDN URL of the HLS master playlist.

    Available when playback_ready is true and Storage has a CDN URL.
    """

    created_by_token_id: Optional[str] = None
    """CreatedByTokenId specifies the Project token used to create the resource.

    It remains set after the token is revoked. Omitted for dashboard requests, MCP
    OAuth connections, Workflow actions, and unknown creators.
    """

    created_by_user_id: Optional[str] = None
    """
    CreatedByUserId specifies the team member who created the resource. Omitted for
    Workflow actions, unknown creators, and deleted accounts.
    """

    created_via: Optional[Literal["api", "dashboard", "mcp", "workflow"]] = None
    """
    CreatedVia specifies how the resource was created: api for API requests,
    dashboard for the Chunkify dashboard, mcp for MCP clients, and workflow for
    Workflow actions. Omitted when the creator is unknown.
    """

    error: Optional[Error] = None

    expires_at: Optional[datetime] = None
    """When managed outputs expire, 24 hours after readiness.

    Omitted for customer-connected Storage.
    """

    playback_path: Optional[str] = None
    """Path of the HLS master playlist in Storage.

    Available when playback_ready is true.
    """

    playback_ready_at: Optional[datetime] = None
    """When HLS playback first became available."""

    poster: Optional[Poster] = None
    """Poster image, available once generated."""

    preview_url: Optional[str] = None
    """Public HLS preview URL.

    Available when playback_ready and preview_enabled are true. No API token is
    required.
    """

    ready_at: Optional[datetime] = None
    """When all required Asset outputs finished processing."""

    size: Optional[int] = None
    """
    Size specifies the total bytes of available streaming, playback preview, poster,
    and timeline files. Excludes static renditions. Omitted until the Asset is
    ready.
    """

    source_id: Optional[str] = None
    """Original Source ID. Omitted after Source deletion."""

    timeline_previews: Optional[TimelinePreviews] = None
    """Timeline thumbnails.

    The WebVTT file maps video timestamps to image URLs and crop coordinates.
    """
