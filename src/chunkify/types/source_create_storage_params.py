# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourceCreateStorageParams"]


class SourceCreateStorageParams(TypedDict, total=False):
    path: Required[str]
    """Exact object key in the configured bucket, 1 to 1024 UTF-8 bytes.

    The output base_prefix is not added.
    """

    id: str
    """Connected external storage belonging to this project.

    If omitted, uses the project default storage, which must be external. The
    resolved storage ID is saved on the source.
    """
