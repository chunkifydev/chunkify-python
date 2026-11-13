# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from . import jpg, hls_av1, mp4_av1, hls_h264, hls_h265, mp4_h264, mp4_h265, webm_vp9
from .._utils import PropertyInfo
from .job_format_id import JobFormatID

__all__ = ["JobFormat", "MP4Av1", "MP4H264", "MP4H265", "WebmVp9", "HlsAv1", "HlsH264", "HlsH265", "Jpg"]


class MP4Av1(mp4_av1.MP4Av1):
    """FFmpeg encoding parameters specific to MP4 with AV1 encoding."""

    id: JobFormatID  # type: ignore
    """The format ID"""


class MP4H264(mp4_h264.MP4H264):
    """FFmpeg encoding parameters specific to MP4 with H.264 encoding."""

    id: JobFormatID  # type: ignore
    """The format ID"""


class MP4H265(mp4_h265.MP4H265):
    """FFmpeg encoding parameters specific to MP4 with H.265 encoding."""

    id: JobFormatID  # type: ignore
    """The format ID"""


class WebmVp9(webm_vp9.WebmVp9):
    """FFmpeg encoding parameters specific to WebM with VP9 encoding."""

    id: JobFormatID  # type: ignore
    """The format ID"""


class HlsAv1(hls_av1.HlsAv1):
    """FFmpeg encoding parameters specific to HLS with AV1 encoding.

    When per-title optimization is disabled, either audio_bitrate or video_bitrate is required.
    """

    id: JobFormatID  # type: ignore
    """The format ID"""


class HlsH264(hls_h264.HlsH264):
    """FFmpeg encoding parameters specific to HLS with H.264 encoding.

    When per-title optimization is disabled, either audio_bitrate or video_bitrate is required.
    """

    id: JobFormatID  # type: ignore
    """The format ID"""


class HlsH265(hls_h265.HlsH265):
    """FFmpeg encoding parameters specific to HLS with H.265 encoding.

    When per-title optimization is disabled, either audio_bitrate or video_bitrate is required.
    """

    id: JobFormatID  # type: ignore
    """The format ID"""


class Jpg(jpg.Jpg):
    """FFmpeg encoding parameters specific to JPEG image extraction."""

    id: JobFormatID  # type: ignore
    """The format ID"""


JobFormat: TypeAlias = Annotated[
    Union[MP4Av1, MP4H264, MP4H265, WebmVp9, HlsAv1, HlsH264, HlsH265, Jpg], PropertyInfo(discriminator="id")
]
