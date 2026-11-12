# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Project", "AssetDefaults"]


class AssetDefaults(BaseModel):
    """Defaults for new Assets, including Assets created from Uploads."""

    delete_files_on_failure: Optional[bool] = None
    """
    Delete generated and partial files from the output Storage when a new Asset
    fails. The Asset record and original Source are preserved. Cleanup is attempted
    once after a delay and requires delete permission on the Storage. Defaults to
    false. Existing Assets are unchanged.
    """

    max_resolution: Optional[Literal["1080p", "2160p"]] = None
    """Maximum streaming resolution.

    Defaults to 1080p on Hobby and 2160p on other plans. 2160p requires Starter or
    above. Smaller sources are not upscaled. Does not affect static renditions.
    """

    min_resolution: Optional[Literal["auto", "240p", "360p", "540p", "720p", "1080p", "1440p", "2160p"]] = None
    """Minimum streaming resolution.

    Defaults to auto, with no minimum. Must not exceed max_resolution. Smaller
    sources are not upscaled. Does not affect static renditions.
    """

    path_template: Optional[str] = None
    """
    PathTemplate specifies the Asset output folder relative to Storage base_prefix.
    Supports {assetID} and case-sensitive {metadata.<key>}; referenced values must
    be non-empty. Ignored for Chunkify storage, which always uses {assetID}.
    Defaults to {assetID}. Maximum template size: 1024 UTF-8 bytes. Expanded prefix:
    768 bytes including base_prefix and trailing slash.
    """

    preview_enabled: Optional[bool] = None
    """Allow public preview access for new Assets without an API token.

    Defaults to true. Existing Assets are unchanged.
    """


class Project(BaseModel):
    id: str
    """Id is the unique identifier for the project."""

    asset_defaults: AssetDefaults
    """Defaults for new Assets, including Assets created from Uploads."""

    created_at: datetime
    """Timestamp when the project was created"""

    name: str
    """Name of the project"""

    slug: str
    """Slug is the slug for the project."""

    storage_id: str
    """StorageId identifier where project files are stored"""

    default_workflow_id: Optional[str] = None
    """DefaultWorkflowId specifies the default Workflow for new Assets.

    Set null to clear it.
    """
