# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .assets.asset_output import AssetOutput

__all__ = ["NotificationPayloadAssetOutputData"]


class NotificationPayloadAssetOutputData(BaseModel):
    """Payload for Asset output creation, readiness, and failure events."""

    output: AssetOutput
    """
    Output contains the canonical typed output snapshot at the event time, matching
    the output API.
    """
