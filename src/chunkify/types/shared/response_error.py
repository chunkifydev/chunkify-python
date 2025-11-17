# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ResponseError", "Error"]


class Error(BaseModel):
    code: int
    """Code is the HTTP status code"""

    message: str
    """Message is a human-readable error description"""

    type: str
    """Type indicates the error category"""


class ResponseError(BaseModel):
    error: Error
    """Error response details"""

    status: str
    """Status indicates the response status "error" """
