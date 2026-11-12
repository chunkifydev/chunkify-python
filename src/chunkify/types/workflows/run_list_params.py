# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RunListParams", "Created"]


class RunListParams(TypedDict, total=False):
    asset_id: str
    """AssetId specifies the Asset whose results to return.

    Omit it to include all Assets.
    """

    created: Created

    event_id: str
    """EventId specifies the triggering event ID to filter by.

    Omit it to include all events.
    """

    latest_per_asset: bool
    """
    LatestPerAsset specifies whether to return only the latest matching run for each
    Asset. Defaults to false. Pagination and total count apply to Assets when true.
    """

    limit: int
    """Limit specifies the maximum number of results to return. Accepts 1 to 100.

    Defaults to 100.
    """

    offset: int
    """Offset specifies the number of matching results to skip. Must be at least 0.

    Defaults to 0.
    """

    status: Literal["pending", "running", "completed", "failed", "cancelled"]
    """Status specifies the run status to filter by. Omit it to include all statuses."""


class Created(TypedDict, total=False):
    gte: int
    """Created at or after this Unix timestamp in seconds."""

    lte: int
    """Created at or before this Unix timestamp in seconds."""
