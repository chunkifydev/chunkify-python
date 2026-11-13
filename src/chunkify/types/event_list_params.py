# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .webhook_event import WebhookEvent

__all__ = ["EventListParams", "Created"]


class EventListParams(TypedDict, total=False):
    created: Created

    events: List[WebhookEvent]
    """Filter by events"""

    limit: int
    """Pagination limit (max 100)"""

    object_id: str
    """
    Filter by the primary or a related resource ID, including retained associations
    after resource deletion.
    """

    offset: int
    """Pagination offset"""


class Created(TypedDict, total=False):
    gte: int
    """Filter by creation date greater than or equal (UNIX epoch time)"""

    lte: int
    """Filter by creation date less than or equal (UNIX epoch time)"""

    sort: Literal["asc", "desc"]
    """Sort by creation date (asc/desc)"""
