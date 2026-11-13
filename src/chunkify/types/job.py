# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .job_format import JobFormat
from .job_storage import JobStorage
from .job_transcoder import JobTranscoder
from .shared.chunkify_error import ChunkifyError

__all__ = ["Job"]


class Job(BaseModel):
    id: str
    """Unique identifier for the job"""

    billable_time: int
    """Billable time in seconds"""

    created_at: datetime
    """Creation timestamp"""

    format: JobFormat
    """The format parameters and settings for a job"""

    progress: float
    """Progress percentage of the job (0-100)"""

    source_id: str
    """ID of the source media being processed"""

    status: Literal[
        "pending",
        "queued",
        "ingesting",
        "transcoding",
        "downloading",
        "merging",
        "uploading",
        "failed",
        "completed",
        "cancelled",
        "merged",
        "downloaded",
        "transcoded",
        "waiting",
    ]
    """Current status of the job."""

    storage: JobStorage
    """Storage settings for where the job output will be saved"""

    updated_at: datetime
    """Last update timestamp"""

    error: Optional[ChunkifyError] = None
    """Error message for the job"""

    hls_manifest_id: Optional[str] = None
    """HLS manifest ID"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the job"""

    started_at: Optional[datetime] = None
    """When the job started processing"""

    transcoder: Optional[JobTranscoder] = None
    """The transcoder configuration for a job"""
