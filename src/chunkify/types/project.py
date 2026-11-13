# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .asset_defaults import AssetDefaults

__all__ = ["Project"]


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
