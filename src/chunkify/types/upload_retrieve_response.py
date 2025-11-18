# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .upload import Upload
from .._models import BaseModel

__all__ = ["UploadRetrieveResponse"]


class UploadRetrieveResponse(BaseModel):
    data: Upload
    """Data contains the response object"""

    status: str
    """Status indicates the response status "success" """
