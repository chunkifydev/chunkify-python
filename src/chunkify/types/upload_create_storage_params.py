# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UploadCreateStorageParams"]


class UploadCreateStorageParams(TypedDict, total=False):
    id: str
    """Storage belonging to this Project. Omit to use the Project default."""

    path: str
    """
    Exact object key including filename, required for customer Storage and forbidden
    for Chunkify Storage. The output base_prefix is not added. Existing keys may be
    overwritten.
    """
