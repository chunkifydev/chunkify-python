# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .file import File
from .response_ok import ResponseOk

__all__ = ["JobGetFilesResponse"]


class JobGetFilesResponse(ResponseOk):
    data: Optional[List[File]] = None  # type: ignore
