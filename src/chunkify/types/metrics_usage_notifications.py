# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MetricsUsageNotifications"]


class MetricsUsageNotifications(BaseModel):
    """Webhook delivery activity."""

    failed: int
    """Failed specifies recorded failed webhook delivery attempts."""

    sent: int
    """Sent specifies recorded successful webhook deliveries."""
