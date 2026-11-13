# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TranscodingStorage"]


class TranscodingStorage(BaseModel):
    """The resolved output destination for a Transcoding."""

    id: str
    """Id identifies the output Storage."""

    path: str
    """
    Path specifies the output file path relative to the Storage base_prefix saved at
    creation.
    """
