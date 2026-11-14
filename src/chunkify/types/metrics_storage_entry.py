# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .metrics_storage_day import MetricsStorageDay
from .metrics_storage_values import MetricsStorageValues

__all__ = ["MetricsStorageEntry"]


class MetricsStorageEntry(BaseModel):
    """Activity for one persistent storage configuration."""

    daily: List[MetricsStorageDay]
    """Daily specifies one record for each selected event day, oldest first."""

    storage_id: str
    """StorageId identifies the persistent storage configuration."""

    summary: MetricsStorageValues
    """Summary specifies recorded activity in the selected period."""
