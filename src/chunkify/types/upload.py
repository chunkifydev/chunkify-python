# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .shared.chunkify_error import ChunkifyError

__all__ = ["Upload"]


class Upload(BaseModel):
    id: str
    """Unique identifier of the upload"""

    created_at: str
    """Timestamp when the upload was created"""

    error: ChunkifyError
    """Error message of the upload"""

    expires_at: str
    """Timestamp when the upload will expire"""

    source_id: str
    """SourceId is the id of the source that was created from the upload"""

    status: str
    """Current status of the upload (waiting, completed, failed, expired)"""

    updated_at: str
    """Timestamp when the upload was updated"""

    upload_url: str
    """Pre-signed URL where the file should be uploaded to"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the upload"""
