# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification_payload_asset_data import NotificationPayloadAssetData

__all__ = ["NotificationPayloadAsset"]


class NotificationPayloadAsset(BaseModel):
    """
    Notification for asset.created, asset.ready, asset.playback_ready, asset.failed and asset.expired.
    """

    id: str
    """Unique identifier of the notification"""

    data: NotificationPayloadAssetData
    """Payload for the event named in event.

    Replays preserve the original data; retrieve the resource for current state and
    fresh signed URLs.
    """

    date: datetime
    """Timestamp of the event payload."""

    event: Literal["asset.created", "asset.ready", "asset.playback_ready", "asset.failed", "asset.expired"]
    """Type of event that triggered the notification."""
