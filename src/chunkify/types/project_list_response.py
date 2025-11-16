# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ProjectListResponse"]


class ProjectListResponse(BaseModel):
    data: Optional[object] = None

    status: Optional[str] = None
    """Status indicates the response status "success" """
