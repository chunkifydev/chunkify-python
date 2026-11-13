# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ThumbnailCreateParams", "Range", "Storage"]


class ThumbnailCreateParams(TypedDict, total=False):
    source_id: Required[str]
    """SourceId identifies a video Source in this Project."""

    count: int
    """
    Count specifies 1 to 100 thumbnails at the middle of equal sections of the
    selected range.
    """

    format: Literal["jpeg", "webp"]
    """Format selects JPEG or WebP. Defaults to JPEG."""

    metadata: Dict[str, str]
    """Metadata attaches string values to this request.

    The serialized object may contain at most 2048 bytes.
    """

    output: Literal["images", "sprites"]
    """Output selects images or sprites. Defaults to images."""

    range: Range
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    size: int
    """Size specifies the maximum image or tile edge in pixels, from 64 to 1920.

    Defaults to 320. Odd sizes are supported. Preserves display aspect ratio without
    cropping or upscaling.
    """

    storage: Storage
    """Storage overrides the Project output destination and names the output files.

    Source storage remains independent.
    """

    timestamps: Iterable[float]
    """Timestamps specifies 1 to 100 Source-relative target times in seconds.

    Every time must be within the selected range. Repeated targets produce separate
    outputs.
    """


class Range(TypedDict, total=False):
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    end: float
    """End specifies the exclusive upper bound in seconds.

    Defaults to the Source duration.
    """

    start: float
    """Start specifies the inclusive lower bound in seconds. Defaults to zero."""


class Storage(TypedDict, total=False):
    """Storage overrides the Project output destination and names the output files.

    Source storage remains independent.
    """

    id: str
    """Id identifies output Storage in this Project. Omit to use the Project default."""

    path: str
    """
    Path specifies the output filename template relative to the selected Storage
    base_prefix. Required for customer storage; generated for Chunkify temporary
    storage. The filename must contain one %05d placeholder, replaced by the image
    or sprite sheet number starting at 1, and end in .jpg for jpeg or .webp for
    webp. The WebVTT file uses the filename without the placeholder and its adjacent
    separator, such as thumb.vtt for thumb-%05d.jpg. The combined path may contain
    at most 1024 bytes.
    """
