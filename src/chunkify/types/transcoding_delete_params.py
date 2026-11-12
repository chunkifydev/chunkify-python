# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TranscodingDeleteParams"]


class TranscodingDeleteParams(TypedDict, total=False):
    delete_files: bool
    """
    DeleteFiles specifies whether to permanently delete this Transcoding's output
    files at their saved storage paths. Defaults to false. The original Source and
    unrelated files are preserved. If deletion fails, records remain for retry, but
    some files may already be deleted. Managed dashboard images are removed with the
    resource; temporary outputs still expire after 24 hours when this option is
    false.
    """
