# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.chunkify_error import ChunkifyError

__all__ = ["Upload"]


class Upload(BaseModel):
    id: str
    """Unique identifier of the upload"""

    created_at: datetime
    """Timestamp when the upload was created"""

    expires_at: datetime
    """Timestamp when the upload will expire"""

    status: Literal["waiting", "completed", "failed", "expired"]
    """Current status of the upload"""

    updated_at: datetime
    """Timestamp when the upload was updated"""

    completion_url: Optional[str] = None
    """Short-lived completion capability, returned only on creation.

    POST after a successful PUT before expires_at. Requires no API key. Repeated
    valid calls are idempotent.
    """

    error: Optional[ChunkifyError] = None
    """Error message of the upload"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the upload"""

    source_id: Optional[str] = None
    """SourceId is the id of the source that was created from the upload"""

    storage_id: Optional[str] = None
    """Resolved Storage selected when the Upload was created.

    Absent for historical uploads.
    """

    upload_url: Optional[str] = None
    """Presigned PUT URL, returned only when creating an Upload session.

    Call completion_url after the PUT succeeds.
    """
