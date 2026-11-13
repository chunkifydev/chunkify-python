# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .workflow_static_resolution import WorkflowStaticResolution

__all__ = ["WorkflowStatic"]


class WorkflowStatic(BaseModel):
    """Parameters for creating one static rendition."""

    resolution: WorkflowStaticResolution
    """Resolution specifies the H.264 MP4 output resolution.

    highest selects the largest supported output without upscaling. Hobby supports
    up to 1080p; other plans support up to 2160p. Streaming resolution limits do not
    apply.
    """
