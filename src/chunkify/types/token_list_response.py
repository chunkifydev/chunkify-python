# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .token import Token
from .shared.response_ok import ResponseOk

__all__ = ["TokenListResponse"]


class TokenListResponse(ResponseOk):
    data: Optional[List[Token]] = None  # type: ignore
