# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification_payload_upload_failed_data import NotificationPayloadUploadFailedData

__all__ = ["NotificationPayloadUploadFailed"]


class NotificationPayloadUploadFailed(BaseModel):
    """Notification for upload.failed and upload.expired."""

    id: str
    """Unique identifier of the notification"""

    data: NotificationPayloadUploadFailedData
    """Payload for the event named in event.

    Replays preserve the original data; retrieve the resource for current state and
    fresh signed URLs.
    """

    date: datetime
    """Timestamp of the event payload."""

    event: Literal["upload.failed", "upload.expired"]
    """Type of event that triggered the notification."""
