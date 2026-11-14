# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["JobFormatID"]

JobFormatID: TypeAlias = Literal[
    "mp4_h264", "mp4_h265", "mp4_av1", "webm_vp9", "hls_h264", "hls_h265", "hls_av1", "jpg"
]
