# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.log import Log

__all__ = ["LogListResponse"]


class LogListResponse(BaseModel):
    """Response containing a list of logs for a job"""

    data: List[Log]

    status: Literal["success"]
    """Status indicates the response status "success" """
