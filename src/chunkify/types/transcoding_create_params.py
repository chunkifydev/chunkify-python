# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

from .transcoding_m4a_aac_param import TranscodingM4aAacParam
from .transcoding_mp4_av1_param import TranscodingMP4Av1Param
from .transcoding_mp4_h264_param import TranscodingMP4H264Param
from .transcoding_mp4_h265_param import TranscodingMP4H265Param
from .transcoding_webm_vp9_param import TranscodingWebmVp9Param

__all__ = ["TranscodingCreateParams", "Format", "Storage"]


class TranscodingCreateParams(TypedDict, total=False):
    format: Required[Format]
    """Format specifies the requested encoding settings."""

    source_id: Required[str]
    """SourceId identifies a Source in this Project."""

    metadata: Dict[str, str]
    """Metadata attaches string values to the Transcoding.

    The serialized object may contain at most 2048 bytes.
    """

    storage: Storage
    """Storage overrides the Project output destination.

    Source storage remains independent.
    """


Format: TypeAlias = Union[
    TranscodingMP4H264Param,
    TranscodingMP4H265Param,
    TranscodingMP4Av1Param,
    TranscodingWebmVp9Param,
    TranscodingM4aAacParam,
]


class Storage(TypedDict, total=False):
    """Storage overrides the Project output destination.

    Source storage remains independent.
    """

    id: str
    """Id specifies a Storage in this Project. Defaults to the Project output storage."""

    path: str
    """
    Path specifies the output object path relative to the selected Storage
    base_prefix. Required for customer storage; generated for Chunkify temporary
    storage. The extension must match the resolved output format. The combined path
    may contain at most 1024 bytes.
    """
