# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkflowTranslationParams"]


class WorkflowTranslationParams(BaseModel):
    """Parameters for translating one original caption into another language."""

    language_code: Literal[
        "en", "fr", "es", "de", "it", "pt", "nl", "ja", "ko", "zh", "ar", "hi", "ru", "tr", "pl", "sv"
    ]
    """
    LanguageCode specifies the target language for the translated subtitle track,
    such as en or fr. The same code appears in the caption and HLS manifest.
    """
