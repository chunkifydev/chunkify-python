# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .response_ok import ResponseOk
from .notification import Notification

__all__ = ["NotificationCreateResponse"]


class NotificationCreateResponse(ResponseOk):
    data: Optional[Notification] = None  # type: ignore
