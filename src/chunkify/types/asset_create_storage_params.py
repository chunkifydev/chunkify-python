# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AssetCreateStorageParams"]


class AssetCreateStorageParams(TypedDict, total=False):
    id: str
    """ID of output Storage in this Project.

    Omit to use the Project default. Applies to all outputs, including static
    renditions added later.
    """
