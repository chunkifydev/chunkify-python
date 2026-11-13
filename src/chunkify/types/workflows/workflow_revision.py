# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel
from ..workflow_rule import WorkflowRule

__all__ = ["WorkflowRevision"]


class WorkflowRevision(BaseModel):
    """An immutable Workflow definition pinned to Assets and Uploads at creation."""

    created_at: datetime
    """When this Workflow revision was created."""

    revision: int
    """Definition revision number, starting at 1."""

    rules: List[WorkflowRule]
    """
    Rules specifies the event subscriptions and actions in this definition. Provide
    exactly one asset.ready rule and up to 15 connected rules, with at most 32
    actions and 65536 encoded bytes across all rules. Array order affects display
    only.
    """

    schema_version: int
    """SchemaVersion specifies the Workflow definition format.

    The supported version is 1.
    """

    workflow_id: str
    """ID of the Workflow that owns this revision."""
