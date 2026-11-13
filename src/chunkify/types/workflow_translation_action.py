# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .workflow_translation import WorkflowTranslation
from .workflow_output_binding import WorkflowOutputBinding

__all__ = ["WorkflowTranslationAction"]


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

    caption_id: WorkflowOutputBinding
    """
    CaptionId specifies the binding to the original caption in the triggering event.
    """

    params: WorkflowTranslation
    """Params specifies the target language."""

    type: Literal["translate_caption"]
    """Type specifies the action to perform. Must be translate_caption."""
