# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TranscodingFileThumbnail"]


class TranscodingFileThumbnail(BaseModel):
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
