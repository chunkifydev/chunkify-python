# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AssetError"]


class AssetError(BaseModel):
    code: str
    """Machine-readable processing error code."""

    message: str
    """Description of the processing failure."""

    stage: Literal["ingest", "analysis", "encoding", "packaging", "upload", "validation", "cleanup"]
    """Processing stage that failed."""
