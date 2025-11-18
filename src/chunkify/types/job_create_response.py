# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .job import Job
from .._models import BaseModel

__all__ = ["JobCreateResponse"]


class JobCreateResponse(BaseModel):
    data: Job
    """Data contains the response object"""

    status: str
    """Status indicates the response status "success" """
