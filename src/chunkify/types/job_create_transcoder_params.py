# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .shared.instance_type import InstanceType

__all__ = ["JobCreateTranscoderParams"]


class JobCreateTranscoderParams(TypedDict, total=False):
    quantity: int
    """Quantity specifies the number of transcoder instances. Required if Type is set."""

    type: InstanceType
    """
    Type specifies the CPU configuration for each transcoder instance. Required if
    Quantity is set.
    """
