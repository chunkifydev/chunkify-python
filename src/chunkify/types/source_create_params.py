# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["SourceCreateParams", "Storage"]


class SourceCreateParams(TypedDict, total=False):
    metadata: Dict[str, str]
    """
    Metadata allows for additional information to be attached to the source, with a
    maximum size of 2048 bytes.
    """

    storage: Storage
    """Storage input configuration. Provide this or url, never both."""

    url: str
    """Url is the URL of the source, which must be a valid HTTP URL."""


class Storage(TypedDict, total=False):
    """Storage input configuration. Provide this or url, never both."""

    path: Required[str]
    """Exact object key in the configured bucket, 1 to 1024 UTF-8 bytes.

    The output base_prefix is not added.
    """

    id: str
    """Connected external storage belonging to this project.

    If omitted, uses the project default storage, which must be external. The
    resolved storage ID is saved on the source.
    """
