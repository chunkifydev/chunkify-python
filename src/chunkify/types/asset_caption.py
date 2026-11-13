# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.asset_output_error import AssetOutputError

__all__ = ["AssetCaption"]


class AssetCaption(BaseModel):
    id: str
    """Unique Asset output ID, prefixed with aop\\__."""

    status: Literal["preparing", "ready", "failed", "expired"]
    """Caption processing status."""

    created_at: Optional[datetime] = None
    """Time this caption output was requested."""

    error: Optional[AssetOutputError] = None
    """Reason caption processing failed."""

    language_code: Optional[str] = None
    """Primary language of this subtitle track, such as en or fr.

    Omitted when no speech was detected or processing has not finished.
    """

    playlist_path: Optional[str] = None
    """Subtitle media playlist path in Storage. Available when speech was detected."""

    size: Optional[int] = None
    """Combined subtitle playlist and WebVTT size in bytes. Available when ready."""

    source_caption_id: Optional[str] = None
    """ID of the caption track translated to create this track.

    Omitted for speech transcription.
    """

    transcript_id: Optional[str] = None
    """
    TranscriptId identifies the original-language transcript used to generate this
    caption. Omitted for translated captions.
    """

    vtt_path: Optional[str] = None
    """WebVTT subtitle segment path in Storage. Available when speech was detected."""
