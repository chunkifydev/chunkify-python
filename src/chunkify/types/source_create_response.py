# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .source import Source
from .._models import BaseModel

__all__ = ["SourceCreateResponse"]


class SourceCreateResponse(BaseModel):
    data: Optional[Source] = None

    status: Optional[str] = None
    """Status indicates the response status "success" """
