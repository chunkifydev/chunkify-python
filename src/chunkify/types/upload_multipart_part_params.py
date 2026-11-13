# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UploadMultipartPartParams"]


class UploadMultipartPartParams(TypedDict, total=False):
    etag: Required[str]
    """
    ETag returned by storage for this part, including its quotation marks when
    present.
    """

    part_number: Required[int]
    """One-based part number."""
