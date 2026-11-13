# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .metrics_storage_values import MetricsStorageValues

__all__ = ["MetricsStorageDay"]


class MetricsStorageDay(MetricsStorageValues):
    """Recorded storage activity grouped by event day."""

    date: str
    """Date specifies the UTC event day."""
