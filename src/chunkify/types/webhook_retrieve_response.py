# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .webhook import Webhook
from .shared.response_ok import ResponseOk

__all__ = ["WebhookRetrieveResponse"]


class WebhookRetrieveResponse(ResponseOk):
    data: Webhook
