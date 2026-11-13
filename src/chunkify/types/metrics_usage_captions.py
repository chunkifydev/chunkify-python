# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MetricsUsageCaptions"]


class MetricsUsageCaptions(BaseModel):
    """Caption processing usage."""

    transcription_seconds: int
    """TranscriptionSeconds specifies audio duration transcribed."""

    translation_seconds: int
    """
    TranslationSeconds specifies caption duration translated, counted once per
    target language.
    """
