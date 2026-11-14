# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from .thumbnail_format import ThumbnailFormat
from .thumbnail_output import ThumbnailOutput
from .thumbnail_range_params import ThumbnailRangeParams
from .thumbnail_create_storage_params import ThumbnailCreateStorageParams

__all__ = ["ThumbnailCreateParams"]


class ThumbnailCreateParams(TypedDict, total=False):
    source_id: Required[str]
    """SourceId identifies a video Source in this Project."""

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

    range: ThumbnailRangeParams
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    size: int
    """Size specifies the maximum image or tile edge in pixels, from 64 to 1920.

    Defaults to 320. Odd sizes are supported. Preserves display aspect ratio without
    cropping or upscaling.
    """

    storage: ThumbnailCreateStorageParams
    """Storage overrides the Project output destination and names the output files.

    Source storage remains independent.
    """

    timestamps: Iterable[float]
    """Timestamps specifies 1 to 100 Source-relative target times in seconds.

    Every time must be within the selected range. Repeated targets produce separate
    outputs.
    """
