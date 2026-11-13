# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .shared.instance_type import InstanceType

__all__ = ["JobTranscoder"]


class JobTranscoder(BaseModel):
    """The transcoder configuration for a job"""

    auto: bool
    """Whether the transcoder configuration is automatically set by Chunkify"""

    quantity: int
    """Number of instances allocated"""

    type: InstanceType
    """Type of transcoder instance"""
