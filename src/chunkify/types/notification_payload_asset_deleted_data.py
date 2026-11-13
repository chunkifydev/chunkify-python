# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .asset import Asset
from .._models import BaseModel

__all__ = ["NotificationPayloadAssetDeletedData"]


class NotificationPayloadAssetDeletedData(BaseModel):
    """Payload for asset.deleted.

    The Asset snapshot is preserved after record deletion.
    """

    asset: Asset

    files_deleted: bool
    """
    FilesDeleted indicates whether the requested cleanup of the Asset's generated
    files completed without error. Missing files count as successful cleanup. False
    means these files were not removed at event time. Private transcript text and
    saved subtitle copies are always scheduled for asynchronous cleanup.
    """

    deleted_size: Optional[int] = None
    """
    DeletedSize specifies the recorded generated-file bytes removed with the Asset,
    including attached outputs. Omitted when cleanup was not requested or the total
    is unavailable. Missing storage objects still contribute their recorded sizes.
    """
