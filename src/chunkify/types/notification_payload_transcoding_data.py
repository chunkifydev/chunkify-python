# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .transcoding import Transcoding

__all__ = ["NotificationPayloadTranscodingData"]


class NotificationPayloadTranscodingData(BaseModel):
    """
    Payload for transcoding.created, transcoding.ready, transcoding.failed, transcoding.cancelled, transcoding.expired and transcoding.deleted events.
    """

    transcoding: Transcoding
    """Transcoding contains the canonical resource snapshot at the event time."""
