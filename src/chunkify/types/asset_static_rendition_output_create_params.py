# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .asset_static_rendition_create_params import AssetStaticRenditionCreateParams

__all__ = ["AssetStaticRenditionOutputCreateParams"]


class AssetStaticRenditionOutputCreateParams(TypedDict, total=False):
    """Create an Asset-owned static rendition output."""

    params: Required[AssetStaticRenditionCreateParams]
    """Params specifies the settings for this output type."""

    type: Required[Literal["static_rendition"]]
    """Type specifies the output kind to create."""
