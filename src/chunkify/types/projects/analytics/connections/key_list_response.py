# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ....._models import BaseModel
from .analytics_key import AnalyticsKey

__all__ = ["KeyListResponse"]


class KeyListResponse(BaseModel):
    data: List[AnalyticsKey]

    status: Literal["success"]
