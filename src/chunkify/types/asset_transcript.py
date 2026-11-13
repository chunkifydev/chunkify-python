# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .asset_output_status import AssetOutputStatus
from .asset_transcript_content import AssetTranscriptContent
from .shared.asset_output_error import AssetOutputError

__all__ = ["AssetTranscript"]


class AssetTranscript(BaseModel):
    """An original-language transcript.

    Content is included in ready output responses and lifecycle event snapshots. Transcripts have no download or CDN URL.
    """

    id: str
    """Id identifies the Asset output, prefixed with aop\\__."""

    status: AssetOutputStatus
    """Status specifies the output processing state.

    Expired means temporary output files are no longer available.
    """

    content: Optional[AssetTranscriptContent] = None
    """Content contains the complete text and timed segments.

    Included when ready; omitted while preparing, failed or expired.
    """

    error: Optional[AssetOutputError] = None
    """A customer-facing Asset output processing failure."""

    language_code: Optional[str] = None
    """LanguageCode identifies the detected primary language, such as en.

    Omitted before recognition or when no speech is detected.
    """
