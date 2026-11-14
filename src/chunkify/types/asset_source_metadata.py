# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AssetSourceMetadata"]


class AssetSourceMetadata(BaseModel):
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
