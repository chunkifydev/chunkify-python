# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WebhookEvent"]

WebhookEvent: TypeAlias = Literal[
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
