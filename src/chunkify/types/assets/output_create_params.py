# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "OutputCreateParams",
    "Output",
    "OutputAssetCaptionOutputCreateParams",
    "OutputAssetCaptionOutputCreateParamsParams",
    "OutputAssetStaticRenditionOutputCreateParams",
    "OutputAssetStaticRenditionOutputCreateParamsParams",
    "OutputAssetThumbnailOutputCreateParams",
    "OutputAssetThumbnailOutputCreateParamsParams",
    "OutputAssetThumbnailOutputCreateParamsParamsRange",
    "OutputAssetTranscriptOutputCreateParams",
]


class OutputCreateParams(TypedDict, total=False):
    output: Required[Output]
    """Create one output for an Asset.

    Type selects its required, strictly validated parameters.
    """


class OutputAssetCaptionOutputCreateParamsParams(TypedDict, total=False):
    """Params specifies the settings for this output type."""

    language_code: Literal[
        "en", "fr", "es", "de", "it", "pt", "nl", "ja", "ko", "zh", "ar", "hi", "ru", "tr", "pl", "sv"
    ]
    """LanguageCode specifies the target language for a translated caption.

    Supply source_caption_id with this field. Omit both fields to transcribe the
    Asset audio with automatic language detection.
    """

    source_caption_id: str
    """SourceCaptionId specifies the caption on this Asset to translate.

    Supply language_code with this field. Omit both fields to generate original
    captions.
    """


class OutputAssetCaptionOutputCreateParams(TypedDict, total=False):
    """Create an Asset-owned caption output."""

    params: Required[OutputAssetCaptionOutputCreateParamsParams]
    """Params specifies the settings for this output type."""

    type: Required[Literal["caption"]]
    """Type specifies the output kind to create."""


class OutputAssetStaticRenditionOutputCreateParamsParams(TypedDict, total=False):
    """Params specifies the settings for this output type."""

    resolution: Required[Literal["highest", "240p", "360p", "480p", "540p", "720p", "1080p", "1440p", "2160p"]]
    """H.264 MP4 resolution.

    highest selects the largest supported output without upscaling. Hobby supports
    up to 1080p; other plans support up to 2160p. Independent of the streaming
    resolution limits.
    """


class OutputAssetStaticRenditionOutputCreateParams(TypedDict, total=False):
    """Create an Asset-owned static rendition output."""

    params: Required[OutputAssetStaticRenditionOutputCreateParamsParams]
    """Params specifies the settings for this output type."""

    type: Required[Literal["static_rendition"]]
    """Type specifies the output kind to create."""


class OutputAssetThumbnailOutputCreateParamsParamsRange(TypedDict, total=False):
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    end: float
    """End specifies the exclusive upper bound in seconds.

    Defaults to the Source duration.
    """

    start: float
    """Start specifies the inclusive lower bound in seconds. Defaults to zero."""


class OutputAssetThumbnailOutputCreateParamsParams(TypedDict, total=False):
    """Params specifies the settings for this output type."""

    count: int
    """
    Count specifies 1 to 100 thumbnails at the middle of equal sections of the
    selected range.
    """

    format: Literal["jpeg", "webp"]
    """Format selects JPEG or WebP. Defaults to JPEG."""

    metadata: Dict[str, str]
    """Metadata attaches string values to this request.

    The serialized object may contain at most 2048 bytes.
    """

    output: Literal["images", "sprites"]
    """Output selects images or sprites. Defaults to images."""

    range: OutputAssetThumbnailOutputCreateParamsParamsRange
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    size: int
    """Size specifies the maximum image or tile edge in pixels, from 64 to 1920.

    Defaults to 320. Odd sizes are supported. Preserves display aspect ratio without
    cropping or upscaling.
    """

    timestamps: Iterable[float]
    """Timestamps specifies 1 to 100 Source-relative target times in seconds.

    Every timestamp must be within the selected range, including its start and
    excluding its end. Repeated targets produce separate outputs.
    """


class OutputAssetThumbnailOutputCreateParams(TypedDict, total=False):
    """Create an Asset-owned thumbnail output."""

    params: Required[OutputAssetThumbnailOutputCreateParamsParams]
    """Params specifies the settings for this output type."""

    type: Required[Literal["thumbnail"]]
    """Type specifies the output kind to create."""


class OutputAssetTranscriptOutputCreateParams(TypedDict, total=False):
    """Create or reuse the original-language transcript for an Asset.

    Caption generation shares this transcript and its speech-recognition charge.
    """

    params: Required[object]
    """Parameters for an original-language transcript.

    Pass an empty object; the spoken language is detected automatically.
    """

    type: Required[Literal["transcript"]]
    """Type specifies the output kind."""


Output: TypeAlias = Union[
    OutputAssetCaptionOutputCreateParams,
    OutputAssetStaticRenditionOutputCreateParams,
    OutputAssetThumbnailOutputCreateParams,
    OutputAssetTranscriptOutputCreateParams,
]
