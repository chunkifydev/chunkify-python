# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .transcoding_m4a_aac_param import TranscodingM4aAacParam
from .transcoding_mp4_av1_param import TranscodingMP4Av1Param
from .transcoding_mp4_h264_param import TranscodingMP4H264Param
from .transcoding_mp4_h265_param import TranscodingMP4H265Param
from .transcoding_webm_vp9_param import TranscodingWebmVp9Param

__all__ = ["TranscodingCreateFormatParams"]

TranscodingCreateFormatParams: TypeAlias = Union[
    TranscodingMP4H264Param,
    TranscodingMP4H265Param,
    TranscodingMP4Av1Param,
    TranscodingWebmVp9Param,
    TranscodingM4aAacParam,
]
