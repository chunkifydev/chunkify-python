# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ChunkifyError"]


class ChunkifyError(BaseModel):
    detail: Optional[str] = None
    """Additional error details or output"""

    message: Optional[str] = None
    """Main error message"""

    type: Optional[str] = None
    """Type of error (e.g., "ffmpeg", "network", "storage", etc.)"""
