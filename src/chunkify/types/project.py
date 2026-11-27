# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .asset_defaults import AssetDefaults

__all__ = ["Project", "PlayerAppearance", "PlayerAppearanceDark", "PlayerAppearanceLight"]


class PlayerAppearanceDark(BaseModel):
    """Dark specifies the player colours in dark mode."""

    accent: str
    """Accent specifies the colour of progress and active controls."""

    primary: str
    """Primary specifies the colour of text and control icons."""

    secondary: str
    """Secondary specifies the colour of player buttons."""


class PlayerAppearanceLight(BaseModel):
    """Light specifies the player colours in light mode."""

    accent: str
    """Accent specifies the colour of progress and active controls."""

    primary: str
    """Primary specifies the colour of text and control icons."""

    secondary: str
    """Secondary specifies the colour of player buttons."""


class PlayerAppearance(BaseModel):
    """
    Player colours and controls used by Chunkify-hosted playback pages, such as embeds.
    """

    dark: PlayerAppearanceDark
    """Dark specifies the player colours in dark mode."""

    hidden_controls: List[Literal["captions", "settings", "pip", "fullscreen", "cast", "airplay", "mute"]]
    """
    HiddenControls lists the player buttons to hide. Other buttons appear when the
    browser and video support them.
    """

    light: PlayerAppearanceLight
    """Light specifies the player colours in light mode."""

    mode: Literal["auto", "light", "dark"]
    """Mode specifies which palette the player uses.

    auto follows the viewer's system setting.
    """


class Project(BaseModel):
    id: str
    """Id is the unique identifier for the project."""

    asset_defaults: AssetDefaults
    """Defaults for new Assets, including Assets created from Uploads."""

    created_at: datetime
    """Timestamp when the project was created"""

    name: str
    """Name of the project"""

    player_appearance: PlayerAppearance
    """
    Player colours and controls used by Chunkify-hosted playback pages, such as
    embeds.
    """

    slug: str
    """Slug is the slug for the project."""

    storage_id: str
    """StorageId identifier where project files are stored"""

    default_workflow_id: Optional[str] = None
    """DefaultWorkflowId specifies the default Workflow for new Assets.

    Set null to clear it.
    """
