# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .upload_multipart_part_params import UploadMultipartPartParams

__all__ = ["UploadCompleteParams"]


class UploadCompleteParams(TypedDict, total=False):
    parts: Iterable[UploadMultipartPartParams]
    """
    All uploaded parts in ascending part_number order, with the ETags returned by
    storage.
    """
