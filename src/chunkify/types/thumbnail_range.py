# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ThumbnailRange"]


class ThumbnailRange(BaseModel):
    """The resolved Source-relative sampling range."""

    end: float
    """End specifies the exclusive upper bound in seconds."""

    start: float
    """Start specifies the inclusive lower bound in seconds."""
