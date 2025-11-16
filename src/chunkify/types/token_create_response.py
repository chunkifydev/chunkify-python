# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .token import Token
from .shared.response_ok import ResponseOk

__all__ = ["TokenCreateResponse"]


class TokenCreateResponse(ResponseOk):
    data: Optional[Token] = None  # type: ignore
