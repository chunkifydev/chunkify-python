# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Transcoding", "File", "FileThumbnail", "Format", "Storage", "Error"]


class FileThumbnail(BaseModel):
    """An optional dashboard preview of the completed output."""

    format: Literal["jpeg", "webp"]
    """Format specifies the image encoding."""

    height: int
    """Height specifies the measured image height in pixels."""

    size: int
    """Size specifies the measured image size in bytes."""

    url: str
    """Url provides a signed image URL valid for at most ten minutes."""

    width: int
    """Width specifies the measured image width in pixels."""


class File(BaseModel):
    """A validated media file published by a Transcoding."""

    id: str
    """Id identifies this published Transcoding file."""

    created_at: datetime
    """CreatedAt records when the validated file was published."""

    duration: float
    """Duration specifies the measured output duration in seconds."""

    mime_type: str
    """MimeType specifies the media content type."""

    path: str
    """
    Path specifies the output path relative to the Storage base_prefix saved when
    the Transcoding was created. Later Storage prefix changes do not move this file.
    """

    size: int
    """Size specifies the measured file size in bytes."""

    storage_id: str
    """StorageId identifies the output Storage."""

    thumbnails: List[FileThumbnail]
    """Thumbnails contains available dashboard preview images.

    Empty for audio-only files, failed previews or expired files.
    """

    transcoding_id: str
    """TranscodingId identifies the Transcoding that produced this file."""

    audio_bitrate: Optional[int] = None
    """AudioBitrate specifies measured audio bits per second, or zero when unavailable.

    Omitted without audio.
    """

    audio_codec: Optional[str] = None
    """AudioCodec specifies the measured audio codec. Omitted without audio."""

    audio_samplerate: Optional[int] = None
    """AudioSamplerate specifies measured audio samples per second.

    Omitted without audio.
    """

    cdn_url: Optional[str] = None
    """CdnUrl provides the URL from the Storage CDN configuration.

    Omitted without a configured CDN or after file expiry.
    """

    expires_at: Optional[datetime] = None
    """ExpiresAt specifies when a temporary output expires.

    Omitted for customer-owned output storage.
    """

    height: Optional[int] = None
    """Height specifies the measured video height in pixels.

    Omitted for audio-only files.
    """

    thumbnail_status: Optional[Literal["ready", "failed"]] = None
    """ThumbnailStatus reports the optional dashboard preview result.

    Failure does not affect the media file. Omitted for audio-only files.
    """

    url: Optional[str] = None
    """Url provides a signed download valid for at most ten minutes.

    Omitted when the file has expired or signing is unavailable.
    """

    video_bitrate: Optional[int] = None
    """VideoBitrate specifies measured video bits per second, or zero when unavailable.

    Omitted without video.
    """

    video_codec: Optional[str] = None
    """VideoCodec specifies the measured video codec. Omitted for audio-only files."""

    video_framerate: Optional[float] = None
    """VideoFramerate specifies measured video frames per second.

    Omitted without video.
    """

    width: Optional[int] = None
    """Width specifies the measured video width in pixels.

    Omitted for audio-only files.
    """


