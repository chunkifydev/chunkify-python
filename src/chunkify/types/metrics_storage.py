# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metrics_storage_entry import MetricsStorageEntry

__all__ = ["MetricsStorage"]


class MetricsStorage(BaseModel):
    """Recorded additions and successful removals within event retention.

    Excludes external storage changes and does not measure current storage size.
    """

    from_: str = FieldInfo(alias="from")
    """From specifies the inclusive UTC start date."""

    storages: List[MetricsStorageEntry]
    """
    Storages specifies persistent project storage configurations, including those
    without recorded activity. Chunkify temporary storage is excluded.
    """

    to: str
    """To specifies the exclusive UTC end date."""
