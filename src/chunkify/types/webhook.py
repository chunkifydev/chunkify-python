# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the webhook"""

    enabled: Optional[bool] = None
    """Whether the webhook is currently enabled"""

    events: Optional[List[str]] = None
    """Array of event types this webhook subscribes to"""

    project_id: Optional[str] = None
    """ID of the project this webhook belongs to"""

    url: Optional[str] = None
    """URL where webhook events will be sent"""
