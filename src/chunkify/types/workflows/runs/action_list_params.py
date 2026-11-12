# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ActionListParams", "Created"]


class ActionListParams(TypedDict, total=False):
    workflow_id: Required[Annotated[str, PropertyInfo(alias="workflowId")]]

    asset_id: str
    """AssetId specifies the Asset whose results to return.

    Omit it to include all Assets.
    """

    created: Created

    limit: int
    """Limit specifies the maximum number of results to return. Accepts 1 to 100.

    Defaults to 100.
    """

    offset: int
    """Offset specifies the number of matching results to skip. Must be at least 0.

    Defaults to 0.
    """

    status: Literal["pending", "running", "waiting", "completed", "failed", "skipped", "cancelled"]
    """Status specifies the action status to filter by.

    Omit it to include all statuses.
    """

    type: Literal["create_static_rendition", "create_caption", "create_transcript", "translate_caption"]
    """Type specifies the action type to filter by.

    Omit it to include all action types.
    """


class Created(TypedDict, total=False):
    gte: int
    """Created at or after this Unix timestamp in seconds."""

    lte: int
    """Created at or before this Unix timestamp in seconds."""
