# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .workflow_static_action import WorkflowStaticAction
from .workflow_caption_action import WorkflowCaptionAction
from .workflow_thumbnail_action import WorkflowThumbnailAction
from .workflow_transcript_action import WorkflowTranscriptAction
from .workflow_translation_action import WorkflowTranslationAction

__all__ = ["WorkflowAction"]

WorkflowAction: TypeAlias = Annotated[
    Union[
        WorkflowStaticAction,
        WorkflowCaptionAction,
        WorkflowTranslationAction,
        WorkflowThumbnailAction,
        WorkflowTranscriptAction,
    ],
    PropertyInfo(discriminator="type"),
]
