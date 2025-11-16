# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["NotificationListParams", "Created", "ResponseStatusCode"]


class NotificationListParams(TypedDict, total=False):
    created: Created

    events: SequenceNotStr[str]
    """Filter by events (e.g.

    job.completed, job.failed, upload.completed, upload.failed, upload.expired)
    """

    limit: int
    """Pagination limit (max 100)"""

    object_id: str
    """Filter by object ID"""

    offset: int
    """Pagination offset"""

    response_status_code: ResponseStatusCode

    webhook_id: str
    """Filter by webhook ID"""


class Created(TypedDict, total=False):
    gte: str
    """Filter by creation date greater than or equal (RFC3339)"""

    lte: str
    """Filter by creation date less than or equal (RFC3339)"""

    sort: str
    """Sort by creation date (asc/desc)"""


class ResponseStatusCode(TypedDict, total=False):
    eq: int
    """Filter by exact response status code"""

    gte: int
    """Filter by response status code greater than or equal"""

    lte: int
    """Filter by response status code less than or equal"""
