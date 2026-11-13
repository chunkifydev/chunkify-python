# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .metrics_usage_assets import MetricsUsageAssets
from .metrics_usage_egress import MetricsUsageEgress
from .metrics_credits_spent import MetricsCreditsSpent
from .metrics_usage_sources import MetricsUsageSources
from .metrics_usage_uploads import MetricsUsageUploads
from .metrics_usage_captions import MetricsUsageCaptions
from .metrics_usage_thumbnails import MetricsUsageThumbnails
from .metrics_usage_transcodings import MetricsUsageTranscodings
from .metrics_usage_notifications import MetricsUsageNotifications
from .metrics_usage_static_renditions import MetricsUsageStaticRenditions

__all__ = ["MetricsUsageValues"]


class MetricsUsageValues(BaseModel):
    """Recorded usage for a UTC accounting day or a complete period."""

    assets: MetricsUsageAssets
    """Asset processing usage."""

    captions: MetricsUsageCaptions
    """Caption processing usage."""

    credits_spent: MetricsCreditsSpent
    """Settled credits in integer units, with 10000 units equal to USD 1 of credits.

    Category values are parts of total, not additional charges.
    """

    egress: MetricsUsageEgress
    """Recorded output egress eligible for the transfer tariff.

    Provider-exempt transfers are excluded.
    """

    notifications: MetricsUsageNotifications
    """Webhook delivery activity."""

    sources: MetricsUsageSources
    """Source ingestion activity."""

    static_renditions: MetricsUsageStaticRenditions
    """Static rendition usage."""

    thumbnails: MetricsUsageThumbnails
    """Thumbnail processing usage."""

    transcodings: MetricsUsageTranscodings
    """Standalone Transcoding usage."""

    uploads: MetricsUsageUploads
    """Upload activity."""
