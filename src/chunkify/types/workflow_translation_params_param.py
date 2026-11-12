# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WorkflowTranslationParamsParam"]


class WorkflowTranslationParamsParam(TypedDict, total=False):
    """Parameters for translating one original caption into another language."""

    language_code: Required[
        Literal["en", "fr", "es", "de", "it", "pt", "nl", "ja", "ko", "zh", "ar", "hi", "ru", "tr", "pl", "sv"]
    ]
    """
    LanguageCode specifies the target language for the translated subtitle track,
    such as en or fr. The same code appears in the caption and HLS manifest.
    """
