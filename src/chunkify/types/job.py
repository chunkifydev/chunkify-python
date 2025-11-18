# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel
from .shared.chunkify_error import ChunkifyError

__all__ = ["Job", "Format", "Storage", "Transcoder"]


class Format(BaseModel):
    config: Optional[Dict[str, object]] = None
    """Configuration parameters for the template.

    A map of configuration values specific to the format For example, for mp4/h264
    format this includes parameters like crf, preset, profile etc.
    """

    name: Optional[str] = None
    """Name of the transcoding template.The format to use for transcoding.

    Valid formats are: mp4/h264, mp4/h265, mp4/av1, webm/vp9, hls/h264, hls/h265,
    hls/av1, jpg
    """


class Storage(BaseModel):
    id: Optional[str] = None
    """ID of the storage"""

    path: Optional[str] = None
    """Path where the output will be stored"""


class Transcoder(BaseModel):
    quantity: Optional[int] = None
    """Number of instances allocated"""

    type: Optional[str] = None
    """Type of transcoder instance"""


class Job(BaseModel):
    id: str
    """Unique identifier for the job"""

    billable_time: int
    """Billable time in seconds"""

    created_at: str
    """Creation timestamp"""

    format: Format
    """A template defines the transcoding parameters and settings for a job"""

    progress: float
    """Progress percentage of the job (0-100)"""

    source_id: str
    """ID of the source video being transcoded"""

    status: str
    """
    Current status of the job (e.g., "queued", "ingesting","transcoding",
    "downloading", "merging", "uploading", "failed", "completed")
    """

    storage: Storage
    """Storage settings for where the job output will be saved"""

    transcoder: Transcoder
    """The transcoder configuration for a job"""

    updated_at: str
    """Last update timestamp"""

    error: Optional[ChunkifyError] = None
    """Error message for the job"""

    hls_manifest_id: Optional[str] = None
    """HLS manifest ID"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the job"""

    started_at: Optional[str] = None
    """When the job started processing"""
