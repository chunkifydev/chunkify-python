# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["JobCreateStorageParams"]


class JobCreateStorageParams(TypedDict, total=False):
    id: str
    """
    Storage Id specifies the storage configuration to use from pre-configured
    storage options. Must be 4-64 characters long and contain only alphanumeric
    characters, underscores and hyphens. Optional if Storage Path is provided.
    """

    path: str
    """
    Storage Path specifies an object path relative to the selected storage
    connection's base_prefix. Do not include the base_prefix. Leading slashes are
    accepted for compatibility and removed before the path is stored. The
    base_prefix and normalized path may contain at most 1024 bytes combined.
    Optional if Storage Id is provided.
    """
