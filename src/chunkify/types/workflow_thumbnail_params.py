# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import TypedDict

from .thumbnail_format import ThumbnailFormat
from .thumbnail_output import ThumbnailOutput
from .workflow_thumbnail_range_params import WorkflowThumbnailRangeParams

__all__ = ["WorkflowThumbnailParams"]


class WorkflowThumbnailParams(TypedDict, total=False):
    """Generate additional thumbnails in the Asset folder and Storage.

    Each layout, format and size combination can be requested once. Specify exactly one of timestamps or count.
    """

    count: int
    """
    Count specifies 1 to 100 thumbnails at the middle of equal sections of the
    selected range.
    """

    format: ThumbnailFormat
    """Format selects JPEG or WebP. Defaults to JPEG."""

    metadata: Dict[str, str]
    """Metadata attaches string values to this request.

    The serialized object may contain at most 2048 bytes.
    """

    output: ThumbnailOutput
    """Output selects images or sprites. Defaults to images."""

    range: WorkflowThumbnailRangeParams
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    size: int
    """Size specifies the maximum image or tile edge in pixels, from 64 to 1920.

    Defaults to 320. Odd sizes are supported. Preserves display aspect ratio without
    cropping or upscaling.
    """

    timestamps: Iterable[float]
    """Timestamps specifies 1 to 100 Source-relative target times in seconds.

    Times outside the selected range are skipped when the action runs. If none
    remain, the action is skipped without a charge. Repeated targets produce
    separate outputs.
    """
