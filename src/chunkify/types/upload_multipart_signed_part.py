# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["UploadMultipartSignedPart"]


class UploadMultipartSignedPart(BaseModel):
    part_number: int
    """PartNumber specifies the one-based part number for this URL."""

    upload_url: str
    """UploadUrl specifies the signed PUT URL for this part.

    Retry the same file slice with this URL before multipart.expires_at.
    """
