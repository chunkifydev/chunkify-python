# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .source import Source
from .shared.response_ok import ResponseOk

__all__ = ["SourceRetrieveResponse"]


class SourceRetrieveResponse(ResponseOk):
    data: Source
