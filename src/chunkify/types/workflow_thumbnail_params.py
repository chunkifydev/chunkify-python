# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkflowThumbnailParams", "Range"]


class Range(BaseModel):
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    end: Optional[float] = None
    """End specifies the exclusive upper bound in seconds.

    Defaults to the Source duration.
    """

    start: Optional[float] = None
    """Start specifies the inclusive lower bound in seconds. Defaults to zero."""


class WorkflowThumbnailParams(BaseModel):
    """Generate additional thumbnails in the Asset folder and Storage.

    Each layout, format and size combination can be requested once. Specify exactly one of timestamps or count.
    """

    count: Optional[int] = None
    """
    Count specifies 1 to 100 thumbnails at the middle of equal sections of the
    selected range.
    """

    format: Optional[Literal["jpeg", "webp"]] = None
    """Format selects JPEG or WebP. Defaults to JPEG."""

    metadata: Optional[Dict[str, str]] = None
    """Metadata attaches string values to this request.

    The serialized object may contain at most 2048 bytes.
    """

    output: Optional[Literal["images", "sprites"]] = None
    """Output selects images or sprites. Defaults to images."""

    range: Optional[Range] = None
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    size: Optional[int] = None
    """Size specifies the maximum image or tile edge in pixels, from 64 to 1920.

    Defaults to 320. Odd sizes are supported. Preserves display aspect ratio without
    cropping or upscaling.
    """

    timestamps: Optional[List[float]] = None
    """Timestamps specifies 1 to 100 Source-relative target times in seconds.

    Times outside the selected range are skipped when the action runs. If none
    remain, the action is skipped without a charge. Repeated targets produce
    separate outputs.
    """
