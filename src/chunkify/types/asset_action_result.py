# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AssetActionResult"]


class AssetActionResult(BaseModel):
    """Reference to the output created or reused by a completed action."""

    output_id: str
    """
    ID of the caption, static rendition, or thumbnail request produced by the
    action.
    """

    output_type: Literal["caption", "static_rendition", "thumbnail", "transcript"]
    """Type of output referenced by output_id.

    Caption generation and translation both produce caption outputs.
    """

    reused: bool
    """Whether the action reused an existing output instead of creating one."""
