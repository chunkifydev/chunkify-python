# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .source import Source
from .upload import Upload
from .._models import BaseModel

__all__ = ["NotificationPayloadUploadCompletedData"]


class NotificationPayloadUploadCompletedData(BaseModel):
    """Payload data structure for upload.completed events"""

    source: Source

    upload: Upload
