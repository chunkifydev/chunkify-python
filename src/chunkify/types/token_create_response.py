# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .token import Token
from .._models import BaseModel

__all__ = ["TokenCreateResponse"]


class TokenCreateResponse(BaseModel):
    data: Token
    """Data contains the response object"""

    status: str
    """Status indicates the response status "success" """
