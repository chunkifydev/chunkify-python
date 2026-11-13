# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .workflow_translation_language_code import WorkflowTranslationLanguageCode

__all__ = ["WorkflowTranslationParams"]


class WorkflowTranslationParams(TypedDict, total=False):
    """Parameters for translating one original caption into another language."""

    language_code: Required[WorkflowTranslationLanguageCode]
    """
    LanguageCode specifies the target language for the translated subtitle track,
    such as en or fr. The same code appears in the caption and HLS manifest.
    """
