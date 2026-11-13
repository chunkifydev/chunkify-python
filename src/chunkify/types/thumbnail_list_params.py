# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .thumbnail_status import ThumbnailStatus

__all__ = ["ThumbnailListParams", "Created"]


class ThumbnailListParams(TypedDict, total=False):
    id: str
    """Id filters by an exact Thumbnail ID. Omit to include all matching resources."""

    created: Created

    limit: int
    """Maximum number of Thumbnails to return."""

    offset: int
    """Number of Thumbnails to skip."""

    source_id: str
    """Filter Thumbnails linked to this Source.

    Omit to include Thumbnails from all Sources in the Project.
    """

    status: ThumbnailStatus
    """Filter by Thumbnail status."""

    storage_id: str
    """Filter by output Storage ID."""


class Created(TypedDict, total=False):
    gte: int
    """Created at or after this Unix timestamp in seconds."""

    lte: int
    """Created at or before this Unix timestamp in seconds."""

    sort: Literal["asc", "desc"]
    """Creation-time ordering. Defaults to newest first."""
