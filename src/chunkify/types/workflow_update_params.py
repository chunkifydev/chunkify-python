# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "WorkflowUpdateParams",
    "Rule",
    "RuleAction",
    "RuleActionWorkflowStaticActionParams",
    "RuleActionWorkflowStaticActionParamsParams",
    "RuleActionWorkflowCaptionActionParams",
    "RuleActionWorkflowCaptionActionParamsParams",
    "RuleActionWorkflowCaptionActionParamsTranscriptID",
    "RuleActionWorkflowTranslationActionParams",
    "RuleActionWorkflowTranslationActionParamsCaptionID",
    "RuleActionWorkflowTranslationActionParamsParams",
    "RuleActionWorkflowThumbnailActionParams",
    "RuleActionWorkflowThumbnailActionParamsParams",
    "RuleActionWorkflowThumbnailActionParamsParamsRange",
    "RuleActionWorkflowTranscriptActionParams",
    "RuleActionWorkflowTranscriptActionParamsParams",
    "RuleOrigin",
]


class WorkflowUpdateParams(TypedDict, total=False):
    expected_revision: int
    """ExpectedRevision specifies the current Workflow revision when replacing rules.

    The update returns a conflict if it no longer matches. Required when rules is
    provided. Must be at least 1.
    """

    name: str
    """Name specifies the Workflow name. Use 1 to 128 characters."""

    rules: Iterable[Rule]
    """
    Rules specifies the event subscriptions and actions in this definition. Provide
    exactly one asset.ready rule and up to 15 connected rules, with at most 32
    actions and 65536 encoded bytes across all rules. Array order affects display
    only. Replaces the complete definition and requires schema_version and
    expected_revision. Existing Assets and Uploads keep their pinned revision.
    """

    schema_version: Literal[1]
    """SchemaVersion specifies the Workflow definition format.

    The supported version is 1. Required when rules is provided.
    """


class RuleActionWorkflowStaticActionParamsParams(TypedDict, total=False):
    """Params specifies the static rendition resolution."""

    resolution: Required[Literal["highest", "240p", "360p", "480p", "540p", "720p", "1080p", "1440p", "2160p"]]
    """Resolution specifies the H.264 MP4 output resolution.

    highest selects the largest supported output without upscaling. Hobby supports
    up to 1080p; other plans support up to 2160p. Streaming resolution limits do not
    apply.
    """


class RuleActionWorkflowStaticActionParams(TypedDict, total=False):
    """Creates or reuses one static rendition for the Asset."""

    id: Required[str]
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: Required[RuleActionWorkflowStaticActionParamsParams]
    """Params specifies the static rendition resolution."""

    type: Required[Literal["create_static_rendition"]]
    """Type specifies the action to perform. Must be create_static_rendition."""


class RuleActionWorkflowCaptionActionParamsParams(TypedDict, total=False):
    """Params specifies caption generation settings. Pass an empty object."""

    pass


_RuleActionWorkflowCaptionActionParamsTranscriptIDReservedKeywords = TypedDict(
    "_RuleActionWorkflowCaptionActionParamsTranscriptIDReservedKeywords",
    {
        "from": Literal["event.output.id"],
    },
    total=False,
)


class RuleActionWorkflowCaptionActionParamsTranscriptID(
    _RuleActionWorkflowCaptionActionParamsTranscriptIDReservedKeywords, total=False
):
    """TranscriptId binds caption publication to the transcript in the triggering event.

    Use it only when connected to create_transcript. When omitted, creates or reuses the Asset’s original transcript.
    """

    pass


class RuleActionWorkflowCaptionActionParams(TypedDict, total=False):
    """
    Generates or reuses original captions and their transcript from the Asset's speech.
    """

    id: Required[str]
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: Required[RuleActionWorkflowCaptionActionParamsParams]
    """Params specifies caption generation settings. Pass an empty object."""

    type: Required[Literal["create_caption"]]
    """Type specifies the action to perform. Must be create_caption."""

    transcript_id: RuleActionWorkflowCaptionActionParamsTranscriptID
    """TranscriptId binds caption publication to the transcript in the triggering
    event.

    Use it only when connected to create_transcript. When omitted, creates or reuses
    the Asset’s original transcript.
    """


_RuleActionWorkflowTranslationActionParamsCaptionIDReservedKeywords = TypedDict(
    "_RuleActionWorkflowTranslationActionParamsCaptionIDReservedKeywords",
    {
        "from": Literal["event.output.id"],
    },
    total=False,
)


class RuleActionWorkflowTranslationActionParamsCaptionID(
    _RuleActionWorkflowTranslationActionParamsCaptionIDReservedKeywords, total=False
):
    """
    CaptionId specifies the binding to the original caption in the triggering event.
    """

    pass


