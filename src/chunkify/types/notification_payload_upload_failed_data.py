# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .upload import Upload
from .._models import BaseModel

__all__ = ["NotificationPayloadUploadFailedData"]


class NotificationPayloadUploadFailedData(BaseModel):
    """Payload data structure for upload.failed and upload.expired events"""

    upload: Upload
