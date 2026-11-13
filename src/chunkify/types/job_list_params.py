# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .job_format_id import JobFormatID

__all__ = ["JobListParams", "Created"]


class JobListParams(TypedDict, total=False):
    id: str
    """Filter by job ID"""

    created: Created

    format_id: JobFormatID
    """Filter by format id"""

    hls_manifest_id: str
    """Filter by hls manifest ID"""

    limit: int
    """Pagination limit"""

    metadata: Iterable[SequenceNotStr[str]]
    """Filter by metadata"""

    offset: int
    """Pagination offset"""

    source_id: str
    """Filter by source ID"""

    status: Literal["completed", "processing", "failed", "cancelled", "queued", "pending"]
    """Filter by job status"""


class Created(TypedDict, total=False):
    gte: int
    """Filter by creation date greater than or equal"""

    lte: int
    """Filter by creation date less than or equal"""

    sort: Literal["asc", "desc"]
    """Sort by creation date (asc/desc)"""
