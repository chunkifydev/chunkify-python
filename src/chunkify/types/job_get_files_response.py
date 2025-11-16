# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .api_file import APIFile
from .response_ok import ResponseOk

__all__ = ["JobGetFilesResponse"]


class JobGetFilesResponse(ResponseOk):
    data: Optional[List[APIFile]] = None  # type: ignore
