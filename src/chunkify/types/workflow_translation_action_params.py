# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .workflow_translation_params import WorkflowTranslationParams
from .workflow_output_binding_params import WorkflowOutputBindingParams

__all__ = ["WorkflowTranslationActionParams"]


class WorkflowTranslationActionParams(TypedDict, total=False):
    """Translates or reuses an original caption in one target language.

    Requires an asset.output.ready rule connected to an original caption creation action.
    """

    id: Required[str]
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    caption_id: Required[WorkflowOutputBindingParams]
    """
    CaptionId specifies the binding to the original caption in the triggering event.
    """

    params: Required[WorkflowTranslationParams]
    """Params specifies the target language."""

    type: Required[Literal["translate_caption"]]
    """Type specifies the action to perform. Must be translate_caption."""
