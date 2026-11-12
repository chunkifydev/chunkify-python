# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkflowCaptionAction", "TranscriptID"]


class TranscriptID(BaseModel):
    """TranscriptId binds caption publication to the transcript in the triggering event.

    Use it only when connected to create_transcript. When omitted, creates or reuses the Asset’s original transcript.
    """

    from_: Literal["event.output.id"] = FieldInfo(alias="from")
    """From specifies where to read the input output ID.

    Use event.output.id to consume the output in the triggering asset.output.ready
    event.
    """


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

    params: object
    """Params specifies caption generation settings. Pass an empty object."""

    type: Literal["create_caption"]
    """Type specifies the action to perform. Must be create_caption."""

    transcript_id: Optional[TranscriptID] = None
    """TranscriptId binds caption publication to the transcript in the triggering
    event.

    Use it only when connected to create_transcript. When omitted, creates or reuses
    the Asset’s original transcript.
    """
