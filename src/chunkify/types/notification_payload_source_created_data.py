# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .source import Source
from .._models import BaseModel

__all__ = ["NotificationPayloadSourceCreatedData"]


class NotificationPayloadSourceCreatedData(BaseModel):
    """Payload for source.created.

    The Source has been validated and saved. Thumbnails may still be pending.
    """

    source: Source
