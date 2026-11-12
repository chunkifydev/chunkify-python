# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["Notification"]


class Notification(BaseModel):
    id: str
    """Unique identifier of the notification"""

    created_at: datetime
    """Timestamp when the notification was created"""

    event: Literal[
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
    """Type of event that triggered this notification"""

    object_id: str
    """ID of the object that triggered this notification"""

    payload: str
    """JSON payload that was sent to the webhook endpoint"""

    webhook: Webhook
    """Webhook endpoint configuration that received this notification"""

    event_id: Optional[str] = None
    """Originating event ID, when recorded by the event log."""

    response_status_code: Optional[int] = None
    """HTTP status code received from the webhook endpoint"""
