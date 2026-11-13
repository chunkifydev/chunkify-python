# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification_payload_workflow_run_data import NotificationPayloadWorkflowRunData

__all__ = ["NotificationPayloadWorkflowRun"]


class NotificationPayloadWorkflowRun(BaseModel):
    """
    Notification for workflow_run.created, workflow_run.completed, workflow_run.failed and workflow_run.cancelled.
    """

    id: str
    """Unique identifier of the notification"""

    data: NotificationPayloadWorkflowRunData
    """Payload for the event named in event.

    Replays preserve the original data; retrieve the resource for current state and
    fresh signed URLs.
    """

    date: datetime
    """Timestamp of the event payload."""

    event: Literal["workflow_run.created", "workflow_run.completed", "workflow_run.failed", "workflow_run.cancelled"]
    """Type of event that triggered the notification."""
