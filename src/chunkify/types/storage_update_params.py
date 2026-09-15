# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["StorageUpdateParams"]


class StorageUpdateParams(TypedDict, total=False):
    base_prefix: str
    """Object-key prefix for future final job outputs.

    Existing files keep their stored object keys. Send an empty string to use the
    bucket root.
    """

    cdn_base_url: Optional[str]
    """Customer-managed HTTPS delivery origin, or null to remove the current value."""
