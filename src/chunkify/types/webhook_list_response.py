# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .webhook import Webhook
from .shared.response_ok import ResponseOk

__all__ = ["WebhookListResponse"]


class WebhookListResponse(ResponseOk):
    data: Optional[List[Webhook]] = None  # type: ignore
