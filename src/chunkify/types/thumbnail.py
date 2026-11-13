# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .thumbnail_file import ThumbnailFile
from .thumbnail_error import ThumbnailError
from .thumbnail_sample import ThumbnailSample
from .thumbnail_status import ThumbnailStatus
from .shared.created_via import CreatedVia
from .thumbnail_settings import ThumbnailSettings

__all__ = ["Thumbnail"]


class Thumbnail(BaseModel):
    """One thumbnail generation request.

    At least one sample and its companion files must be published before the resource is ready.
    """

    id: str
    """Id identifies this thumbnail request.

    Standalone requests use thm* IDs; Asset-owned outputs use aop* IDs.
    """

    asset_id: Optional[str] = None
    """
    AssetId identifies the owning Asset for Workflow outputs, or null for standalone
    requests.
    """

    created_at: datetime
    """CreatedAt records when the request was accepted."""

    files: List[ThumbnailFile]
    """Files contains all published images or sheets and the WebVTT index.

    Empty while preparing.
    """

    metadata: Dict[str, str]
    """Metadata contains the accepted string metadata."""

    samples: List[ThumbnailSample]
    """Samples contains published thumbnails ordered by timestamp.

    Empty while preparing. A ready resource may contain fewer samples than
    requested.
    """

    settings: ThumbnailSettings
    """Settings contains the accepted sampling and output settings."""

    source_id: Optional[str] = None
    """SourceId identifies the input Source, or null if it has been deleted."""

    status: ThumbnailStatus
    """Status reports processing or output expiry."""

    storage_id: str
    """StorageId identifies the accepted output Storage."""

    storage_path: Optional[str] = None
    """
    StoragePath specifies the accepted filename template relative to the Storage
    base_prefix, or null when Chunkify generated the file names.
    """

    storage_prefix: str
    """StoragePrefix specifies the complete output folder saved at creation.

    File and sample paths are relative to this folder.
    """

    updated_at: datetime
    """UpdatedAt records the last lifecycle update."""

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

    delete_at: Optional[datetime] = None
    """
    DeleteAt specifies when this standalone request is deleted: three days after its
    temporary output expires, otherwise when the team's data retention period ends,
    counted from when the request was accepted, and no sooner than three days after
    it finished. It does not delete files in customer-owned Storage. Omitted while
    preparing and for Asset-owned thumbnails, which follow their Asset.
    """

    error: Optional[ThumbnailError] = None
    """Error explains a failed request. Omitted otherwise."""

    expires_at: Optional[datetime] = None
    """ExpiresAt specifies when temporary output files expire.

    Omitted for customer output Storage.
    """

    ready_at: Optional[datetime] = None
    """ReadyAt records when the complete available set was published.

    Omitted before publication.
    """
