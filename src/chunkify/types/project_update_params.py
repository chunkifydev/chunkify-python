# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ProjectUpdateParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    name: Required[str]

    storage_id: str


class Variant1(TypedDict, total=False):
    storage_id: Required[str]

    name: str


ProjectUpdateParams: TypeAlias = Union[Variant0, Variant1]
