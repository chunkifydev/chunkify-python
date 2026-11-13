# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .asset_caption import AssetCaption
from .asset_output_status import AssetOutputStatus

__all__ = ["AssetCaptionOutput"]


class AssetCaptionOutput(BaseModel):
    """An Asset-owned caption output and its canonical resource details."""

    id: str
    """Id identifies the Asset output, prefixed with aop\\__.

    The type field identifies the output kind.
    """

    asset_id: str
    """AssetId identifies the owning Asset."""

    details: AssetCaption
    """
    Details contains the canonical typed output resource, including its available
    delivery fields.
    """

    status: AssetOutputStatus
    """Status specifies the output processing state.

    Expired means temporary output files are no longer available.
    """

    type: Literal["caption"]
    """Type identifies the output kind."""
