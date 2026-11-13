# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification_payload_transcoding_data import NotificationPayloadTranscodingData

__all__ = ["NotificationPayloadTranscoding"]


class NotificationPayloadTranscoding(BaseModel):
    """
    Notification for transcoding.created, transcoding.ready, transcoding.failed, transcoding.cancelled, transcoding.expired and transcoding.deleted.
    """

    id: str
    """Unique identifier of the notification"""

    data: NotificationPayloadTranscodingData
    """Payload for the event named in event.

    Replays preserve the original data; retrieve the resource for current state and
    fresh signed URLs.
    """

    date: datetime
    """Timestamp of the event payload."""

    event: Literal[
        "transcoding.created",
        "transcoding.ready",
        "transcoding.failed",
        "transcoding.cancelled",
        "transcoding.expired",
        "transcoding.deleted",
    ]
    """Type of event that triggered the notification."""
