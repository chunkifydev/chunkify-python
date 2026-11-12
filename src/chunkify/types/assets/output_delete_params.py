# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OutputDeleteParams"]


class OutputDeleteParams(TypedDict, total=False):
    asset_id: Required[Annotated[str, PropertyInfo(alias="assetId")]]

    delete_files: bool
    """
    DeleteFiles specifies whether to remove this output's published media files from
    Storage. Defaults to false, preserving those files. Transcript deletion always
    schedules removal of its private text and saved subtitle copy, regardless of
    this option. The Asset, Source, and other outputs are preserved. File cleanup
    failures retain the output record for retry; files already removed cannot be
    restored.
    """
