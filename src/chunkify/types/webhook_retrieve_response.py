# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["WebhookRetrieveResponse"]


class WebhookRetrieveResponse(BaseModel):
    data: Optional[Webhook] = None

    status: Optional[str] = None
    """Status indicates the response status "success" """
