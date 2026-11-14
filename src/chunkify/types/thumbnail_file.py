# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ThumbnailFile"]


class ThumbnailFile(BaseModel):
    """One published image, sprite sheet, or WebVTT file."""

    kind: Literal["image", "sprite", "vtt"]
    """Kind identifies an individual image, sprite sheet, or WebVTT index."""

    path: str
    """Path specifies the file relative to storage_prefix."""

    size: int
    """Size specifies the measured encoded file size in bytes."""

    cdn_url: Optional[str] = None
    """CdnUrl provides delivery through the configured CDN.

    Omitted without a CDN or after expiry.
    """

    height: Optional[int] = None
    """Height specifies the measured image or complete sprite canvas height.

    Omitted for WebVTT.
    """

    url: Optional[str] = None
    """Url provides temporary authorized delivery.

    Omitted after expiry or when unavailable.
    """

    width: Optional[int] = None
    """Width specifies the measured image or complete sprite canvas width.

    Omitted for WebVTT.
    """
