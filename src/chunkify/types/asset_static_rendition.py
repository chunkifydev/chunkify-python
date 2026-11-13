# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .asset_rendition_progress import AssetRenditionProgress
from .shared.asset_output_error import AssetOutputError

__all__ = ["AssetStaticRendition"]


class AssetStaticRendition(BaseModel):
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

    error: Optional[AssetOutputError] = None
    """A customer-facing Asset output processing failure."""

    progress: Optional[AssetRenditionProgress] = None
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
