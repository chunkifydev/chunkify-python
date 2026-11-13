# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.created_via import CreatedVia
from .shared.chunkify_error import ChunkifyError
from .upload_multipart_session import UploadMultipartSession

__all__ = ["Upload"]


class Upload(BaseModel):
    id: str
    """Unique identifier of the upload"""

    create_asset: bool
    """Whether this Upload creates an Asset on completion."""

    created_at: datetime
    """Timestamp when the upload was created"""

    expires_at: datetime
    """Timestamp when the upload will expire"""

    status: Literal["waiting", "completed", "failed", "expired"]
    """Current status of the upload"""

    updated_at: datetime
    """Timestamp when the upload was updated"""

    upload_mode: Literal["single", "multipart"]
    """Resolved transfer mode for this Upload."""

    workflow_id: Optional[str] = None
    """Selected Workflow ID, or null."""

    workflow_revision: Optional[int] = None
    """Pinned Workflow revision, or null."""

    asset_id: Optional[str] = None
    """Automatically created Asset.

    May be absent before completion or after record deletion.
    """

    completion_url: Optional[str] = None
    """Completion capability, returned only on creation.

    POST after a successful single PUT or with all multipart ETags before
    expires_at. Requires no API key. Repeated valid calls are idempotent.
    """

    created_by_token_id: Optional[str] = None
    """CreatedByTokenId specifies the Project token used to create the resource.

    It remains set after the token is revoked. Omitted for dashboard requests, MCP
    OAuth connections, Workflow actions, and unknown creators.
    """

    created_by_user_id: Optional[str] = None
    """
    CreatedByUserId specifies the team member who created the resource. Omitted for
    Workflow actions, unknown creators, and deleted accounts.
    """

    created_via: Optional[CreatedVia] = None
    """
    CreatedVia specifies how the resource was created: api for API requests,
    dashboard for the Chunkify dashboard, mcp for MCP clients, and workflow for
    Workflow actions. Omitted when the creator is unknown.
    """

    error: Optional[ChunkifyError] = None
    """Error message of the upload"""

    file_size_bytes: Optional[int] = None
    """Declared file size in bytes, when supplied at creation."""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the upload"""

    multipart: Optional[UploadMultipartSession] = None
    """Multipart transfer details, returned only on creation for multipart Uploads."""

    source_id: Optional[str] = None
    """SourceId is the id of the source that was created from the upload"""

    storage_id: Optional[str] = None
    """Resolved Storage selected when the Upload was created.

    Absent for historical uploads.
    """

    upload_url: Optional[str] = None
    """Presigned PUT URL, returned only when creating a single-PUT Upload session.

    Call completion_url after the PUT succeeds.
    """
