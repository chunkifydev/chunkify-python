# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .source import Source
from .._models import BaseModel

__all__ = ["SourceCreateResponse"]


class SourceCreateResponse(BaseModel):
    data: Source
    """Data contains the response object"""

    status: str
    """Status indicates the response status "success" """
