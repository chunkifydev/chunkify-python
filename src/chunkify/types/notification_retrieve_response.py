# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .notification import Notification

__all__ = ["NotificationRetrieveResponse"]


class NotificationRetrieveResponse(BaseModel):
    data: Notification
    """Data contains the response object"""

    status: str
    """Status indicates the response status "success" """
