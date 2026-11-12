# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .workflow_translation_params_param import WorkflowTranslationParamsParam

__all__ = ["WorkflowTranslationActionParam", "CaptionID"]

_CaptionIDReservedKeywords = TypedDict(
    "_CaptionIDReservedKeywords",
    {
        "from": Literal["event.output.id"],
    },
    total=False,
)


class CaptionID(_CaptionIDReservedKeywords, total=False):
    """
    CaptionId specifies the binding to the original caption in the triggering event.
    """

    pass


class WorkflowTranslationActionParam(TypedDict, total=False):
    """Translates or reuses an original caption in one target language.

    Requires an asset.output.ready rule connected to an original caption creation action.
    """

    id: Required[str]
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    caption_id: Required[CaptionID]
    """
    CaptionId specifies the binding to the original caption in the triggering event.
    """

    params: Required[WorkflowTranslationParamsParam]
    """Params specifies the target language."""

    type: Required[Literal["translate_caption"]]
    """Type specifies the action to perform. Must be translate_caption."""
