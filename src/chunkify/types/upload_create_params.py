# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["UploadCreateParams", "Storage"]


class UploadCreateParams(TypedDict, total=False):
    create_asset: bool
    """CreateAsset specifies whether to create an Asset after Upload completion.

    Defaults to false. Snapshots the Project output settings, including the path
    template. Referenced metadata must be non-empty in this request. Asset
    processing is billed separately.
    """

    file_size_bytes: int
    """FileSizeBytes specifies the exact file size in bytes.

    Required when UploadMode is omitted, auto, or multipart. Optional for explicit
    single mode. Must fit the team's Source size limit. Single PUT supports up to 5
    GiB, subject to the provider's limit; multipart supports up to 5 TiB.
    """

    metadata: Dict[str, str]
    """
    Metadata allows for additional information to be attached to the upload, with a
    maximum size of 2048 bytes.
    """

    storage: Storage
    """Optional Storage override.

    Omit id to use the Project default. Customer-connected Storage requires path;
    Chunkify Storage generates its own path.
    """

    upload_mode: Literal["single", "multipart", "auto"]
    """UploadMode specifies the transfer method.

    Defaults to auto. Auto chooses multipart above 100 MiB and single PUT at or
    below 100 MiB for every Storage provider. Multipart requires a provider that
    supports the required multipart operations and signed part URLs. Provider
    failures return an error without falling back to single PUT.
    """

    validity_timeout: int
    """ValidityTimeout specifies the session and signed URL lifetime in seconds.

    Single PUT defaults to 7200 and allows 300–36000. Multipart defaults to twice
    the transfer time at 5 Mbps plus 1800 seconds, bounded to 7200–172800; an
    explicit value allows 300–172800. Complete before expiry. Storage credentials
    and policies can shorten URL validity. Expired URLs cannot be refreshed.
    """

    workflow_id: Optional[str]
    """WorkflowId specifies the Workflow to select.

    Omit to use the Project default. Set null to disable automatic actions. The
    current revision is pinned when creation is accepted.
    """


class Storage(TypedDict, total=False):
    """Optional Storage override.

    Omit id to use the Project default. Customer-connected Storage requires path; Chunkify Storage generates its own path.
    """

    id: str
    """Storage belonging to this Project. Omit to use the Project default."""

    path: str
    """
    Exact object key including filename, required for customer Storage and forbidden
    for Chunkify Storage. The output base_prefix is not added. Existing keys may be
    overwritten.
    """
