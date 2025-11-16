# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Job", "Error", "Format", "Storage", "Transcoder"]


class Error(BaseModel):
    detail: Optional[str] = None
    """Additional error details or output"""

    message: Optional[str] = None
    """Main error message"""

    type: Optional[str] = None
    """Type of error (e.g., "ffmpeg", "network", "storage", etc.)"""


class Format(BaseModel):
    config: Optional[object] = None
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
    id: Optional[str] = None
    """Unique identifier for the job"""

    billable_time: Optional[int] = None
    """Billable time in seconds"""

    created_at: Optional[str] = None
    """Creation timestamp"""

    error: Optional[Error] = None
    """Error message for the job"""

    format: Optional[Format] = None
    """A template defines the transcoding parameters and settings for a job"""

    hls_manifest_id: Optional[str] = None
    """HLS manifest ID"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the job"""

    progress: Optional[float] = None
    """Progress percentage of the job (0-100)"""

    source_id: Optional[str] = None
    """ID of the source video being transcoded"""

    started_at: Optional[str] = None
    """When the job started processing"""

    status: Optional[str] = None
    """
    Current status of the job (e.g., "queued", "ingesting","transcoding",
    "downloading", "merging", "uploading", "failed", "completed")
    """

    storage: Optional[Storage] = None
    """Storage settings for where the job output will be saved"""

    transcoder: Optional[Transcoder] = None
    """The transcoder configuration for a job"""

    updated_at: Optional[str] = None
    """Last update timestamp"""
