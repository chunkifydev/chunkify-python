# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the file"""

    audio_bitrate: Optional[int] = None
    """Audio bitrate in bits per second"""

    audio_codec: Optional[str] = None
    """Audio codec used (e.g. aac, mp3)"""

    created_at: Optional[str] = None
    """Timestamp when the file was created"""

    duration: Optional[int] = None
    """Duration of the video in seconds"""

    height: Optional[int] = None
    """Height of the video in pixels"""

    job_id: Optional[str] = None
    """ID of the job that created this file"""

    mime_type: Optional[str] = None
    """MIME type of the file"""

    path: Optional[str] = None
    """Path to the file in storage"""

    size: Optional[int] = None
    """Size of the file in bytes"""

    storage_id: Optional[str] = None
    """StorageId identifier where the file is stored"""

    url: Optional[str] = None
    """Pre-signed URL to directly access the file (only included when available)"""

    video_bitrate: Optional[int] = None
    """Video bitrate in bits per second"""

    video_codec: Optional[str] = None
    """Video codec used (e.g. h264, h265)"""

    video_framerate: Optional[float] = None
    """Video framerate in frames per second"""

    width: Optional[int] = None
    """Width of the video in pixels"""
