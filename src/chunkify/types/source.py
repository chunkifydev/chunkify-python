# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Source"]


class Source(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the source"""

    audio_bitrate: Optional[int] = None
    """Audio bitrate in bits per second"""

    audio_codec: Optional[str] = None
    """Audio codec used (e.g. aac, mp3)"""

    created_at: Optional[str] = None
    """Timestamp when the source was created"""

    device: Optional[str] = None
    """Device used to record the video"""

    duration: Optional[int] = None
    """Duration of the video in seconds"""

    height: Optional[int] = None
    """Height of the video in pixels"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the source"""

    size: Optional[int] = None
    """Size of the source file in bytes"""

    url: Optional[str] = None
    """URL where the source video can be accessed"""

    video_bitrate: Optional[int] = None
    """Video bitrate in bits per second"""

    video_codec: Optional[str] = None
    """Video codec used (e.g. h264, h265)"""

    video_framerate: Optional[float] = None
    """Video framerate in frames per second"""

    width: Optional[int] = None
    """Width of the video in pixels"""
