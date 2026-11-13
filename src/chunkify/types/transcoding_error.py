# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .transcoding_processing_stage import TranscodingProcessingStage

__all__ = ["TranscodingError"]


class TranscodingError(BaseModel):
    """A customer-facing Transcoding processing failure."""

    code: str
    """Code identifies the processing failure."""

    message: str
    """Message describes the failure without internal worker or provider diagnostics."""

    stage: TranscodingProcessingStage
    """Stage identifies where processing failed."""
