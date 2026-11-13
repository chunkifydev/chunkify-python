# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .upload import Upload
from .._models import BaseModel

__all__ = ["NotificationPayloadUploadCreatedData"]


class NotificationPayloadUploadCreatedData(BaseModel):
    """Payload for upload.created.

    A waiting upload session has been created; its Source is created only after successful completion. Transfer credentials are not included.
    """

    upload: Upload
