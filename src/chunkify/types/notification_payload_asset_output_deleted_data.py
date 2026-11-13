# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .assets.asset_output import AssetOutput

__all__ = ["NotificationPayloadAssetOutputDeletedData"]


class NotificationPayloadAssetOutputDeletedData(BaseModel):
    """Payload for asset.output.deleted.

    The output snapshot is preserved after removal.
    """

    files_deleted: bool
    """
    FilesDeleted indicates whether the requested cleanup of the output files
    completed without error. Missing files count as successful cleanup. False means
    these files were not removed at event time. Private transcript text and saved
    subtitle copies are always scheduled for asynchronous cleanup.
    """

    output: AssetOutput
    """Output contains the canonical typed output snapshot before removal."""
