# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["UploadCreateParams", "Storage"]


class UploadCreateParams(TypedDict, total=False):
    metadata: Dict[str, str]
    """
    Metadata allows for additional information to be attached to the upload, with a
    maximum size of 2048 bytes.
    """

    storage: Storage
    """Optional Storage override.

    Omit id to use the Project default. Customer-connected Storage requires path;
    Chunkify Storage generates its own path.
    """

    validity_timeout: int
    """
    Both the file PUT and completion POST must finish within this timeout in seconds
    """


class Storage(TypedDict, total=False):
    """Optional Storage override.

    Omit id to use the Project default. Customer-connected Storage requires path; Chunkify Storage generates its own path.
    """

    id: str
    """Storage belonging to this Project. Omit to use the Project default."""

    path: str
    """
    Exact object key including filename, required for customer Storage and forbidden
    for Chunkify Storage. The output base_prefix is not added. Existing keys may be
    overwritten.
    """
