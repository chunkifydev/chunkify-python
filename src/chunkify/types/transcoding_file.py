# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .transcoding_file_thumbnail import TranscodingFileThumbnail

__all__ = ["TranscodingFile"]


class TranscodingFile(BaseModel):
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

    thumbnails: List[TranscodingFileThumbnail]
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
