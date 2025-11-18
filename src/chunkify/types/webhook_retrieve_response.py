# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["WebhookRetrieveResponse"]


class WebhookRetrieveResponse(BaseModel):
    data: Webhook
    """Data contains the response object"""

    status: str
    """Status indicates the response status "success" """
