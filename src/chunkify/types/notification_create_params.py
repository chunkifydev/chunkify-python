# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .webhook_event import WebhookEvent

__all__ = ["NotificationCreateParams"]


class NotificationCreateParams(TypedDict, total=False):
    event: Required[WebhookEvent]
    """Event specifies the type of event that triggered the notification."""

    object_id: Required[str]
    """ID of the resource that triggered the event.

    Use the caption, static rendition, or thumbnail ID for their Asset child events.
    Replaying asset events, job.created, or source.created requires a retained
    snapshot. Resource deletion does not prevent replay.
    """

    webhook_id: Required[str]
    """WebhookId specifies the webhook endpoint that will receive the notification."""
