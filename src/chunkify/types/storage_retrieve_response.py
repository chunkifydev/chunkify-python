# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .storage import Storage
from .shared.response_ok import ResponseOk

__all__ = ["StorageRetrieveResponse"]


class StorageRetrieveResponse(ResponseOk):
    data: Storage
