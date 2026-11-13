# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MetricsUsageUploads"]


class MetricsUsageUploads(BaseModel):
    """Upload activity."""

    bytes: int
    """Bytes specifies successfully uploaded bytes."""

    completed: int
    """Completed specifies successfully completed Uploads."""

    failed: int
    """Failed specifies recorded failed Uploads."""
