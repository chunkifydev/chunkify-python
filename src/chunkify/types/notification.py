# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .webhook import Webhook
from .._models import BaseModel
from .webhook_event import WebhookEvent

__all__ = ["Notification"]


class Notification(BaseModel):
    id: str
    """Unique identifier of the notification"""

    created_at: datetime
    """Timestamp when the notification was created"""

    event: WebhookEvent
    """Type of event that triggered this notification"""

    object_id: str
    """ID of the object that triggered this notification"""

    payload: str
    """JSON payload that was sent to the webhook endpoint"""

    webhook: Webhook
    """Webhook endpoint configuration that received this notification"""

    event_id: Optional[str] = None
    """Originating event ID, when recorded by the event log."""

    response_status_code: Optional[int] = None
    """HTTP status code received from the webhook endpoint"""
