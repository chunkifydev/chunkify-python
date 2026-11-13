# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .transcoding_file import TranscodingFile
from .transcoding_error import TranscodingError
from .shared.created_via import CreatedVia
from .transcoding_format import TranscodingFormat
from .transcoding_status import TranscodingStatus
from .transcoding_storage import TranscodingStorage
from .transcoding_processing_stage import TranscodingProcessingStage

__all__ = ["Transcoding"]


class Transcoding(BaseModel):
    """
    A standalone file-encoding request with its accepted settings and published files.
    """

    id: str
    """Id uniquely identifies the Transcoding."""

    created_at: datetime
    """CreatedAt specifies when the request was accepted."""

    files: List[TranscodingFile]
    """
    Files contains the published output files and their measured properties, ordered
    by creation time. Empty until publication. Presigned URLs are refreshed on each
    read and included in lifecycle webhooks when available.
    """

    format: TranscodingFormat
    """
    Format contains the resolved encoding settings accepted at creation, including
    defaults, dimensions, frame rate and normalized seek and duration. Per-title
    rate control is resolved during processing. Measured media properties are
    available in Files.
    """

    metadata: Dict[str, str]
    """Metadata contains the string values attached to the Transcoding."""

    status: TranscodingStatus
    """Status reports processing or output expiry."""

    storage: TranscodingStorage
    """Storage contains the resolved output destination."""

    updated_at: datetime
    """UpdatedAt specifies when the request was last updated."""

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
    DeleteAt specifies when this record is deleted: three days after its temporary
    output expires, otherwise when the team's data retention period ends, counted
    from when the request was accepted, and no sooner than three days after it
    finished. It does not delete files in customer-owned Storage. Omitted while the
    Transcoding is preparing.
    """

    error: Optional[TranscodingError] = None
    """Error describes why processing failed. Omitted when no processing error exists."""

    expires_at: Optional[datetime] = None
    """ExpiresAt specifies when temporary output files expire.

    Omitted for customer output Storage and before the Transcoding is ready.
    """

    processing_stage: Optional[TranscodingProcessingStage] = None
    """ProcessingStage specifies the current activity while the status is preparing.

    Omitted otherwise.
    """

    progress: Optional[float] = None
    """Progress specifies the video encoding percentage.

    Available once processing starts and after the output is ready. Omitted for
    audio-only output; 100 requires published output.
    """

    ready_at: Optional[datetime] = None
    """ReadyAt specifies when the output was published.

    Omitted before the Transcoding is ready.
    """

    source_id: Optional[str] = None
    """SourceId identifies the original Source. Omitted after Source deletion."""
