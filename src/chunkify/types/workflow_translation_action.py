# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow_translation_params import WorkflowTranslationParams

__all__ = ["WorkflowTranslationAction", "CaptionID"]


class CaptionID(BaseModel):
    """
    CaptionId specifies the binding to the original caption in the triggering event.
    """

    from_: Literal["event.output.id"] = FieldInfo(alias="from")
    """From specifies where to read the input output ID.

    Use event.output.id to consume the output in the triggering asset.output.ready
    event.
    """


class WorkflowTranslationAction(BaseModel):
    """Translates or reuses an original caption in one target language.

    Requires an asset.output.ready rule connected to an original caption creation action.
    """

    id: str
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    caption_id: CaptionID
    """
    CaptionId specifies the binding to the original caption in the triggering event.
    """

    params: WorkflowTranslationParams
    """Params specifies the target language."""

    type: Literal["translate_caption"]
    """Type specifies the action to perform. Must be translate_caption."""
