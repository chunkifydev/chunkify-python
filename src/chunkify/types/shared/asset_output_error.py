# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AssetOutputError"]


class AssetOutputError(BaseModel):
    """A customer-facing Asset output processing failure."""

    code: str
    """Machine-readable processing error code."""

    message: str
    """Description of the processing failure."""
