# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .project import Project
from .shared.response_ok import ResponseOk

__all__ = ["ProjectRetrieveResponse"]


class ProjectRetrieveResponse(ResponseOk):
    data: Project
