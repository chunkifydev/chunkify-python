# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .file import File
from .response_ok import ResponseOk

__all__ = ["FileRetrieveResponse"]


class FileRetrieveResponse(ResponseOk):
    data: Optional[File] = None  # type: ignore
