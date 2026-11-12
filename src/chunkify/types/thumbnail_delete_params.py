# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ThumbnailDeleteParams"]


class ThumbnailDeleteParams(TypedDict, total=False):
    delete_files: bool
    """
    DeleteFiles specifies whether to permanently delete this Thumbnail's owned
    images, sprite sheets, VTT and partial outputs at their saved storage prefix.
    Defaults to false. The Source and unrelated files are preserved. If deletion
    fails, records remain for retry, but some files may already be deleted.
    Temporary outputs still expire when this option is false.
    """
