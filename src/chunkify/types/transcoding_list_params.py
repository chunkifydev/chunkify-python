# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .transcoding_status import TranscodingStatus

__all__ = ["TranscodingListParams", "Created"]


class TranscodingListParams(TypedDict, total=False):
    id: str
    """Id filters by an exact Transcoding ID. Omit to include all matching resources."""

    created: Created

    limit: int
    """Maximum number of Transcodings to return."""

    offset: int
    """Number of Transcodings to skip."""

    source_id: str
    """Filter Transcodings linked to this Source.

    Omit to include Transcodings from all Sources in the Project.
    """

    status: TranscodingStatus
    """Filter by Transcoding status."""

    storage_id: str
    """Filter by output Storage ID."""


class Created(TypedDict, total=False):
    gte: int
    """Created at or after this Unix timestamp in seconds."""

    lte: int
    """Created at or before this Unix timestamp in seconds."""

    sort: Literal["asc", "desc"]
    """Creation-time ordering. Defaults to newest first."""
