# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .source import Source
from .response_ok import ResponseOk

__all__ = ["SourceRetrieveResponse"]


class SourceRetrieveResponse(ResponseOk):
    data: Optional[Source] = None  # type: ignore
