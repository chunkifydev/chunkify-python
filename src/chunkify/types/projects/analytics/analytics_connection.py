# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AnalyticsConnection"]


class AnalyticsConnection(BaseModel):
    """A saved source for analytics reports.

    The dashboard player default is independent of the connection selected in reports. External players keep their own configuration. Only the public ingest key is included; read and management credentials stay private.
    """

    id: str
    """Id identifies this saved analytics connection."""

    created_at: datetime
    """CreatedAt records when this connection was added."""

    default_for_dashboard: bool
    """
    DefaultForDashboard selects this connection for Chunkify dashboard players,
    public previews, the playground and newly generated snippets. It does not change
    existing external players. At most one connection per project is selected.
    """

    endpoint: str
    """Endpoint specifies the analytics server base URL.

    It does not configure the player.
    """

    name: str
    """Name identifies this connection in the dashboard."""

    project_id: str
    """ProjectId identifies the owning Chunkify project."""

    status: Literal["preparing", "ready", "failed"]
    """
    Status indicates whether the connection is ready to read or requires setup
    repair.
    """

    type: Literal["hosted", "custom"]
    """Type specifies whether Chunkify manages the analytics project."""

    updated_at: datetime
    """UpdatedAt records when this connection was last changed."""

    allowed_origins: Optional[List[str]] = None
    """
    AllowedOrigins lists additional website origins permitted to ingest events for a
    hosted connection. Shared installation origins remain allowed. An empty list
    clears project-specific origins. Custom servers manage origins on their own
    infrastructure.
    """

    last_checked_at: Optional[datetime] = None
    """LastCheckedAt records the most recent successful connection check."""

    public_ingest_key: Optional[str] = None
    """
    PublicIngestKey is the public browser ingestion key used by Chunkify previews
    and player examples. It cannot read or manage analytics. Hosted connections use
    their primary public key. Omitted when preview tracking is not configured.
    """

    retention_seconds: Optional[int] = None
    """RetentionSeconds is the last retention applied to a hosted project, in seconds.

    Omitted for custom connections.
    """
