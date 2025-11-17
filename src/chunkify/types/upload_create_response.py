# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .upload import Upload
from .shared.response_ok import ResponseOk

__all__ = ["UploadCreateResponse"]


class UploadCreateResponse(ResponseOk):
    data: Optional[Upload] = None
