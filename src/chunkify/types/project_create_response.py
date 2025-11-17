# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .project import Project
from .shared.response_ok import ResponseOk

__all__ = ["ProjectCreateResponse"]


class ProjectCreateResponse(ResponseOk):
    data: Optional[Project] = None
