# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ProjectUpdateParams", "AssetDefaults"]


class ProjectUpdateParams(TypedDict, total=False):
    asset_defaults: AssetDefaults
    """Defaults for new Assets and automatic Uploads.

    Replaces the whole object. Omitted fields reset to their defaults. Existing
    Assets are unchanged.
    """

    default_workflow_id: Optional[str]
    """DefaultWorkflowId specifies the default Workflow for new Assets.

    Set null to clear it.
    """

    name: str
    """Project name."""

    storage_id: str
    """ID of this Project's default Storage."""


class AssetDefaults(TypedDict, total=False):
    """Defaults for new Assets and automatic Uploads.

    Replaces the whole object. Omitted fields reset to their defaults. Existing Assets are unchanged.
    """

    delete_files_on_failure: bool
    """
    Delete generated and partial files from the output Storage when a new Asset
    fails. The Asset record and original Source are preserved. Cleanup is attempted
    once after a delay and requires delete permission on the Storage. Defaults to
    false. Existing Assets are unchanged.
    """

    max_resolution: Literal["1080p", "2160p"]
    """Maximum streaming resolution.

    Defaults to 1080p on Hobby and 2160p on other plans. 2160p requires Starter or
    above. Smaller sources are not upscaled. Does not affect static renditions.
    """

    min_resolution: Literal["auto", "240p", "360p", "540p", "720p", "1080p", "1440p", "2160p"]
    """Minimum streaming resolution.

    Defaults to auto, with no minimum. Must not exceed max_resolution. Smaller
    sources are not upscaled. Does not affect static renditions.
    """

    path_template: str
    """
    PathTemplate specifies the Asset output folder relative to Storage base_prefix.
    Supports {assetID} and case-sensitive {metadata.<key>}; referenced values must
    be non-empty. Ignored for Chunkify storage, which always uses {assetID}.
    Defaults to {assetID}. Maximum template size: 1024 UTF-8 bytes. Expanded prefix:
    768 bytes including base_prefix and trailing slash.
    """

    preview_enabled: bool
    """Allow public preview access for new Assets without an API token.

    Defaults to true. Existing Assets are unchanged.
    """
