# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .upload_multipart_signed_part import UploadMultipartSignedPart

__all__ = ["UploadMultipartSession"]


class UploadMultipartSession(BaseModel):
    expires_at: datetime
    """ExpiresAt specifies when the signed part URLs expire.

    URLs cannot be refreshed; create a new Upload after expiry.
    """

    part_size_bytes: int
    """PartSizeBytes specifies the size of each part except the final part, in bytes."""

    parts: List[UploadMultipartSignedPart]
    """Parts contains every signed upload URL in ascending part_number order.

    Upload file slices directly to these URLs.
    """
