# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .project import Project
from .._models import BaseModel

__all__ = ["ProjectCreateResponse"]


class ProjectCreateResponse(BaseModel):
    data: Optional[Project] = None

    status: Optional[str] = None
    """Status indicates the response status "success" """
