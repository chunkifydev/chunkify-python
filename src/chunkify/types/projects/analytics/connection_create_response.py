# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .analytics_connection import AnalyticsConnection

__all__ = ["ConnectionCreateResponse"]


class ConnectionCreateResponse(BaseModel):
    data: AnalyticsConnection
    """A saved source for analytics reports.

    The dashboard player default is independent of the connection selected in
    reports. External players keep their own configuration. Only the public ingest
    key is included; read and management credentials stay private.
    """

    status: Literal["success"]

    public_key: Optional[str] = None
    """PublicKey is the hosted ingestion key.

    It remains available as public_ingest_key on the connection. Omitted for custom
    connections.
    """
