# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .asset_defaults_max_resolution import AssetDefaultsMaxResolution
from .asset_defaults_min_resolution import AssetDefaultsMinResolution

__all__ = ["AssetDefaultsParams"]


class AssetDefaultsParams(TypedDict, total=False):
    delete_files_on_failure: bool
    """
    Delete generated and partial files from the output Storage when a new Asset
    fails. The Asset record and original Source are preserved. Cleanup is attempted
    once after a delay and requires delete permission on the Storage. Defaults to
    false. Existing Assets are unchanged.
    """

    max_resolution: AssetDefaultsMaxResolution
    """Maximum streaming resolution.

    Defaults to 1080p on Hobby and 2160p on other plans. 2160p requires Starter or
    above. Smaller sources are not upscaled. Does not affect static renditions.
    """

    min_resolution: AssetDefaultsMinResolution
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
