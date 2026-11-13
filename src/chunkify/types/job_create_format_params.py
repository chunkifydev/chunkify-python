# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .jpg_param import JpgParam
from .hls_av1_param import HlsAv1Param
from .mp4_av1_param import MP4Av1Param
from .hls_h264_param import HlsH264Param
from .hls_h265_param import HlsH265Param
from .mp4_h264_param import MP4H264Param
from .mp4_h265_param import MP4H265Param
from .webm_vp9_param import WebmVp9Param

__all__ = ["JobCreateFormatParams"]

JobCreateFormatParams: TypeAlias = Union[
    MP4Av1Param, MP4H264Param, MP4H265Param, WebmVp9Param, HlsAv1Param, HlsH264Param, HlsH265Param, JpgParam
]
