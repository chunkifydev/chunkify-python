# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WorkflowThumbnailRange"]


class WorkflowThumbnailRange(BaseModel):
    """Optional Source-relative sampling boundaries."""

    end: Optional[float] = None
    """End specifies the exclusive upper bound in seconds.

    Defaults to the Source duration.
    """

    start: Optional[float] = None
    """Start specifies the inclusive lower bound in seconds. Defaults to zero."""
