# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .workflow_rule import WorkflowRule

__all__ = ["Workflow"]


class Workflow(BaseModel):
    """A reusable definition of actions triggered by Asset events."""

    id: str
    """Unique Workflow ID."""

    archived_at: Optional[datetime] = None
    """When the Workflow was archived, or null if it is available for selection.

    Archiving stops new runs; accepted actions finish.
    """

    created_at: datetime
    """When the Workflow was created."""

    name: str
    """Name specifies the Workflow name. Use 1 to 128 characters."""

    revision: int
    """Current definition revision. Starts at 1 and increases when rules are replaced."""

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

    updated_at: datetime
    """When the Workflow was last updated."""
