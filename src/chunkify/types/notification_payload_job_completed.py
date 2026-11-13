# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification_payload_job_completed_data import NotificationPayloadJobCompletedData

__all__ = ["NotificationPayloadJobCompleted"]


class NotificationPayloadJobCompleted(BaseModel):
    """Notification for job.completed."""

    id: str
    """Unique identifier of the notification"""

    data: NotificationPayloadJobCompletedData
    """Payload for the event named in event.

    Replays preserve the original data; retrieve the resource for current state and
    fresh signed URLs.
    """

    date: datetime
    """Timestamp of the event payload."""

    event: Literal["job.completed"]
    """Type of event that triggered the notification."""
