# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnalyticsConnectionCreateParams"]


class AnalyticsConnectionCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name identifies this connection in the dashboard."""

    type: Required[Literal["hosted", "custom"]]
    """Type specifies whether Chunkify manages the analytics project."""

    endpoint: str
    """Endpoint specifies the custom server base URL.

    Required for custom connections and omitted for hosted connections.
    """

    public_ingest_key: str
    """PublicIngestKey optionally enables preview tracking for a custom connection.

    Supply the public ingestion key for the same analytics project as read_key. It
    is returned in connection reads and used in browser code. Omit for hosted
    connections.
    """

    read_key: str
    """ReadKey supplies a read-only project credential for a custom connection.

    Required for custom connections and omitted for hosted connections. Stored
    encrypted and never returned.
    """