class Format(BaseModel):
    """
    Format contains the resolved encoding settings accepted at creation, including defaults, dimensions, frame rate and normalized seek and duration. Per-title rate control is resolved during processing. Measured media properties are available in Files.
    """

    id: Literal["mp4_h264", "mp4_h265", "mp4_av1", "webm_vp9", "m4a_aac"]
    """Id specifies the resolved container and codec selection."""

    duration: float
    """
    Duration specifies the accepted output duration in seconds, including normalized
    trims.
    """

    seek: float
    """
    Seek specifies the accepted start position in source seconds, normalized to the
    output timeline.
    """

    audio_bitrate: Optional[int] = None
    """AudioBitrate specifies the resolved audio bitrate in bits per second.

    Omitted for video-only output.
    """

    audio_samplerate: Optional[int] = None
    """AudioSamplerate specifies the resolved audio samples per second.

    Omitted for video-only output.
    """

    bufsize: Optional[int] = None
    """
    Bufsize specifies the resolved video buffer size in bits, including codec-level
    defaults. Omitted when no buffer applies.
    """

    channels: Optional[int] = None
    """Channels specifies the resolved audio channel count: 1, 2, 6 or 8.

    Omitted for video-only output.
    """

    cpu_used: Optional[str] = None
    """CpuUsed specifies the accepted VP9 encoder speed setting from 0 through 8.

    Omitted for other codecs.
    """

    crf: Optional[int] = None
    """Crf specifies the accepted constant quality.

    Omitted for bitrate-controlled, per-title and audio-only encoding.
    """

    disable_audio: Optional[bool] = None
    """DisableAudio is true for video-only output. Omitted when audio is selected."""

    framerate: Optional[float] = None
    """Framerate specifies the resolved video frames per second.

    Omitted for audio-only output.
    """

    gop: Optional[int] = None
    """Gop specifies the resolved maximum keyframe interval in frames.

    Omitted for audio-only output.
    """

    height: Optional[int] = None
    """Height specifies the resolved video height in pixels.

    Omitted for audio-only output.
    """

    level: Optional[int] = None
    """Level specifies the accepted codec level when explicitly selected."""

    maxrate: Optional[int] = None
    """
    Maxrate specifies the resolved maximum video bitrate in bits per second,
    including codec-level defaults. Omitted when no maximum applies.
    """

    minrate: Optional[int] = None
    """
    Minrate specifies the accepted minimum video bitrate in bits per second, when
    configured.
    """

    movflags: Optional[str] = None
    """Movflags specifies MP4 packaging. MP4 video exports use faststart."""

    per_title: Optional[bool] = None
    """
    PerTitle specifies whether video rate control is selected during content
    analysis. Omitted for audio-only output.
    """

    pixfmt: Optional[str] = None
    """Pixfmt specifies the accepted video pixel format.

    Omitted for audio-only output.
    """

    preset: Optional[str] = None
    """Preset specifies the accepted codec preset.

    Omitted when the codec does not use presets.
    """

    profilev: Optional[str] = None
    """Profilev specifies the accepted codec profile when explicitly selected."""

    quality: Optional[str] = None
    """Quality specifies the accepted VP9 deadline policy: good, best or realtime.

    Omitted for other codecs.
    """

    video_bitrate: Optional[int] = None
    """VideoBitrate specifies the accepted video bitrate in bits per second.

    Omitted for CRF and per-title encoding.
    """

    width: Optional[int] = None
    """Width specifies the resolved video width in pixels.

    Omitted for audio-only output.
    """


class Storage(BaseModel):
    """Storage contains the resolved output destination."""

    id: str
    """Id identifies the output Storage."""

    path: str
    """
    Path specifies the output file path relative to the Storage base_prefix saved at
    creation.
    """


class Error(BaseModel):
    """Error describes why processing failed. Omitted when no processing error exists."""

    code: str
    """Code identifies the processing failure."""

    message: str
    """Message describes the failure without internal worker or provider diagnostics."""

    stage: Literal["queued", "starting", "encoding", "finalizing", "uploading"]
    """Stage identifies where processing failed."""


class Transcoding(BaseModel):
    """
    A standalone file-encoding request with its accepted settings and published files.
    """

    id: str
    """Id uniquely identifies the Transcoding."""

    created_at: datetime
    """CreatedAt specifies when the request was accepted."""

    files: List[File]
    """
    Files contains the published output files and their measured properties, ordered
    by creation time. Empty until publication. Presigned URLs are refreshed on each
    read and included in lifecycle webhooks when available.
    """

    format: Format
    """
    Format contains the resolved encoding settings accepted at creation, including
    defaults, dimensions, frame rate and normalized seek and duration. Per-title
    rate control is resolved during processing. Measured media properties are
    available in Files.
    """

    metadata: Dict[str, str]
    """Metadata contains the string values attached to the Transcoding."""

    status: Literal["preparing", "ready", "failed", "cancelled", "expired"]
    """Status reports processing or output expiry."""

    storage: Storage
    """Storage contains the resolved output destination."""

    updated_at: datetime
    """UpdatedAt specifies when the request was last updated."""

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

    delete_at: Optional[datetime] = None
    """
    DeleteAt specifies when this record is deleted: three days after its temporary
    output expires, otherwise when the team's data retention period ends, counted
    from when the request was accepted, and no sooner than three days after it
    finished. It does not delete files in customer-owned Storage. Omitted while the
    Transcoding is preparing.
    """

    error: Optional[Error] = None
    """Error describes why processing failed. Omitted when no processing error exists."""

    expires_at: Optional[datetime] = None
    """ExpiresAt specifies when temporary output files expire.

    Omitted for customer output Storage and before the Transcoding is ready.
    """

    processing_stage: Optional[Literal["queued", "starting", "encoding", "finalizing", "uploading"]] = None
    """ProcessingStage specifies the current activity while the status is preparing.

    Omitted otherwise.
    """

    progress: Optional[float] = None
    """Progress specifies the video encoding percentage.

    Available once processing starts and after the output is ready. Omitted for
    audio-only output; 100 requires published output.
    """

    ready_at: Optional[datetime] = None
    """ReadyAt specifies when the output was published.

    Omitted before the Transcoding is ready.
    """

    source_id: Optional[str] = None
    """SourceId identifies the original Source. Omitted after Source deletion."""
