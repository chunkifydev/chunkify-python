# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification_payload_asset_output_data import NotificationPayloadAssetOutputData

__all__ = ["NotificationPayloadAssetOutput"]


class NotificationPayloadAssetOutput(BaseModel):
    """
    Notification for asset.output.created, asset.output.ready and asset.output.failed.
    """

    id: str
    """Unique identifier of the notification"""

    data: NotificationPayloadAssetOutputData
    """Payload for the event named in event.

    Replays preserve the original data; retrieve the resource for current state and
    fresh signed URLs.
    """

    date: datetime
    """Timestamp of the event payload."""

    event: Literal["asset.output.created", "asset.output.ready", "asset.output.failed"]
    """Type of event that triggered the notification."""
