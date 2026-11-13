# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .asset import Asset
from .._models import BaseModel

__all__ = ["NotificationPayloadAssetData"]


class NotificationPayloadAssetData(BaseModel):
    asset: Asset