class RuleActionWorkflowTranslationActionParamsParams(TypedDict, total=False):
    """Params specifies the target language."""

    language_code: Required[
        Literal["en", "fr", "es", "de", "it", "pt", "nl", "ja", "ko", "zh", "ar", "hi", "ru", "tr", "pl", "sv"]
    ]
    """
    LanguageCode specifies the target language for the translated subtitle track,
    such as en or fr. The same code appears in the caption and HLS manifest.
    """


class RuleActionWorkflowTranslationActionParams(TypedDict, total=False):
    """Translates or reuses an original caption in one target language.

    Requires an asset.output.ready rule connected to an original caption creation action.
    """

    id: Required[str]
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    caption_id: Required[RuleActionWorkflowTranslationActionParamsCaptionID]
    """
    CaptionId specifies the binding to the original caption in the triggering event.
    """

    params: Required[RuleActionWorkflowTranslationActionParamsParams]
    """Params specifies the target language."""

    type: Required[Literal["translate_caption"]]
    """Type specifies the action to perform. Must be translate_caption."""


class RuleActionWorkflowThumbnailActionParamsParamsRange(TypedDict, total=False):
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    end: float
    """End specifies the exclusive upper bound in seconds.

    Defaults to the Source duration.
    """

    start: float
    """Start specifies the inclusive lower bound in seconds. Defaults to zero."""


class RuleActionWorkflowThumbnailActionParamsParams(TypedDict, total=False):
    """Params specifies sampling and image settings.

    Outputs use the Asset folder and Storage.
    """

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

    range: RuleActionWorkflowThumbnailActionParamsParamsRange
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

    Times outside the selected range are skipped when the action runs. If none
    remain, the action is skipped without a charge. Repeated targets produce
    separate outputs.
    """


class RuleActionWorkflowThumbnailActionParams(TypedDict, total=False):
    """Creates an independent thumbnail request after asset.ready.

    Replaying this action uses its accepted request; separate actions create separate requests.
    """

    id: Required[str]
    """Id specifies a stable action key, unique within its rule."""

    params: Required[RuleActionWorkflowThumbnailActionParamsParams]
    """Params specifies sampling and image settings.

    Outputs use the Asset folder and Storage.
    """

    type: Required[Literal["create_thumbnails"]]
    """Type specifies the action to perform. Must be create_thumbnails."""


class RuleActionWorkflowTranscriptActionParamsParams(TypedDict, total=False):
    """Params specifies transcript settings. Pass an empty object."""

    pass


class RuleActionWorkflowTranscriptActionParams(TypedDict, total=False):
    """Creates or reuses the original-language transcript.

    Can run alongside caption generation in the same asset.ready rule.
    """

    id: Required[str]
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: Required[RuleActionWorkflowTranscriptActionParamsParams]
    """Params specifies transcript settings. Pass an empty object."""

    type: Required[Literal["create_transcript"]]
    """Type specifies the action to perform. Must be create_transcript."""


RuleAction: TypeAlias = Union[
    RuleActionWorkflowStaticActionParams,
    RuleActionWorkflowCaptionActionParams,
    RuleActionWorkflowTranslationActionParams,
    RuleActionWorkflowThumbnailActionParams,
    RuleActionWorkflowTranscriptActionParams,
]


class RuleOrigin(TypedDict, total=False):
    """Origin specifies the action whose ready output starts this rule.

    Required for asset.output.ready; omit it for asset.ready. Translation steps must connect to a create_caption action.
    References must point to a compatible action in this definition and must not form a cycle.
    """

    action_id: Required[str]
    """
    ActionId specifies the ID of the producing action within that rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    rule_id: Required[str]
    """
    RuleId specifies the ID of the rule containing the producing action. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """


class Rule(TypedDict, total=False):
    """A starting or connected step with one or more independent actions."""

    id: Required[str]
    """
    Id specifies a stable rule key, unique within this Workflow definition. Use 1 to
    64 characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    actions: Required[Iterable[RuleAction]]
    """Actions specifies the work to start when the rule matches.

    Actions can run concurrently; array order does not define execution order.
    Provide 1 to 32 actions per rule, with at most 32 across the definition.
    """

    event: Required[Literal["asset.ready", "asset.output.ready"]]
    """Event specifies when this rule starts.

    Use asset.ready for the single starting rule. Output ready events require an
    origin caption or static rendition action in this Workflow.
    """

    origin: RuleOrigin
    """Origin specifies the action whose ready output starts this rule.

    Required for asset.output.ready; omit it for asset.ready. Translation steps must
    connect to a create_caption action. References must point to a compatible action
    in this definition and must not form a cycle.
    """
