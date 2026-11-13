# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .asset_transcript_output_params import AssetTranscriptOutputParams

__all__ = ["AssetTranscriptOutputCreateParams"]


class AssetTranscriptOutputCreateParams(TypedDict, total=False):
    """Create or reuse the original-language transcript for an Asset.

    Caption generation shares this transcript and its speech-recognition charge.
    """

    params: Required[AssetTranscriptOutputParams]
    """Parameters for an original-language transcript.

    Pass an empty object; the spoken language is detected automatically.
    """

    type: Required[Literal["transcript"]]
    """Type specifies the output kind."""
