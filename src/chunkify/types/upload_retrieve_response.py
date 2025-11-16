# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .upload import Upload
from .response_ok import ResponseOk

__all__ = ["UploadRetrieveResponse"]


class UploadRetrieveResponse(ResponseOk):
    data: Optional[Upload] = None  # type: ignore
