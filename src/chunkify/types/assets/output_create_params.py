# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from ..asset_caption_output_create_params import AssetCaptionOutputCreateParams
from ..asset_thumbnail_output_create_params import AssetThumbnailOutputCreateParams
from ..asset_transcript_output_create_params import AssetTranscriptOutputCreateParams
from ..asset_static_rendition_output_create_params import AssetStaticRenditionOutputCreateParams

__all__ = ["OutputCreateParams", "Output"]


class OutputCreateParams(TypedDict, total=False):
    output: Required[Output]
    """Create one output for an Asset.

    Type selects its required, strictly validated parameters.
    """


Output: TypeAlias = Union[
    AssetCaptionOutputCreateParams,
    AssetStaticRenditionOutputCreateParams,
    AssetThumbnailOutputCreateParams,
    AssetTranscriptOutputCreateParams,
]
