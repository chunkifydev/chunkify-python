# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NotificationCreateParams"]


class NotificationCreateParams(TypedDict, total=False):
    event: Required[
        Literal[
            "job.created",
            "job.completed",
            "job.failed",
            "job.cancelled",
            "source.created",
            "source.deleted",
            "upload.created",
            "upload.completed",
            "upload.failed",
            "upload.expired",
            "asset.created",
            "asset.ready",
            "asset.playback_ready",
            "asset.failed",
            "asset.expired",
            "asset.deleted",
            "asset.output.created",
            "asset.output.ready",
            "asset.output.failed",
            "asset.output.deleted",
            "workflow_run.created",
            "workflow_run.completed",
            "workflow_run.failed",
            "workflow_run.cancelled",
            "transcoding.created",
            "transcoding.ready",
            "transcoding.failed",
            "transcoding.cancelled",
            "transcoding.expired",
            "transcoding.deleted",
            "thumbnail.created",
            "thumbnail.ready",
            "thumbnail.failed",
            "thumbnail.expired",
            "thumbnail.deleted",
        ]
    ]
    """Event specifies the type of event that triggered the notification."""

    object_id: Required[str]
    """ID of the resource that triggered the event.

    Use the caption, static rendition, or thumbnail ID for their Asset child events.
    Replaying asset events, job.created, or source.created requires a retained
    snapshot. Resource deletion does not prevent replay.
    """

    webhook_id: Required[str]
    """WebhookId specifies the webhook endpoint that will receive the notification."""
