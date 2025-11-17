# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .upload import Upload
from .shared.response_ok import ResponseOk

__all__ = ["UploadRetrieveResponse"]


class UploadRetrieveResponse(ResponseOk):
    data: Upload
