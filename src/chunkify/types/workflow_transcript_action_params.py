# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .workflow_transcript_params import WorkflowTranscriptParams

__all__ = ["WorkflowTranscriptActionParams"]


class WorkflowTranscriptActionParams(TypedDict, total=False):
    """Creates or reuses the original-language transcript.

    Can run alongside caption generation in the same asset.ready rule.
    """

    id: Required[str]
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: Required[WorkflowTranscriptParams]
    """Params specifies transcript settings. Pass an empty object."""

    type: Required[Literal["create_transcript"]]
    """Type specifies the action to perform. Must be create_transcript."""
