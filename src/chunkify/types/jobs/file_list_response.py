# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..api_file import APIFile
from ..shared.response_ok import ResponseOk

__all__ = ["FileListResponse"]


class FileListResponse(ResponseOk):
    data: Optional[List[APIFile]] = None
