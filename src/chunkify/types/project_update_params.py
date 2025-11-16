# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    name: str
    """
    Name is the new name for the project, which must be between 4 and 32 characters.
    """

    storage_id: str
    """
    StorageId specifies the storage configuration for the project, which must be
    between 4 and 64 characters.
    """
