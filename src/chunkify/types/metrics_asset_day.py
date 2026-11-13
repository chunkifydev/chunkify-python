# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .metrics_asset_values import MetricsAssetValues

__all__ = ["MetricsAssetDay"]


class MetricsAssetDay(MetricsAssetValues):
    """Asset measurements grouped by creation day."""

    date: str
    """Date specifies the UTC Asset creation day."""
