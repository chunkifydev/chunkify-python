# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ThumbnailError"]


class ThumbnailError(BaseModel):
    """A customer-facing processing failure."""

    code: str
    """Code identifies the processing failure."""

    message: str
    """Message explains the processing failure."""
