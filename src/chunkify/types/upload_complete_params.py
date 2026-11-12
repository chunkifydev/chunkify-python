# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["UploadCompleteParams", "Part"]


class UploadCompleteParams(TypedDict, total=False):
    parts: Iterable[Part]
    """
    All uploaded parts in ascending part_number order, with the ETags returned by
    storage.
    """


class Part(TypedDict, total=False):
    etag: Required[str]
    """
    ETag returned by storage for this part, including its quotation marks when
    present.
    """

    part_number: Required[int]
    """One-based part number."""
