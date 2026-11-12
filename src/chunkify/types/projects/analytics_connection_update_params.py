# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["AnalyticsConnectionUpdateParams"]


class AnalyticsConnectionUpdateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    allowed_origins: SequenceNotStr[str]
    """
    AllowedOrigins lists additional website origins permitted to ingest events for a
    hosted connection. Shared installation origins remain allowed. An empty list
    clears project-specific origins. Custom servers manage origins on their own
    infrastructure.
    """

    default_for_dashboard: bool
    """
    DefaultForDashboard selects this ready connection for Chunkify dashboard
    players, public previews, the playground and newly generated snippets. Requires
    a public ingest key. Setting true replaces the previous default atomically.
    Setting false disables dashboard tracking if no default remains; another
    connection is not selected automatically. Existing external players keep their
    own configuration.
    """

    endpoint: str
    """Endpoint specifies a replacement custom server base URL.

    Supply read_key together with it.
    """

    name: str
    """Name identifies this connection in the dashboard."""

    public_ingest_key: str
    """PublicIngestKey optionally enables preview tracking for a custom connection.

    Supply the public ingestion key for the same analytics project as read_key. It
    is returned in connection reads and used in browser code. Omit for hosted
    connections. An empty string disables preview tracking. A replacement endpoint
    clears the saved public key unless a replacement is supplied.
    """

    read_key: str
    """ReadKey replaces the custom connection credential after validation.

    Its value is never returned.
    """
