# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .workflow_translation_language_code import WorkflowTranslationLanguageCode

__all__ = ["WorkflowTranslation"]


class WorkflowTranslation(BaseModel):
    """Parameters for translating one original caption into another language."""

    language_code: WorkflowTranslationLanguageCode
    """
    LanguageCode specifies the target language for the translated subtitle track,
    such as en or fr. The same code appears in the caption and HLS manifest.
    """
