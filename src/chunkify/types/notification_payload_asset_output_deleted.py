# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification_payload_asset_output_deleted_data import NotificationPayloadAssetOutputDeletedData

__all__ = ["NotificationPayloadAssetOutputDeleted"]


class NotificationPayloadAssetOutputDeleted(BaseModel):
    """Notification for asset.output.deleted."""

    id: str
    """Unique identifier of the notification"""

    data: NotificationPayloadAssetOutputDeletedData
    """Payload for the event named in event.

    Replays preserve the original data; retrieve the resource for current state and
    fresh signed URLs.
    """

    date: datetime
    """Timestamp of the event payload."""

    event: Literal["asset.output.deleted"]
    """Type of event that triggered the notification."""
