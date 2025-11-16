# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .notification import Notification

__all__ = ["NotificationRetrieveResponse"]


class NotificationRetrieveResponse(BaseModel):
    data: Optional[Notification] = None

    status: Optional[str] = None
    """Status indicates the response status "success" """
