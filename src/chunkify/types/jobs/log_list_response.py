# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from ..shared.response_ok import ResponseOk

__all__ = ["LogListResponse", "LogListResponseData"]


class LogListResponseData(BaseModel):
    attributes: Dict[str, object]
    """Additional structured data attached to the log"""

    level: str
    """Log level (e.g. "info", "error", "debug")"""

    msg: str
    """The log message content"""

    service: str
    """Name of the service that generated the log"""

    time: str
    """Timestamp when the log was created"""

    job_id: Optional[str] = None
    """Optional ID of the job this log is associated with"""


class LogListResponse(ResponseOk):
    data: List[LogListResponseData]
