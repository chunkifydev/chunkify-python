# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["AssetUpdateParams"]


class AssetUpdateParams(TypedDict, total=False):
    metadata: Dict[str, str]
    """Replaces all metadata.

    Send {} to clear it; omit to leave unchanged. Maximum encoded JSON size: 2,048
    bytes.
    """

    preview_enabled: bool
    """Allow public preview access without an API token.

    Does not control CDN or static download access. Disabling it does not revoke
    signed URLs already issued.
    """

    title: str
    """Asset title, up to 256 characters.

    Send an empty string to clear it; omit to leave unchanged.
    """
