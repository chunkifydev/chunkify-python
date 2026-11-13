# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .workflow_static_action_params import WorkflowStaticActionParams
from .workflow_caption_action_params import WorkflowCaptionActionParams
from .workflow_thumbnail_action_params import WorkflowThumbnailActionParams
from .workflow_transcript_action_params import WorkflowTranscriptActionParams
from .workflow_translation_action_params import WorkflowTranslationActionParams

__all__ = ["WorkflowActionParams"]

WorkflowActionParams: TypeAlias = Union[
    WorkflowStaticActionParams,
    WorkflowCaptionActionParams,
    WorkflowTranslationActionParams,
    WorkflowThumbnailActionParams,
    WorkflowTranscriptActionParams,
]
