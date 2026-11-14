# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .asset_status import AssetStatus

__all__ = ["AssetListParams", "Created"]


class AssetListParams(TypedDict, total=False):
    created: Created

    limit: int
    """Maximum number of Assets to return."""

    metadata: SequenceNotStr[str]
    """Repeat key:value pairs to match all supplied metadata conditions."""

    offset: int
    """Number of Assets to skip."""

    search: str
    """Case-insensitive search of Asset IDs and titles."""

    source_id: str
    """Filter Assets linked to this Source.

    Omit to include Assets from all Sources in the Project.
    """

    status: AssetStatus
    """Filter by Asset status."""

    storage_id: str
    """Filter by output Storage ID."""


class Created(TypedDict, total=False):
    gte: int
    """Created at or after this Unix timestamp in seconds."""

    lte: int
    """Created at or before this Unix timestamp in seconds."""

    sort: Literal["asc", "desc"]
    """Creation-time ordering. Defaults to newest first."""
