# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MetricsUsageThumbnails"]


class MetricsUsageThumbnails(BaseModel):
    """Thumbnail processing usage."""

    images_published: int
    """ImagesPublished specifies the number of published thumbnail images."""

    sets_failed: int
    """SetsFailed specifies recorded failed Thumbnail requests."""

    sets_ready: int
    """SetsReady specifies recorded successful Thumbnail requests."""
