# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["JobListParams", "Created"]


class JobListParams(TypedDict, total=False):
    id: str
    """Filter by job ID"""

    created: Created

    format_name: str
    """Filter by format name"""

    hls_manifest_id: str
    """Filter by hls manifest ID"""

    limit: int
    """Pagination limit"""

    metadata: str
    """Filter by metadata (format: key:value,key2:value2)"""

    offset: int
    """Pagination offset"""

    source_id: str
    """Filter by source ID"""

    status: str
    """Filter by job status"""


class Created(TypedDict, total=False):
    gte: str
    """Filter by creation date greater than or equal"""

    lte: str
    """Filter by creation date less than or equal"""

    sort: str
    """Sort by creation date (asc/desc)"""
