# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .asset_caption_output_params import AssetCaptionOutputParams

__all__ = ["AssetCaptionOutputCreateParams"]


class AssetCaptionOutputCreateParams(TypedDict, total=False):
    """Create an Asset-owned caption output."""

    params: Required[AssetCaptionOutputParams]
    """Params specifies the settings for this output type."""

    type: Required[Literal["caption"]]
    """Type specifies the output kind to create."""
