# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .job import Job
from .shared.response_ok import ResponseOk

__all__ = ["JobRetrieveResponse"]


class JobRetrieveResponse(ResponseOk):
    data: Job
