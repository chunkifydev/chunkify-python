# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification_payload_thumbnail_data import NotificationPayloadThumbnailData

__all__ = ["NotificationPayloadThumbnail"]


class NotificationPayloadThumbnail(BaseModel):
    """
    Notification for thumbnail.created, thumbnail.ready, thumbnail.failed, thumbnail.expired and thumbnail.deleted.
    """

    id: str
    """Unique identifier of the notification"""

    data: NotificationPayloadThumbnailData
    """Payload for the event named in event.

    Replays preserve the original data; retrieve the resource for current state and
    fresh signed URLs.
    """

    date: datetime
    """Timestamp of the event payload."""

    event: Literal["thumbnail.created", "thumbnail.ready", "thumbnail.failed", "thumbnail.expired", "thumbnail.deleted"]
    """Type of event that triggered the notification."""
