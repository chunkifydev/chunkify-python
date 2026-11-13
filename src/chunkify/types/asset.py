# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .asset_error import AssetError
from .asset_poster import AssetPoster
from .asset_status import AssetStatus
from .shared.created_via import CreatedVia
from .asset_source_metadata import AssetSourceMetadata
from .asset_timeline_previews import AssetTimelinePreviews

__all__ = ["Asset"]


class Asset(BaseModel):
    id: str
    """Unique Asset ID."""

    can_add_static_renditions: bool
    """Whether the Asset can accept new static rendition requests.

    Creation can still fail if the original video is no longer accessible.
    """

    created_at: datetime
    """When the Asset was created."""

    max_resolution: Literal["1080p", "2160p"]
    """Maximum streaming resolution selected at creation.

    Does not limit static renditions.
    """

    metadata: Dict[str, str]
    """String metadata attached to the Asset."""

    min_resolution: Literal["auto", "240p", "360p", "540p", "720p", "1080p", "1440p", "2160p"]
    """Minimum streaming resolution selected at creation.

    auto means no minimum; smaller sources are not upscaled.
    """

    playback_ready: bool
    """Whether HLS playback is available, including while the Asset is preparing."""

    preview_enabled: bool
    """Allow public preview access without an API token.

    Does not control CDN or static download access. Disabling it does not revoke
    signed URLs already issued.
    """

    source_metadata: AssetSourceMetadata
    """
    Original media metadata saved at Asset creation and preserved after Source
    deletion.
    """

    status: AssetStatus
    """Status specifies the Asset preparation state.

    ready means the video is prepared for playback, with its poster and timeline
    previews available. Static renditions and captions have independent statuses.
    """

    storage_id: str
    """ID of the output Storage."""

    title: str
    """Asset title."""

    updated_at: datetime
    """When the Asset was last updated."""

    workflow_id: Optional[str] = None
    """Selected Workflow ID, or null."""

    workflow_revision: Optional[int] = None
    """Pinned Workflow revision, or null."""

    cdn_url: Optional[str] = None
    """Unsigned CDN URL of the HLS master playlist.

    Available when playback_ready is true and Storage has a CDN URL.
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

    error: Optional[AssetError] = None

    expires_at: Optional[datetime] = None
    """When managed outputs expire, 24 hours after readiness.

    Omitted for customer-connected Storage.
    """

    playback_path: Optional[str] = None
    """Path of the HLS master playlist in Storage.

    Available when playback_ready is true.
    """

    playback_ready_at: Optional[datetime] = None
    """When HLS playback first became available."""

    poster: Optional[AssetPoster] = None
    """Poster image, available once generated."""

    preview_url: Optional[str] = None
    """Public HLS preview URL.

    Available when playback_ready and preview_enabled are true. No API token is
    required.
    """

    ready_at: Optional[datetime] = None
    """When all required Asset outputs finished processing."""

    size: Optional[int] = None
    """
    Size specifies the total bytes of available streaming, playback preview, poster,
    and timeline files. Excludes static renditions. Omitted until the Asset is
    ready.
    """

    source_id: Optional[str] = None
    """Original Source ID. Omitted after Source deletion."""

    timeline_previews: Optional[AssetTimelinePreviews] = None
    """Timeline thumbnails.

    The WebVTT file maps video timestamps to image URLs and crop coordinates.
    """
