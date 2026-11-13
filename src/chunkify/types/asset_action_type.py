# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AssetActionType"]

AssetActionType: TypeAlias = Literal[
    "create_static_rendition", "create_caption", "create_transcript", "translate_caption", "create_thumbnails"
]
