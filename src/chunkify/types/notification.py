# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["Notification"]


class Notification(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the notification"""

    created_at: Optional[str] = None
    """Timestamp when the notification was created"""

    event: Optional[str] = None
    """Type of event that triggered this notification"""

    object_id: Optional[str] = None
    """ID of the object that triggered this notification"""

    payload: Optional[str] = None
    """JSON payload that was sent to the webhook endpoint"""

    response_status_code: Optional[int] = None
    """HTTP status code received from the webhook endpoint"""

    webhook: Optional[Webhook] = None
    """Webhook endpoint configuration that received this notification"""
