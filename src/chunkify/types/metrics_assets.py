# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metrics_asset_day import MetricsAssetDay
from .metrics_asset_values import MetricsAssetValues

__all__ = ["MetricsAssets"]


class MetricsAssets(BaseModel):
    """Measurements saved on retained Assets.

    Explicit deletion can change historical results; temporary media cleanup does not erase saved Asset measurements.
    """

    daily: List[MetricsAssetDay]
    """Daily specifies one record for each selected creation day, oldest first."""

    from_: str = FieldInfo(alias="from")
    """From specifies the inclusive UTC start date."""

    summary: MetricsAssetValues
    """Summary specifies the complete creation-date cohort."""

    to: str
    """To specifies the exclusive UTC end date."""
