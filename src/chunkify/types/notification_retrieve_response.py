# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .notification import Notification
from .shared.response_ok import ResponseOk

__all__ = ["NotificationRetrieveResponse"]


class NotificationRetrieveResponse(ResponseOk):
    data: Notification
