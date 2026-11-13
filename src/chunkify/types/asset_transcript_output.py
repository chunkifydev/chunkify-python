# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .asset_transcript import AssetTranscript
from .asset_output_status import AssetOutputStatus

__all__ = ["AssetTranscriptOutput"]


class AssetTranscriptOutput(BaseModel):
    """An Asset-owned transcript output and its content."""

    id: str
    """Id identifies the Asset output, prefixed with aop\\__."""

    asset_id: str
    """AssetId identifies the owning Asset."""

    details: AssetTranscript
    """An original-language transcript.

    Content is included in ready output responses and lifecycle event snapshots.
    Transcripts have no download or CDN URL.
    """

    status: AssetOutputStatus
    """Status specifies the output processing state.

    Expired means temporary output files are no longer available.
    """

    type: Literal["transcript"]
    """Type identifies the output kind."""
