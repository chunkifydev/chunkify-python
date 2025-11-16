# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ResponseError", "Error"]


class Error(BaseModel):
    code: Optional[int] = None
    """Code is the HTTP status code"""

    message: Optional[str] = None
    """Message is a human-readable error description"""

    type: Optional[str] = None
    """Type indicates the error category"""


class ResponseError(BaseModel):
    error: Optional[Error] = None
    """Error response details"""

    status: Optional[str] = None
    """Status indicates the response status "error" """
