# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .workflow_caption import WorkflowCaption
from .workflow_output_binding import WorkflowOutputBinding

__all__ = ["WorkflowCaptionAction"]


class WorkflowCaptionAction(BaseModel):
    """
    Generates or reuses original captions and their transcript from the Asset's speech.
    """

    id: str
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: WorkflowCaption
    """Params specifies caption generation settings. Pass an empty object."""

    type: Literal["create_caption"]
    """Type specifies the action to perform. Must be create_caption."""

    transcript_id: Optional[WorkflowOutputBinding] = None
    """TranscriptId binds caption publication to the transcript in the triggering
    event.

    Use it only when connected to create_transcript. When omitted, creates or reuses
    the Asset’s original transcript.
    """
