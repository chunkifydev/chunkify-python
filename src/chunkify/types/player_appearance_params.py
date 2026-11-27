# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .player_control import PlayerControl
from .player_theme_mode import PlayerThemeMode
from .player_palette_params import PlayerPaletteParams

__all__ = ["PlayerAppearanceParams"]


class PlayerAppearanceParams(TypedDict, total=False):
    dark: PlayerPaletteParams
    """Dark specifies the player colours in dark mode.

    Omit to use the default dark colours.
    """

    hidden_controls: List[PlayerControl]
    """HiddenControls lists the player buttons to hide.

    Defaults to an empty list. Other buttons appear when the browser and video
    support them.
    """

    light: PlayerPaletteParams
    """Light specifies the player colours in light mode.

    Omit to use the default light colours.
    """

    mode: PlayerThemeMode
    """Mode specifies which palette the player uses.

    auto follows the viewer's system setting. An embed can override it with its
    theme URL parameter. Defaults to auto.
    """
