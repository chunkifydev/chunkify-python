# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TranscodingCreateStorageParams"]


class TranscodingCreateStorageParams(TypedDict, total=False):
    """Output storage selection, independent of the Source storage."""

    id: str
    """Id specifies a Storage in this Project. Defaults to the Project output storage."""

    path: str
    """
    Path specifies the output object path relative to the selected Storage
    base_prefix. Required for customer storage; generated for Chunkify temporary
    storage. The extension must match the resolved output format. The combined path
    may contain at most 1024 bytes.
    """
