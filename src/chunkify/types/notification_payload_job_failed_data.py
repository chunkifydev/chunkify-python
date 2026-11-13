# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .job import Job
from .._models import BaseModel

__all__ = ["NotificationPayloadJobFailedData"]


class NotificationPayloadJobFailedData(BaseModel):
    """Payload data structure for job.failed and job.cancelled events"""

    job: Job
