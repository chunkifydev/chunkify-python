# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification_payload_source_created_data import NotificationPayloadSourceCreatedData

__all__ = ["NotificationPayloadSourceCreated"]


class NotificationPayloadSourceCreated(BaseModel):
    """Notification for source.created."""

    id: str
    """Unique identifier of the notification"""

    data: NotificationPayloadSourceCreatedData
    """Payload for the event named in event.

    Replays preserve the original data; retrieve the resource for current state and
    fresh signed URLs.
    """

    date: datetime
    """Timestamp of the event payload."""

    event: Literal["source.created"]
    """Type of event that triggered the notification."""
