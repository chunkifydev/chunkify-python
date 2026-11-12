# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "Workflow",
    "Rule",
    "RuleAction",
    "RuleActionWorkflowStaticAction",
    "RuleActionWorkflowStaticActionParams",
    "RuleActionWorkflowCaptionAction",
    "RuleActionWorkflowCaptionActionTranscriptID",
    "RuleActionWorkflowTranslationAction",
    "RuleActionWorkflowTranslationActionCaptionID",
    "RuleActionWorkflowTranslationActionParams",
    "RuleActionWorkflowThumbnailAction",
    "RuleActionWorkflowThumbnailActionParams",
    "RuleActionWorkflowThumbnailActionParamsRange",
    "RuleActionWorkflowTranscriptAction",
    "RuleOrigin",
]


class RuleActionWorkflowStaticActionParams(BaseModel):
    """Params specifies the static rendition resolution."""

    resolution: Literal["highest", "240p", "360p", "480p", "540p", "720p", "1080p", "1440p", "2160p"]
    """Resolution specifies the H.264 MP4 output resolution.

    highest selects the largest supported output without upscaling. Hobby supports
    up to 1080p; other plans support up to 2160p. Streaming resolution limits do not
    apply.
    """


class RuleActionWorkflowStaticAction(BaseModel):
    """Creates or reuses one static rendition for the Asset."""

    id: str
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: RuleActionWorkflowStaticActionParams
    """Params specifies the static rendition resolution."""

    type: Literal["create_static_rendition"]
    """Type specifies the action to perform. Must be create_static_rendition."""


class RuleActionWorkflowCaptionActionTranscriptID(BaseModel):
    """TranscriptId binds caption publication to the transcript in the triggering event.

    Use it only when connected to create_transcript. When omitted, creates or reuses the Asset’s original transcript.
    """

    from_: Literal["event.output.id"] = FieldInfo(alias="from")
    """From specifies where to read the input output ID.

    Use event.output.id to consume the output in the triggering asset.output.ready
    event.
    """


class RuleActionWorkflowCaptionAction(BaseModel):
    """
    Generates or reuses original captions and their transcript from the Asset's speech.
    """

    id: str
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: object
    """Params specifies caption generation settings. Pass an empty object."""

    type: Literal["create_caption"]
    """Type specifies the action to perform. Must be create_caption."""

    transcript_id: Optional[RuleActionWorkflowCaptionActionTranscriptID] = None
    """TranscriptId binds caption publication to the transcript in the triggering
    event.

    Use it only when connected to create_transcript. When omitted, creates or reuses
    the Asset’s original transcript.
    """


class RuleActionWorkflowTranslationActionCaptionID(BaseModel):
    """
    CaptionId specifies the binding to the original caption in the triggering event.
    """

    from_: Literal["event.output.id"] = FieldInfo(alias="from")
    """From specifies where to read the input output ID.

    Use event.output.id to consume the output in the triggering asset.output.ready
    event.
    """


class RuleActionWorkflowTranslationActionParams(BaseModel):
    """Params specifies the target language."""

    language_code: Literal[
        "en", "fr", "es", "de", "it", "pt", "nl", "ja", "ko", "zh", "ar", "hi", "ru", "tr", "pl", "sv"
    ]
    """
    LanguageCode specifies the target language for the translated subtitle track,
    such as en or fr. The same code appears in the caption and HLS manifest.
    """


class RuleActionWorkflowTranslationAction(BaseModel):
    """Translates or reuses an original caption in one target language.

    Requires an asset.output.ready rule connected to an original caption creation action.
    """

    id: str
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    caption_id: RuleActionWorkflowTranslationActionCaptionID
    """
    CaptionId specifies the binding to the original caption in the triggering event.
    """

    params: RuleActionWorkflowTranslationActionParams
    """Params specifies the target language."""

    type: Literal["translate_caption"]
    """Type specifies the action to perform. Must be translate_caption."""


