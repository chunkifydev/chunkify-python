# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .webhook_event import WebhookEvent

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    url: Required[str]
    """
    Url is the endpoint that will receive webhook notifications, which must be a
    valid HTTP URL.
    """

    enabled: bool
    """Enabled indicates whether the webhook is active."""

    events: List[WebhookEvent]
    """Events specifies the types of events that will trigger the webhook."""
