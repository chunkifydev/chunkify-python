# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkflowStaticParams"]


class WorkflowStaticParams(BaseModel):
    """Parameters for creating one static rendition."""

    resolution: Literal["highest", "240p", "360p", "480p", "540p", "720p", "1080p", "1440p", "2160p"]
    """Resolution specifies the H.264 MP4 output resolution.

    highest selects the largest supported output without upscaling. Hobby supports
    up to 1080p; other plans support up to 2160p. Streaming resolution limits do not
    apply.
    """
