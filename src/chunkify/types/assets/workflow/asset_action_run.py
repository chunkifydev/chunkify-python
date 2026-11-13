# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AssetActionRun", "Input", "InputThumbnails", "InputThumbnailsRange", "Result"]


class InputThumbnailsRange(BaseModel):
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    end: Optional[float] = None
    """End specifies the exclusive upper bound in seconds.

    Defaults to the Source duration.
    """

    start: Optional[float] = None
    """Start specifies the inclusive lower bound in seconds. Defaults to zero."""


class InputThumbnails(BaseModel):
    """Thumbnail settings. Included only for create_thumbnails actions."""

    count: Optional[int] = None
    """
    Count specifies 1 to 100 thumbnails at the middle of equal sections of the
    selected range.
    """

    format: Optional[Literal["jpeg", "webp"]] = None
    """Format selects JPEG or WebP. Defaults to JPEG."""

    metadata: Optional[Dict[str, str]] = None
    """Metadata attaches string values to this request.

    The serialized object may contain at most 2048 bytes.
    """

    output: Optional[Literal["images", "sprites"]] = None
    """Output selects images or sprites. Defaults to images."""

    range: Optional[InputThumbnailsRange] = None
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    size: Optional[int] = None
    """Size specifies the maximum image or tile edge in pixels, from 64 to 1920.

    Defaults to 320. Odd sizes are supported. Preserves display aspect ratio without
    cropping or upscaling.
    """

    timestamps: Optional[List[float]] = None
    """Timestamps specifies 1 to 100 Source-relative target times in seconds.

    Times outside the selected range are skipped when the action runs. If none
    remain, the action is skipped without a charge. Repeated targets produce
    separate outputs.
    """


class Input(BaseModel):
    """Resolved parameters and input references for this execution."""

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

    thumbnails: Optional[InputThumbnails] = None
    """Thumbnail settings. Included only for create_thumbnails actions."""

    transcript_id: Optional[str] = None
    """TranscriptId specifies the original transcript consumed by caption publication.

    Omitted for actions without a transcript input.
    """


class Result(BaseModel):
    """Output reference and reuse flag.

    Included when the action completes successfully.
    """

    output_id: str
    """
    ID of the caption, static rendition, or thumbnail request produced by the
    action.
    """

    output_type: Literal["caption", "static_rendition", "thumbnail", "transcript"]
    """Type of output referenced by output_id.

    Caption generation and translation both produce caption outputs.
    """

    reused: bool
    """Whether the action reused an existing output instead of creating one."""


class AssetActionRun(BaseModel):
    """
    One execution of an Asset action, started by a Workflow or a direct output request.
    """

    id: str
    """Unique action execution ID, prefixed with acr\\__."""

    asset_id: str
    """ID of the Asset processed by this action."""

    completed_at: Optional[datetime] = None
    """When the action completed, failed, was skipped, or was cancelled.

    Null while work remains.
    """

    created_at: datetime
    """When the action was accepted."""

    input: Input
    """Resolved parameters and input references for this execution."""

    status: Literal["pending", "running", "waiting", "completed", "failed", "skipped", "cancelled"]
    """Current execution status of the action."""

    type: Literal[
        "create_static_rendition", "create_caption", "create_transcript", "translate_caption", "create_thumbnails"
    ]
    """Type of action performed."""

    updated_at: datetime
    """When the action was last updated."""

    workflow_run_id: Optional[str] = None
    """ID of the Workflow run that started the action.

    Null for direct output requests.
    """

    action_id: Optional[str] = None
    """Action key within the rule. Omitted for direct output requests."""

    error: Optional[str] = None
    """Reason the action failed. Omitted when no failure message is available."""

    reason: Optional[str] = None
    """Machine-readable reason for waiting, skipping, failure, or cancellation.

    Omitted when no reason applies.
    """

    result: Optional[Result] = None
    """Output reference and reuse flag.

    Included when the action completes successfully.
    """

    rule_id: Optional[str] = None
    """Rule key from the Workflow definition. Omitted for direct output requests."""
