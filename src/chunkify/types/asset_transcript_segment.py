# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AssetTranscriptSegment"]


class AssetTranscriptSegment(BaseModel):
    """A timed passage of recognized speech.

    Times are seconds from the start of the Asset.
    """

    end: float
    """End specifies the passage end time in seconds."""

    start: float
    """Start specifies the passage start time in seconds."""

    text: str
    """Text contains the recognized passage, including punctuation."""
