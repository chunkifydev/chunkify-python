# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AssetStaticRenditionCreateParams"]


class AssetStaticRenditionCreateParams(TypedDict, total=False):
    """Parameters for an independently processed H.264 MP4 rendition."""

    resolution: Required[Literal["highest", "240p", "360p", "480p", "540p", "720p", "1080p", "1440p", "2160p"]]
    """H.264 MP4 resolution.

    highest selects the largest supported output without upscaling. Hobby supports
    up to 1080p; other plans support up to 2160p. Independent of the streaming
    resolution limits.
    """
