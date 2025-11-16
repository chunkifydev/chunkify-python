# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .project import Project
from .response_ok import ResponseOk

__all__ = ["ProjectListResponse"]


class ProjectListResponse(ResponseOk):
    data: Optional[List[Project]] = None  # type: ignore
