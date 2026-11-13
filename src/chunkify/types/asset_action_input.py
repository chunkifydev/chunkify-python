# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .workflow_thumbnail import WorkflowThumbnail

__all__ = ["AssetActionInput"]


class AssetActionInput(BaseModel):
    """Resolved action inputs. Only fields relevant to the action type are included."""

    language_code: Optional[
        Literal["en", "fr", "es", "de", "it", "pt", "nl", "ja", "ko", "zh", "ar", "hi", "ru", "tr", "pl", "sv"]
    ] = None
    """
    LanguageCode specifies the target language for the translated subtitle track,
    such as en or fr. The same code appears in the caption and HLS manifest.
    """

    resolution: Optional[Literal["highest", "240p", "360p", "480p", "540p", "720p", "1080p", "1440p", "2160p"]] = None
    """Resolution specifies the H.264 MP4 output resolution.

    highest selects the largest supported output without upscaling. Hobby supports
    up to 1080p; other plans support up to 2160p. Streaming resolution limits do not
    apply.
    """

    source_caption_id: Optional[str] = None
    """ID of the original caption to translate. Included only for translation actions."""

    thumbnails: Optional[WorkflowThumbnail] = None
    """Thumbnail settings. Included only for create_thumbnails actions."""

    transcript_id: Optional[str] = None
    """TranscriptId specifies the original transcript consumed by caption publication.

    Omitted for actions without a transcript input.
    """
