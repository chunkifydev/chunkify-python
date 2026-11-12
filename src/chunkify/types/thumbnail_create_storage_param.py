# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ThumbnailCreateStorageParam"]


class ThumbnailCreateStorageParam(TypedDict, total=False):
    """Output Storage selection, independent of Source storage."""

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
