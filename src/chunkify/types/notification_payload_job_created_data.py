# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .job import Job
from .._models import BaseModel

__all__ = ["NotificationPayloadJobCreatedData"]


class NotificationPayloadJobCreatedData(BaseModel):
    """Payload for job.created.

    A standalone Job has been accepted for processing; execution may not have started.
    """

    job: Job
