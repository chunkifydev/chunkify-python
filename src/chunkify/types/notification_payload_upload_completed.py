# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification_payload_upload_completed_data import NotificationPayloadUploadCompletedData

__all__ = ["NotificationPayloadUploadCompleted"]


class NotificationPayloadUploadCompleted(BaseModel):
    """Notification for upload.completed."""

    id: str
    """Unique identifier of the notification"""

    data: NotificationPayloadUploadCompletedData
    """Payload for the event named in event.

    Replays preserve the original data; retrieve the resource for current state and
    fresh signed URLs.
    """

    date: datetime
    """Timestamp of the event payload."""

    event: Literal["upload.completed"]
    """Type of event that triggered the notification."""
