# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkflowListParams"]


class WorkflowListParams(TypedDict, total=False):
    archived: bool
    """Archived specifies whether to include archived Workflows. Defaults to false."""

    limit: int
    """Limit specifies the maximum number of results to return. Accepts 1 to 100.

    Defaults to 100.
    """

    offset: int
    """Offset specifies the number of matching results to skip. Must be at least 0.

    Defaults to 0.
    """
