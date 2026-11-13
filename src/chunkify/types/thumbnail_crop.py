# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ThumbnailCrop"]


class ThumbnailCrop(BaseModel):
    """The image rectangle within a sprite sheet."""

    x: int
    """X specifies the left edge in pixels."""

    y: int
    """Y specifies the top edge in pixels."""
