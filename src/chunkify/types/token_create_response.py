# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .token import Token
from .._models import BaseModel

__all__ = ["TokenCreateResponse"]


class TokenCreateResponse(BaseModel):
    data: Optional[Token] = None

    status: Optional[str] = None
    """Status indicates the response status "success" """
