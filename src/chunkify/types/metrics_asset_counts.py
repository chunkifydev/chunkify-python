# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MetricsAssetCounts"]


class MetricsAssetCounts(BaseModel):
    """Asset outcomes grouped by Asset creation date."""

    completed: int
    """Completed specifies Assets with a recorded ready timestamp."""

    failed: int
    """Failed specifies retained Assets currently in failed status."""

    processed_seconds: float
    """
    ProcessedSeconds specifies measured media duration of completed Assets,
    preserving fractional seconds.
    """

    saved: int
    """Saved specifies retained Assets created in the period."""
