# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["EventListParams", "Created"]


class EventListParams(TypedDict, total=False):
    created: Created

    events: List[
        Literal[
            "job.created",
            "job.completed",
            "job.failed",
            "job.cancelled",
            "source.created",
            "source.deleted",
            "upload.created",
            "upload.completed",
            "upload.failed",
            "upload.expired",
            "asset.created",
            "asset.ready",
            "asset.playback_ready",
            "asset.failed",
            "asset.expired",
            "asset.deleted",
            "asset.output.created",
            "asset.output.ready",
            "asset.output.failed",
            "asset.output.deleted",
            "workflow_run.created",
            "workflow_run.completed",
            "workflow_run.failed",
            "workflow_run.cancelled",
            "transcoding.created",
            "transcoding.ready",
            "transcoding.failed",
            "transcoding.cancelled",
            "transcoding.expired",
            "transcoding.deleted",
            "thumbnail.created",
            "thumbnail.ready",
            "thumbnail.failed",
            "thumbnail.expired",
            "thumbnail.deleted",
        ]
    ]
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
