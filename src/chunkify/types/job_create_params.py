# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .jpg_param import JpgParam
from .hls_av1_param import HlsAv1Param
from .mp4_av1_param import MP4Av1Param
from .hls_h264_param import HlsH264Param
from .hls_h265_param import HlsH265Param
from .mp4_h264_param import MP4H264Param
from .mp4_h265_param import MP4H265Param
from .webm_vp9_param import WebmVp9Param

__all__ = [
    "JobCreateParams",
    "Format",
    "FormatHlsAv1",
    "FormatHlsH264",
    "FormatHlsH265",
    "FormatJpg",
    "FormatMP4Av1",
    "FormatMP4H264",
    "FormatMP4H265",
    "FormatWebmVp9",
    "Storage",
    "Transcoder",
]


class JobCreateParams(TypedDict, total=False):
    format: Required[Format]
    """Required format configuration..."""

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


class FormatHlsAv1(TypedDict, total=False):
    hls_av1: Required[HlsAv1Param]
    """FFmpeg encoding parameters specific to HLS with AV1 encoding."""


class FormatHlsH264(TypedDict, total=False):
    hls_h264: Required[HlsH264Param]
    """FFmpeg encoding parameters specific to HLS with H.264 encoding."""


class FormatHlsH265(TypedDict, total=False):
    hls_h265: Required[HlsH265Param]
    """FFmpeg encoding parameters specific to HLS with H.265 encoding."""


class FormatJpg(TypedDict, total=False):
    jpg: Required[JpgParam]
    """FFmpeg encoding parameters specific to JPEG image extraction."""


class FormatMP4Av1(TypedDict, total=False):
    mp4_av1: Required[MP4Av1Param]
    """FFmpeg encoding parameters specific to MP4 with AV1 encoding."""


class FormatMP4H264(TypedDict, total=False):
    mp4_h264: Required[MP4H264Param]
    """FFmpeg encoding parameters specific to MP4 with H.264 encoding."""


class FormatMP4H265(TypedDict, total=False):
    mp4_h265: Required[MP4H265Param]
    """FFmpeg encoding parameters specific to MP4 with H.265 encoding."""


class FormatWebmVp9(TypedDict, total=False):
    webm_vp9: Required[WebmVp9Param]
    """FFmpeg encoding parameters specific to WebM with VP9 encoding."""


Format: TypeAlias = Union[
    FormatHlsAv1, FormatHlsH264, FormatHlsH265, FormatJpg, FormatMP4Av1, FormatMP4H264, FormatMP4H265, FormatWebmVp9
]


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
