# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .asset_output_status import AssetOutputStatus
from .asset_static_rendition import AssetStaticRendition

__all__ = ["AssetStaticRenditionOutput"]


class AssetStaticRenditionOutput(BaseModel):
    """An Asset-owned static rendition output and its canonical resource details."""

    id: str
    """Id identifies the Asset output, prefixed with aop\\__.

    The type field identifies the output kind.
    """

    asset_id: str
    """AssetId identifies the owning Asset."""

    details: AssetStaticRendition
    """
    Details contains the canonical typed output resource, including its available
    delivery fields.
    """

    status: AssetOutputStatus
    """Status specifies the output processing state.

    Expired means temporary output files are no longer available.
    """

    type: Literal["static_rendition"]
    """Type identifies the output kind."""
