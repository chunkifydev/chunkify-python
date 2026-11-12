# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..asset_static_rendition_create_params import AssetStaticRenditionCreateParams

__all__ = [
    "OutputCreateParams",
    "AssetCaptionOutputCreateParams",
    "AssetCaptionOutputCreateParamsParams",
    "AssetStaticRenditionOutputCreateParams",
    "AssetThumbnailOutputCreateParams",
    "AssetThumbnailOutputCreateParamsParams",
    "AssetThumbnailOutputCreateParamsParamsRange",
    "AssetTranscriptOutputCreateParams",
]


class AssetCaptionOutputCreateParams(TypedDict, total=False):
    params: Required[AssetCaptionOutputCreateParamsParams]
    """Params specifies the settings for this output type."""

    type: Required[Literal["caption"]]
    """Type specifies the output kind to create."""


class AssetCaptionOutputCreateParamsParams(TypedDict, total=False):
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


class AssetStaticRenditionOutputCreateParams(TypedDict, total=False):
    params: Required[AssetStaticRenditionCreateParams]
    """Params specifies the settings for this output type."""

    type: Required[Literal["static_rendition"]]
    """Type specifies the output kind to create."""


class AssetThumbnailOutputCreateParams(TypedDict, total=False):
    params: Required[AssetThumbnailOutputCreateParamsParams]
    """Params specifies the settings for this output type."""

    type: Required[Literal["thumbnail"]]
    """Type specifies the output kind to create."""


class AssetThumbnailOutputCreateParamsParamsRange(TypedDict, total=False):
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    end: float
    """End specifies the exclusive upper bound in seconds.

    Defaults to the Source duration.
    """

    start: float
    """Start specifies the inclusive lower bound in seconds. Defaults to zero."""


class AssetThumbnailOutputCreateParamsParams(TypedDict, total=False):
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

    range: AssetThumbnailOutputCreateParamsParamsRange
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


class AssetTranscriptOutputCreateParams(TypedDict, total=False):
    params: Required[object]
    """Parameters for an original-language transcript.

    Pass an empty object; the spoken language is detected automatically.
    """

    type: Required[Literal["transcript"]]
    """Type specifies the output kind."""


OutputCreateParams: TypeAlias = Union[
    AssetCaptionOutputCreateParams,
    AssetStaticRenditionOutputCreateParams,
    AssetThumbnailOutputCreateParams,
    AssetTranscriptOutputCreateParams,
]
