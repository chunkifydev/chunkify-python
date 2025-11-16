# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Upload", "Error"]


class Error(BaseModel):
    detail: Optional[str] = None
    """Additional error details or output"""

    message: Optional[str] = None
    """Main error message"""

    type: Optional[str] = None
    """Type of error (e.g., "ffmpeg", "network", "storage", etc.)"""


class Upload(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the upload"""

    created_at: Optional[str] = None
    """Timestamp when the upload was created"""

    error: Optional[Error] = None
    """Error message of the upload"""

    expires_at: Optional[str] = None
    """Timestamp when the upload will expire"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the upload"""

    source_id: Optional[str] = None
    """SourceId is the id of the source that was created from the upload"""

    status: Optional[str] = None
    """Current status of the upload (waiting, completed, failed, expired)"""

    updated_at: Optional[str] = None
    """Timestamp when the upload was updated"""

    upload_url: Optional[str] = None
    """Pre-signed URL where the file should be uploaded to"""
