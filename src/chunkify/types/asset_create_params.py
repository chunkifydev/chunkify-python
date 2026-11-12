# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AssetCreateParams", "Storage"]


class AssetCreateParams(TypedDict, total=False):
    source_id: Required[str]
    """ID of the video Source to process."""

    max_resolution: Literal["1080p", "2160p"]
    """Maximum streaming resolution.

    Omit to use the Project default, or the plan maximum if unset. 2160p requires
    Starter or above. Smaller sources are not upscaled. Does not affect static
    renditions.
    """

    metadata: Dict[str, str]
    """String metadata with a maximum encoded JSON size of 2048 bytes."""

    min_resolution: Literal["auto", "240p", "360p", "540p", "720p", "1080p", "1440p", "2160p"]
    """Minimum streaming resolution.

    Omit to use the Project default; auto removes the minimum. Must not exceed
    max_resolution. Smaller sources are not upscaled. Does not affect static
    renditions.
    """

    path_template: str
    """
    PathTemplate specifies the Asset output folder relative to Storage base_prefix.
    Supports {assetID} and case-sensitive {metadata.<key>}; referenced values must
    be non-empty. Ignored for Chunkify storage, which always uses {assetID}.
    Overrides the Project default. Defaults to {assetID} when neither is set.
    Maximum template size: 1024 UTF-8 bytes. Expanded prefix: 768 bytes including
    base_prefix and trailing slash.
    """

    preview_enabled: bool
    """Allow public preview access without an API token.

    Omit to use the Project default. Does not control CDN or static download access.
    """

    storage: Storage
    """Output Storage.

    Omit to use the Project default. The path_template controls the folder for
    generated output paths.
    """

    title: str
    """Asset title, up to 256 characters. Defaults to an empty string."""

    workflow_id: Optional[str]
    """WorkflowId specifies the Workflow to select.

    Omit to use the Project default. Set null to disable automatic actions. The
    current revision is pinned when creation is accepted.
    """


class Storage(TypedDict, total=False):
    """Output Storage.

    Omit to use the Project default. The path_template controls the folder for generated output paths.
    """

    id: str
    """ID of output Storage in this Project.

    Omit to use the Project default. Applies to all outputs, including static
    renditions added later.
    """
