# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.response_ok import ResponseOk

__all__ = ["LogListResponse", "LogListResponseData"]


class LogListResponseData(BaseModel):
    attributes: Optional[object] = None
    """Additional structured data attached to the log"""

    job_id: Optional[str] = None
    """Optional ID of the job this log is associated with"""

    level: Optional[str] = None
    """Log level (e.g. "info", "error", "debug")"""

    msg: Optional[str] = None
    """The log message content"""

    service: Optional[str] = None
    """Name of the service that generated the log"""

    time: Optional[str] = None
    """Timestamp when the log was created"""


class LogListResponse(ResponseOk):
    data: Optional[List[LogListResponseData]] = None  # type: ignore
