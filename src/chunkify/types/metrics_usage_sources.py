# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MetricsUsageSources"]


class MetricsUsageSources(BaseModel):
    """Source ingestion activity."""

    bytes: int
    """
    Bytes specifies cumulative ingested Source bytes, not current storage occupancy.
    """

    created: int
    """Created specifies the number of ingested Sources."""

    ingested_seconds: int
    """IngestedSeconds specifies ingested media duration in seconds."""
