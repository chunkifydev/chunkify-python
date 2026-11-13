# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.transcoder_status import TranscoderStatus

__all__ = ["TranscoderListResponse"]


class TranscoderListResponse(BaseModel):
    """Response containing a list of transcoders for a job"""

    data: List[TranscoderStatus]

    status: Literal["success"]
    """Status indicates the response status "success" """
