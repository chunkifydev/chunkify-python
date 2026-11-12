# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Thumbnail", "File", "Sample", "SampleCrop", "Settings", "SettingsRange", "Error"]


class File(BaseModel):
    """One published image, sprite sheet, or WebVTT file."""

    kind: Literal["image", "sprite", "vtt"]
    """Kind identifies an individual image, sprite sheet, or WebVTT index."""

    path: str
    """Path specifies the file relative to storage_prefix."""

    size: int
    """Size specifies the measured encoded file size in bytes."""

    cdn_url: Optional[str] = None
    """CdnUrl provides delivery through the configured CDN.

    Omitted without a CDN or after expiry.
    """

    height: Optional[int] = None
    """Height specifies the measured image or complete sprite canvas height.

    Omitted for WebVTT.
    """

    url: Optional[str] = None
    """Url provides temporary authorized delivery.

    Omitted after expiry or when unavailable.
    """

    width: Optional[int] = None
    """Width specifies the measured image or complete sprite canvas width.

    Omitted for WebVTT.
    """


class SampleCrop(BaseModel):
    """Crop specifies the tile origin in its sprite sheet.

    Omitted for individual images; width and height give the tile dimensions.
    """

    x: int
    """X specifies the left edge in pixels."""

    y: int
    """Y specifies the top edge in pixels."""


class Sample(BaseModel):
    """One successfully published requested sample.

    Repeated samples remain separate entries.
    """

    height: int
    """Height specifies this image or tile height in pixels."""

    path: str
    """Path identifies the image or sprite sheet in files."""

    timestamp: float
    """
    Timestamp specifies the measured Source-relative presentation time of the
    selected frame in seconds. Compatible cached inputs use millisecond timestamps,
    which can select a neighboring frame compared with the original Source.
    """

    width: int
    """Width specifies this image or tile width in pixels."""

    crop: Optional[SampleCrop] = None
    """Crop specifies the tile origin in its sprite sheet.

    Omitted for individual images; width and height give the tile dimensions.
    """


class SettingsRange(BaseModel):
    """Range contains the accepted sampling boundaries."""

    end: float
    """End specifies the exclusive upper bound in seconds."""

    start: float
    """Start specifies the inclusive lower bound in seconds."""


class Settings(BaseModel):
    """Settings contains the accepted sampling and output settings."""

    format: Literal["jpeg", "webp"]
    """Format specifies the accepted image encoding."""

    output: Literal["images", "sprites"]
    """Output specifies the accepted output mode."""

    range: SettingsRange
    """Range contains the accepted sampling boundaries."""

    size: int
    """Size specifies the accepted maximum image or tile edge in pixels."""

    count: Optional[int] = None
    """
    Count specifies 1 to 100 thumbnails at the middle of equal sections of the
    selected range.
    """

    timestamps: Optional[List[float]] = None
    """Timestamps specifies 1 to 100 Source-relative target times in seconds.

    Every time must be within the selected range. Repeated targets produce separate
    outputs.
    """


class Error(BaseModel):
    """Error explains a failed request. Omitted otherwise."""

    code: str
    """Code identifies the processing failure."""

    message: str
    """Message explains the processing failure."""


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

    files: List[File]
    """Files contains all published images or sheets and the WebVTT index.

    Empty while preparing.
    """

    metadata: Dict[str, str]
    """Metadata contains the accepted string metadata."""

    samples: List[Sample]
    """Samples contains published thumbnails ordered by timestamp.

    Empty while preparing. A ready resource may contain fewer samples than
    requested.
    """

    settings: Settings
    """Settings contains the accepted sampling and output settings."""

    source_id: Optional[str] = None
    """SourceId identifies the input Source, or null if it has been deleted."""

    status: Literal["preparing", "ready", "failed", "expired"]
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

    created_via: Optional[Literal["api", "dashboard", "mcp", "workflow"]] = None
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

    error: Optional[Error] = None
    """Error explains a failed request. Omitted otherwise."""

    expires_at: Optional[datetime] = None
    """ExpiresAt specifies when temporary output files expire.

    Omitted for customer output Storage.
    """

    ready_at: Optional[datetime] = None
    """ReadyAt records when the complete available set was published.

    Omitted before publication.
    """
