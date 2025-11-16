# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .storage import Storage
from .shared.response_ok import ResponseOk

__all__ = ["StorageListResponse"]


class StorageListResponse(ResponseOk):
    data: Optional[List[Storage]] = None  # type: ignore
