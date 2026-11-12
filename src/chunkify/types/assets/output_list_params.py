# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OutputListParams"]


class OutputListParams(TypedDict, total=False):
    limit: int
    """Limit specifies the maximum number of results to return. Accepts 1 to 100.

    Defaults to 100.
    """

    offset: int
    """Offset specifies the number of matching results to skip. Must be at least 0.

    Defaults to 0.
    """

    status: Literal["preparing", "ready", "failed", "expired"]
    """Status specifies the current output state to include.

    Omit it to include all states.
    """

    type: Literal["caption", "transcript", "static_rendition", "thumbnail"]
    """Type specifies the output kind to include. Omit it to include all kinds."""
