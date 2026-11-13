# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AssetCaptionOutputParams"]


class AssetCaptionOutputParams(TypedDict, total=False):
    """
    Parameters for original captions or a translation of an existing caption on this Asset.
    """

    language_code: Literal[
        "en", "fr", "es", "de", "it", "pt", "nl", "ja", "ko", "zh", "ar", "hi", "ru", "tr", "pl", "sv"
    ]
    """LanguageCode specifies the target language for a translated caption.

    Supply source_caption_id with this field. Omit both fields to transcribe the
    Asset audio with automatic language detection.
    """

    source_caption_id: str
    """SourceCaptionId specifies the caption on this Asset to translate.

    Supply language_code with this field. Omit both fields to generate original
    captions.
    """
