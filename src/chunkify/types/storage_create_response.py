# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .storage import Storage
from .shared.response_ok import ResponseOk

__all__ = ["StorageCreateResponse"]


class StorageCreateResponse(ResponseOk):
    data: Optional[Storage] = None  # type: ignore
