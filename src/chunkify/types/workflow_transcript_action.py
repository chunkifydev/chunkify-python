# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkflowTranscriptAction"]


class WorkflowTranscriptAction(BaseModel):
    """Creates or reuses the original-language transcript.

    Can run alongside caption generation in the same asset.ready rule.
    """

    id: str
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: object
    """Params specifies transcript settings. Pass an empty object."""

    type: Literal["create_transcript"]
    """Type specifies the action to perform. Must be create_transcript."""
