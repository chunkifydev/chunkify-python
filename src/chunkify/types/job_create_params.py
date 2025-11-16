# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .jpg_param import JpgParam
from .hls_av1_param import HlsAv1Param
from .mp4_av1_param import MP4Av1Param
from .hls_h264_param import HlsH264Param
from .hls_h265_param import HlsH265Param
from .mp4_h264_param import MP4H264Param
from .mp4_h265_param import MP4H265Param
from .webm_vp9_param import WebmVp9Param

__all__ = ["JobCreateParams", "Format", "Storage", "Transcoder"]


class JobCreateParams(TypedDict, total=False):
    format: Required[Format]
    """
    Required format configuration, one and only one valid format configuration must
    be provided. If you want to use a format without specifying any configuration,
    use an empty object in the corresponding field.
    """

    source_id: Required[str]
    """The ID of the source file to transcode"""

    hls_manifest_id: str
    """
    Optional HLS manifest configuration Use the same hls manifest ID to group
    multiple jobs into a single HLS manifest By default, it's automatically
    generated if no set for HLS jobs
    """

    metadata: Dict[str, str]
    """Optional metadata to attach to the job (max 1024 bytes)"""

    storage: Storage
    """Optional storage configuration"""

    transcoder: Transcoder
    """Optional transcoder configuration.

    If not provided, the system will automatically calculate the optimal quantity
    and CPU type based on the source file specifications and output requirements.
    This auto-scaling ensures efficient resource utilization.
    """


class Format(TypedDict, total=False):
    hls_av1: HlsAv1Param
    """FFmpeg encoding parameters specific to HLS with AV1 encoding."""

    hls_h264: HlsH264Param
    """FFmpeg encoding parameters specific to HLS with H.264 encoding."""

    hls_h265: HlsH265Param
    """FFmpeg encoding parameters specific to HLS with H.265 encoding."""

    jpg: JpgParam
    """FFmpeg encoding parameters specific to JPEG image extraction."""

    mp4_av1: MP4Av1Param
    """FFmpeg encoding parameters specific to MP4 with AV1 encoding."""

    mp4_h264: MP4H264Param
    """FFmpeg encoding parameters specific to MP4 with H.264 encoding."""

    mp4_h265: MP4H265Param
    """FFmpeg encoding parameters specific to MP4 with H.265 encoding."""

    webm_vp9: WebmVp9Param
    """FFmpeg encoding parameters specific to WebM with VP9 encoding."""


class Storage(TypedDict, total=False):
    id: str
    """
    Storage Id specifies the storage configuration to use from pre-configured
    storage options. Must be 4-64 characters long and contain only alphanumeric
    characters, underscores and hyphens. Optional if Storage Path is provided.
    """

    path: str
    """
    Storage Path specifies a custom storage path where processed files will be
    stored. Must be a valid file path with max length of 1024 characters. Optional
    if Storage Id is provided.
    """


class Transcoder(TypedDict, total=False):
    quantity: int
    """
    Quantity specifies the number of transcoder instances to use (1-50). Required if
    Type is set.
    """

    type: Literal["4vCPU", "8vCPU", "16vCPU"]
    """
    Type specifies the CPU configuration for each transcoder instance. Required if
    Quantity is set.
    """
