# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .webhook import Webhook
from .response_ok import ResponseOk

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(ResponseOk):
    data: Optional[Webhook] = None  # type: ignore
