# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ResponseOk"]


class ResponseOk(BaseModel):
    status: str
    """Status indicates the response status "success" """
