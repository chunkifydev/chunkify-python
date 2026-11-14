# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AssetRenditionProgress"]


class AssetRenditionProgress(BaseModel):
    """Current rendition preparation progress.

    Encoding progress measures processed video duration, not elapsed time or playback availability.
    """

    stage: Literal["queued", "starting", "encoding", "finalizing", "uploading"]
    """Stage specifies the current preparation activity.

    Finalization and streaming publication can overlap encoding; finalizing is shown
    once encoding has completed.
    """

    percent: Optional[float] = None
    """Percent specifies the percentage of the video encoded so far.

    Present only during encoding when video duration is known. It may decrease if
    processing restarts. It does not estimate total preparation time.
    """
