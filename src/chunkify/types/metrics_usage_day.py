# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .metrics_usage_values import MetricsUsageValues

__all__ = ["MetricsUsageDay"]


class MetricsUsageDay(MetricsUsageValues):
    """Daily recorded usage. Inactive days contain zero counters."""

    date: str
    """Date specifies the UTC accounting day."""
