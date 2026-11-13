# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .thumbnail_range import ThumbnailRange
from .thumbnail_format import ThumbnailFormat
from .thumbnail_output import ThumbnailOutput

__all__ = ["ThumbnailSettings"]


class ThumbnailSettings(BaseModel):
    """Accepted sampling and output settings, with defaults resolved."""

    format: ThumbnailFormat
    """Format specifies the accepted image encoding."""

    output: ThumbnailOutput
    """Output specifies the accepted output mode."""

    range: ThumbnailRange
    """Range contains the accepted sampling boundaries."""

    size: int
    """Size specifies the accepted maximum image or tile edge in pixels."""

    count: Optional[int] = None
    """
    Count specifies 1 to 100 thumbnails at the middle of equal sections of the
    selected range.
    """

    timestamps: Optional[List[float]] = None
    """Timestamps specifies 1 to 100 Source-relative target times in seconds.

    Every time must be within the selected range. Repeated targets produce separate
    outputs.
    """
