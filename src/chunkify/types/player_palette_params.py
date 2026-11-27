# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PlayerPaletteParams"]


class PlayerPaletteParams(TypedDict, total=False):
    accent: Required[str]
    """Accent specifies the colour of progress and active controls, as #rrggbb."""

    primary: Required[str]
    """Primary specifies the colour of text and control icons, as #rrggbb."""

    secondary: Required[str]
    """Secondary specifies the colour of player buttons, as #rrggbb."""
