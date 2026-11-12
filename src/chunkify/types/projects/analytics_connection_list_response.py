# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .analytics_connection import AnalyticsConnection

__all__ = ["AnalyticsConnectionListResponse"]


class AnalyticsConnectionListResponse(BaseModel):
    data: List[AnalyticsConnection]
    """Saved connections in creation order."""

    status: Literal["success"]
