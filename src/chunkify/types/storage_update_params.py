# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["StorageUpdateParams"]


class StorageUpdateParams(TypedDict, total=False):
    access_key_id: str
    """Replacement access key ID for customer-managed storage.

    Send with a non-empty secret_access_key. Omit both credential fields to keep the
    saved pair. Null and empty values are rejected. Credentials are validated before
    either value is saved and are never returned.
    """

    base_prefix: str
    """Object-key prefix for future final job outputs.

    Existing files keep their stored object keys. Send an empty string to use the
    bucket root.
    """

    cdn_base_url: Optional[str]
    """Customer-managed HTTPS delivery origin, or null to remove the current value."""

    secret_access_key: str
    """Replacement secret access key.

    Required with access_key_id; cannot be null or empty. The pair is encrypted and
    saved atomically only after validation succeeds.
    """
