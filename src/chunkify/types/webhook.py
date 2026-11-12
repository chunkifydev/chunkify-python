# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    id: str
    """Unique identifier of the webhook"""

    enabled: bool
    """Whether the webhook is currently enabled"""

    events: List[
        Literal[
            "job.created",
            "job.completed",
            "job.failed",
            "job.cancelled",
            "source.created",
            "source.deleted",
            "upload.created",
            "upload.completed",
            "upload.failed",
            "upload.expired",
            "asset.created",
            "asset.ready",
            "asset.playback_ready",
            "asset.failed",
            "asset.expired",
            "asset.deleted",
            "asset.output.created",
            "asset.output.ready",
            "asset.output.failed",
            "asset.output.deleted",
            "workflow_run.created",
            "workflow_run.completed",
            "workflow_run.failed",
            "workflow_run.cancelled",
            "transcoding.created",
            "transcoding.ready",
            "transcoding.failed",
            "transcoding.cancelled",
            "transcoding.expired",
            "transcoding.deleted",
            "thumbnail.created",
            "thumbnail.ready",
            "thumbnail.failed",
            "thumbnail.expired",
            "thumbnail.deleted",
        ]
    ]
    """Array of event types this webhook subscribes to"""

    project_id: str
    """ID of the project this webhook belongs to"""

    url: str
    """URL where webhook events will be sent"""
