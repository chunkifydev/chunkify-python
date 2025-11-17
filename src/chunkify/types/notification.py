# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["Notification"]


class Notification(BaseModel):
    id: str
    """Unique identifier of the notification"""

    created_at: str
    """Timestamp when the notification was created"""

    event: str
    """Type of event that triggered this notification"""

    object_id: str
    """ID of the object that triggered this notification"""

    payload: str
    """JSON payload that was sent to the webhook endpoint"""

    response_status_code: int
    """HTTP status code received from the webhook endpoint"""

    webhook: Webhook
    """Webhook endpoint configuration that received this notification"""
