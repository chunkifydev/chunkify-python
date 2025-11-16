# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .storage import Storage
from .._models import BaseModel

__all__ = ["StorageCreateResponse"]


class StorageCreateResponse(BaseModel):
    data: Optional[Storage] = None

    status: Optional[str] = None
    """Status indicates the response status "success" """
