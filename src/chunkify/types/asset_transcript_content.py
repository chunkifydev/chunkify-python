# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .asset_transcript_segment import AssetTranscriptSegment

__all__ = ["AssetTranscriptContent"]


class AssetTranscriptContent(BaseModel):
    """The complete transcript and its timed passages.

    An audio track without speech produces empty text and an empty segments array.
    """

    segments: List[AssetTranscriptSegment]
    """Segments contains timed passages in chronological order.

    Individual word timestamps are not included.
    """

    text: str
    """Text contains the complete recognized speech in the original language."""
