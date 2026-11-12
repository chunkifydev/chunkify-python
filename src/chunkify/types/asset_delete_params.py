# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AssetDeleteParams"]


class AssetDeleteParams(TypedDict, total=False):
    delete_files: bool
    """
    Also delete all files under the Asset's storage prefix, including streaming and
    static outputs. Other files and the original input are preserved. Defaults to
    false, which preserves published media files. Private transcript text and saved
    subtitle copies are always scheduled for removal. File deletion is irreversible.
    If cleanup fails, records remain for retry, but files may already be deleted.
    """
