# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metrics_usage_day import MetricsUsageDay
from .metrics_usage_values import MetricsUsageValues

__all__ = ["MetricsUsage"]


class MetricsUsage(BaseModel):
    """Project usage for the selected UTC accounting period."""

    daily: List[MetricsUsageDay]
    """Daily specifies one record for every selected day, oldest first."""

    from_: str = FieldInfo(alias="from")
    """From specifies the inclusive UTC start date."""

    summary: MetricsUsageValues
    """Summary specifies totals across the selected period."""

    to: str
    """To specifies the exclusive UTC end date."""
