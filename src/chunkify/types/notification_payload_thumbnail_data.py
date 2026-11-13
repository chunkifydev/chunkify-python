# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .thumbnail import Thumbnail

__all__ = ["NotificationPayloadThumbnailData"]


class NotificationPayloadThumbnailData(BaseModel):
    """A canonical thumbnail snapshot for standalone thumbnail.* events.

    Asset-owned thumbnails use the Asset output event payload.
    """

    thumbnail: Thumbnail
    """Thumbnail contains the resource at the event time."""
