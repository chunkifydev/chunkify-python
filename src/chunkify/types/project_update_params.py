# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

from .asset_defaults_params import AssetDefaultsParams

__all__ = ["ProjectUpdateParams", "PlayerAppearance", "PlayerAppearanceDark", "PlayerAppearanceLight"]


class ProjectUpdateParams(TypedDict, total=False):
    asset_defaults: AssetDefaultsParams
    """Defaults for new Assets and automatic Uploads.

    Replaces the whole object. Omitted fields reset to their defaults. Existing
    Assets are unchanged.
    """

    default_workflow_id: Optional[str]
    """DefaultWorkflowId specifies the default Workflow for new Assets.

    Set null to clear it.
    """

    name: str
    """Project name."""

    player_appearance: PlayerAppearance
    """Player colours and controls for Chunkify-hosted playback pages, such as embeds.

    Replaces the whole object. Omitted fields reset to their defaults. Existing
    embeds use the new values.
    """

    storage_id: str
    """ID of this Project's default Storage."""


class PlayerAppearanceDark(TypedDict, total=False):
    """Dark specifies the player colours in dark mode.

    Omit to use the default dark colours.
    """

    accent: Required[str]
    """Accent specifies the colour of progress and active controls, as #rrggbb."""

    primary: Required[str]
    """Primary specifies the colour of text and control icons, as #rrggbb."""

    secondary: Required[str]
    """Secondary specifies the colour of player buttons, as #rrggbb."""


class PlayerAppearanceLight(TypedDict, total=False):
    """Light specifies the player colours in light mode.

    Omit to use the default light colours.
    """

    accent: Required[str]
    """Accent specifies the colour of progress and active controls, as #rrggbb."""

    primary: Required[str]
    """Primary specifies the colour of text and control icons, as #rrggbb."""

    secondary: Required[str]
    """Secondary specifies the colour of player buttons, as #rrggbb."""


class PlayerAppearance(TypedDict, total=False):
    """Player colours and controls for Chunkify-hosted playback pages, such as embeds.

    Replaces the whole object. Omitted fields reset to their defaults. Existing embeds use the new values.
    """

    dark: PlayerAppearanceDark
    """Dark specifies the player colours in dark mode.

    Omit to use the default dark colours.
    """

    hidden_controls: List[Literal["captions", "settings", "pip", "fullscreen", "cast", "airplay", "mute"]]
    """HiddenControls lists the player buttons to hide.

    Defaults to an empty list. Other buttons appear when the browser and video
    support them.
    """

    light: PlayerAppearanceLight
    """Light specifies the player colours in light mode.

    Omit to use the default light colours.
    """

    mode: Literal["auto", "light", "dark"]
    """Mode specifies which palette the player uses.

    auto follows the viewer's system setting. An embed can override it with its
    theme URL parameter. Defaults to auto.
    """
