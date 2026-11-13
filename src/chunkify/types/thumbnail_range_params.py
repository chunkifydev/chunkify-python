# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ThumbnailRangeParams"]


class ThumbnailRangeParams(TypedDict, total=False):
    """Optional Source-relative sampling boundaries."""

    end: float
    """End specifies the exclusive upper bound in seconds.

    Defaults to the Source duration.
    """

    start: float
    """Start specifies the inclusive lower bound in seconds. Defaults to zero."""
