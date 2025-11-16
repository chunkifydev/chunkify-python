# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .api_file import APIFile
from .shared.response_ok import ResponseOk

__all__ = ["FileRetrieveResponse"]


class FileRetrieveResponse(ResponseOk):
    data: Optional[APIFile] = None  # type: ignore
