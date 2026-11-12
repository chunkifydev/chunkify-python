# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .workflow_static_action_param import WorkflowStaticActionParam
from .workflow_caption_action_param import WorkflowCaptionActionParam
from .workflow_thumbnail_action_param import WorkflowThumbnailActionParam
from .workflow_transcript_action_param import WorkflowTranscriptActionParam
from .workflow_translation_action_param import WorkflowTranslationActionParam

__all__ = ["WorkflowActionParam"]

WorkflowActionParam: TypeAlias = Union[
    WorkflowStaticActionParam,
    WorkflowCaptionActionParam,
    WorkflowTranslationActionParam,
    WorkflowThumbnailActionParam,
    WorkflowTranscriptActionParam,
]