class RuleActionWorkflowThumbnailActionParamsRange(BaseModel):
    """Range limits sampling to part of the Source.

    Defaults to the whole Source duration.
    """

    end: Optional[float] = None
    """End specifies the exclusive upper bound in seconds.

    Defaults to the Source duration.
    """

    start: Optional[float] = None
    """Start specifies the inclusive lower bound in seconds. Defaults to zero."""


class RuleActionWorkflowThumbnailActionParams(BaseModel):
    """Params specifies sampling and image settings.

    Outputs use the Asset folder and Storage.
    """

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

    range: Optional[RuleActionWorkflowThumbnailActionParamsRange] = None
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


class RuleActionWorkflowThumbnailAction(BaseModel):
    """Creates an independent thumbnail request after asset.ready.

    Replaying this action uses its accepted request; separate actions create separate requests.
    """

    id: str
    """Id specifies a stable action key, unique within its rule."""

    params: RuleActionWorkflowThumbnailActionParams
    """Params specifies sampling and image settings.

    Outputs use the Asset folder and Storage.
    """

    type: Literal["create_thumbnails"]
    """Type specifies the action to perform. Must be create_thumbnails."""


class RuleActionWorkflowTranscriptAction(BaseModel):
    """Creates or reuses the original-language transcript.

    Can run alongside caption generation in the same asset.ready rule.
    """

    id: str
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: object
    """Params specifies transcript settings. Pass an empty object."""

    type: Literal["create_transcript"]
    """Type specifies the action to perform. Must be create_transcript."""


RuleAction: TypeAlias = Annotated[
    Union[
        RuleActionWorkflowStaticAction,
        RuleActionWorkflowCaptionAction,
        RuleActionWorkflowTranslationAction,
        RuleActionWorkflowThumbnailAction,
        RuleActionWorkflowTranscriptAction,
    ],
    PropertyInfo(discriminator="type"),
]


class RuleOrigin(BaseModel):
    """Origin specifies the action whose ready output starts this rule.

    Required for asset.output.ready; omit it for asset.ready. Translation steps must connect to a create_caption action.
    References must point to a compatible action in this definition and must not form a cycle.
    """

    action_id: str
    """
    ActionId specifies the ID of the producing action within that rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    rule_id: str
    """
    RuleId specifies the ID of the rule containing the producing action. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """


class Rule(BaseModel):
    """A starting or connected step with one or more independent actions."""

    id: str
    """
    Id specifies a stable rule key, unique within this Workflow definition. Use 1 to
    64 characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    actions: List[RuleAction]
    """Actions specifies the work to start when the rule matches.

    Actions can run concurrently; array order does not define execution order.
    Provide 1 to 32 actions per rule, with at most 32 across the definition.
    """

    event: Literal["asset.ready", "asset.output.ready"]
    """Event specifies when this rule starts.

    Use asset.ready for the single starting rule. Output ready events require an
    origin caption or static rendition action in this Workflow.
    """

    origin: Optional[RuleOrigin] = None
    """Origin specifies the action whose ready output starts this rule.

    Required for asset.output.ready; omit it for asset.ready. Translation steps must
    connect to a create_caption action. References must point to a compatible action
    in this definition and must not form a cycle.
    """


class Workflow(BaseModel):
    """A reusable definition of actions triggered by Asset events."""

    id: str
    """Unique Workflow ID."""

    archived_at: Optional[datetime] = None
    """When the Workflow was archived, or null if it is available for selection.

    Archiving stops new runs; accepted actions finish.
    """

    created_at: datetime
    """When the Workflow was created."""

    name: str
    """Name specifies the Workflow name. Use 1 to 128 characters."""

    revision: int
    """Current definition revision. Starts at 1 and increases when rules are replaced."""

    rules: List[Rule]
    """
    Rules specifies the event subscriptions and actions in this definition. Provide
    exactly one asset.ready rule and up to 15 connected rules, with at most 32
    actions and 65536 encoded bytes across all rules. Array order affects display
    only.
    """

    schema_version: int
    """SchemaVersion specifies the Workflow definition format.

    The supported version is 1.
    """

    updated_at: datetime
    """When the Workflow was last updated."""
