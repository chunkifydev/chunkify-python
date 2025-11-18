# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .webhook import Webhook
from .._models import BaseModel

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    data: Webhook
    """Data contains the response object"""

    status: str
    """Status indicates the response status "success" """
