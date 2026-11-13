# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .asset_defaults_params import AssetDefaultsParams

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    asset_defaults: AssetDefaultsParams
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
