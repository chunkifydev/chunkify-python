# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .asset_thumbnail_create_params import AssetThumbnailCreateParams

__all__ = ["AssetThumbnailOutputCreateParams"]


class AssetThumbnailOutputCreateParams(TypedDict, total=False):
    """Create an Asset-owned thumbnail output."""

    params: Required[AssetThumbnailCreateParams]
    """Params specifies the settings for this output type."""

    type: Required[Literal["thumbnail"]]
    """Type specifies the output kind to create."""
