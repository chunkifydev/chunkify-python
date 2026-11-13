# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .workflow_caption_params import WorkflowCaptionParams
from .workflow_output_binding_params import WorkflowOutputBindingParams

__all__ = ["WorkflowCaptionActionParams"]


class WorkflowCaptionActionParams(TypedDict, total=False):
    """
    Generates or reuses original captions and their transcript from the Asset's speech.
    """

    id: Required[str]
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: Required[WorkflowCaptionParams]
    """Params specifies caption generation settings. Pass an empty object."""

    type: Required[Literal["create_caption"]]
    """Type specifies the action to perform. Must be create_caption."""

    transcript_id: WorkflowOutputBindingParams
    """TranscriptId binds caption publication to the transcript in the triggering
    event.

    Use it only when connected to create_transcript. When omitted, creates or reuses
    the Asset’s original transcript.
    """
