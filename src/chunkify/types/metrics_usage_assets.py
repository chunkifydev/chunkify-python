# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["MetricsUsageAssets"]


class MetricsUsageAssets(BaseModel):
    """Asset processing usage."""

    failed: int
    """Failed specifies recorded failed Asset outcomes."""

    input_seconds: int
    """InputSeconds specifies settled billable Asset input duration."""

    input_seconds_by_resolution: Dict[str, int]
    """Video duration in seconds by pricing resolution tier: sd, hd, 2k and uhd."""

    ready: int
    """Ready specifies recorded successful Asset outcomes."""
