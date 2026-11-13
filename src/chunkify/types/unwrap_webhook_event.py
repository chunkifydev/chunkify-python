# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .notification_payload_asset import NotificationPayloadAsset
from .notification_payload_thumbnail import NotificationPayloadThumbnail
from .notification_payload_job_failed import NotificationPayloadJobFailed
from .notification_payload_job_created import NotificationPayloadJobCreated
from .notification_payload_transcoding import NotificationPayloadTranscoding
from .notification_payload_asset_output import NotificationPayloadAssetOutput
from .notification_payload_workflow_run import NotificationPayloadWorkflowRun
from .notification_payload_asset_deleted import NotificationPayloadAssetDeleted
from .notification_payload_job_completed import NotificationPayloadJobCompleted
from .notification_payload_upload_failed import NotificationPayloadUploadFailed
from .notification_payload_source_created import NotificationPayloadSourceCreated
from .notification_payload_source_deleted import NotificationPayloadSourceDeleted
from .notification_payload_upload_created import NotificationPayloadUploadCreated
from .notification_payload_upload_completed import NotificationPayloadUploadCompleted
from .notification_payload_asset_output_deleted import NotificationPayloadAssetOutputDeleted

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Annotated[
    Union[
        NotificationPayloadJobCompleted,
        NotificationPayloadJobFailed,
        NotificationPayloadJobCreated,
        NotificationPayloadSourceCreated,
        NotificationPayloadSourceDeleted,
        NotificationPayloadUploadCreated,
        NotificationPayloadUploadCompleted,
        NotificationPayloadUploadFailed,
        NotificationPayloadAsset,
        NotificationPayloadAssetOutput,
        NotificationPayloadAssetOutputDeleted,
        NotificationPayloadAssetDeleted,
        NotificationPayloadWorkflowRun,
        NotificationPayloadTranscoding,
        NotificationPayloadThumbnail,
    ],
    PropertyInfo(discriminator="event"),
]
