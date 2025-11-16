# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    enabled: bool
    """Enabled indicates whether the webhook should be enabled or disabled."""

    events: SequenceNotStr[str]
    """Events specifies the types of events that will trigger the webhook."""
