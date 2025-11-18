# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .storage import Storage
from .._models import BaseModel

__all__ = ["StorageCreateResponse"]


class StorageCreateResponse(BaseModel):
    data: Storage
    """Data contains the response object"""

    status: str
    """Status indicates the response status "success" """
