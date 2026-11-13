# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .source_create_storage_params import SourceCreateStorageParams

__all__ = ["SourceCreateParams"]


class SourceCreateParams(TypedDict, total=False):
    metadata: Dict[str, str]
    """
    Metadata allows for additional information to be attached to the source, with a
    maximum size of 2048 bytes.
    """

    storage: SourceCreateStorageParams
    """Storage input configuration. Provide this or url, never both."""

    url: str
    """Url is the URL of the source, which must be a valid HTTP URL."""
