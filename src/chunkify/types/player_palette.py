# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PlayerPalette"]


class PlayerPalette(BaseModel):
    accent: str
    """Accent specifies the colour of progress and active controls."""

    primary: str
    """Primary specifies the colour of text and control icons."""

    secondary: str
    """Secondary specifies the colour of player buttons."""
