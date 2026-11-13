# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .transcoding_create_format_params import TranscodingCreateFormatParams
from .transcoding_create_storage_params import TranscodingCreateStorageParams

__all__ = ["TranscodingCreateParams"]


class TranscodingCreateParams(TypedDict, total=False):
    format: Required[TranscodingCreateFormatParams]
    """Format specifies the requested encoding settings."""

    source_id: Required[str]
    """SourceId identifies a Source in this Project."""

    metadata: Dict[str, str]
    """Metadata attaches string values to the Transcoding.

    The serialized object may contain at most 2048 bytes.
    """

    storage: TranscodingCreateStorageParams
    """Storage overrides the Project output destination.

    Source storage remains independent.
    """
