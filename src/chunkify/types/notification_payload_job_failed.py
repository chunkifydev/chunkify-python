# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification_payload_job_failed_data import NotificationPayloadJobFailedData

__all__ = ["NotificationPayloadJobFailed"]


class NotificationPayloadJobFailed(BaseModel):
    """Notification for job.failed and job.cancelled."""

    id: str
    """Unique identifier of the notification"""

    data: NotificationPayloadJobFailedData
    """Payload for the event named in event.

    Replays preserve the original data; retrieve the resource for current state and
    fresh signed URLs.
    """

    date: datetime
    """Timestamp of the event payload."""

    event: Literal["job.failed", "job.cancelled"]
    """Type of event that triggered the notification."""
