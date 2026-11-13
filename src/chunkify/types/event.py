# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .notification import Notification
from .webhook_event import WebhookEvent

__all__ = ["Event"]


class Event(BaseModel):
    """A retained lifecycle event, recorded independently of webhook subscriptions.

    The payload is an immutable JSON snapshot.
    """

    id: str
    """Unique event ID."""

    created_at: datetime
    """Time the event occurred."""

    delivery_count: int
    """Number of retained webhook delivery attempts."""

    delivery_status: Literal["none", "pending", "delivered", "failed"]
    """Summary of the latest retained attempt for each webhook.

    none means no retained attempts; pending means at least one latest attempt is
    awaiting delivery; failed means at least one latest attempt failed and none are
    pending; delivered means all latest attempts succeeded. Earlier failures
    superseded by successful retries do not mark the event failed.
    """

    event: WebhookEvent

    expires_at: datetime
    """Retention deadline set from the project team plan when the event was recorded.

    Deliveries and retries share this deadline.
    """

    object_id: str
    """ID of the resource that caused this event."""

    payload: str
    """Immutable JSON event envelope.

    Its ID is the event ID; webhook delivery envelopes retain their notification
    IDs. Signed links in historical snapshots may have expired.
    """

    related_object_ids: List[str]
    """Related resource IDs retained independently of resource deletion."""

    deliveries: Optional[List[Notification]] = None
    """First 100 delivery attempts, oldest first; included on retrieval.

    List notifications with event_id to paginate all attempts.
    """
