# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .source import Source
from .._models import BaseModel

__all__ = ["NotificationPayloadSourceDeletedData"]


class NotificationPayloadSourceDeletedData(BaseModel):
    """Payload for source.deleted.

    The Source was deleted on request or after the team's data retention period. Resources created from it are preserved and no longer report its source_id.
    """

    source: Source
    """Source contains the last snapshot before deletion."""
