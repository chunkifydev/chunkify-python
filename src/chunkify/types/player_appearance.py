# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .player_control import PlayerControl
from .player_palette import PlayerPalette
from .player_theme_mode import PlayerThemeMode

__all__ = ["PlayerAppearance"]


class PlayerAppearance(BaseModel):
    dark: PlayerPalette
    """Dark specifies the player colours in dark mode."""

    hidden_controls: List[PlayerControl]
    """
    HiddenControls lists the player buttons to hide. Other buttons appear when the
    browser and video support them.
    """

    light: PlayerPalette
    """Light specifies the player colours in light mode."""

    mode: PlayerThemeMode
    """Mode specifies which palette the player uses.

    auto follows the viewer's system setting.
    """
