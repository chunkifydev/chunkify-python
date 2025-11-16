# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UploadListParams", "Created"]


class UploadListParams(TypedDict, total=False):
    id: str
    """Filter by upload ID"""

    created: Created

    limit: int
    """Pagination limit (max 100)"""

    metadata: str
    """Filter by metadata (format: key:value,key:value)"""

    offset: int
    """Pagination offset"""

    source_id: str
    """Filter by source ID"""

    status: str
    """Filter by status (pending, completed, error)"""


class Created(TypedDict, total=False):
    gte: str
    """Filter by creation date greater than or equal (RFC3339)"""

    lte: str
    """Filter by creation date less than or equal (RFC3339)"""

    sort: str
    """Sort by creation date (asc/desc)"""
