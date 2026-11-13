# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AssetPoster"]


class AssetPoster(BaseModel):
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
