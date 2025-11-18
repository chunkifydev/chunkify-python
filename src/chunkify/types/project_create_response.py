# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .project import Project
from .._models import BaseModel

__all__ = ["ProjectCreateResponse"]


class ProjectCreateResponse(BaseModel):
    data: Project
    """Data contains the response object"""

    status: str
    """Status indicates the response status "success" """
