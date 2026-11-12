# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["AnalyticsKey"]


class AnalyticsKey(BaseModel):
    """One key per purpose.

    Public player values remain available; read and MCP values are returned only on creation or rotation.
    """

    id: str
    """Id identifies this key in the collector."""

    purpose: Literal["player", "read", "mcp"]
    """
    Purpose distinguishes player ingestion, read-only API access and a separate
    read-only MCP credential. Read and MCP keys have the same collector permissions.
    """

    public_key: Optional[str] = None
    """PublicKey is the browser ingestion credential for a player key.

    Omitted for read-only API and MCP keys, whose secret values are shown once.
    """
