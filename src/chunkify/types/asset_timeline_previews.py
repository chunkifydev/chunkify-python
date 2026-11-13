# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AssetTimelinePreviews"]


class AssetTimelinePreviews(BaseModel):
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
