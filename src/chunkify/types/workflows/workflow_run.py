# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WorkflowRun", "Actions"]


class Actions(BaseModel):
    """Counts of action outcomes in this run.

    Reused actions are included in completed.
    """

    cancelled: int
    """Number of actions cancelled before completion."""

    completed: int
    """Number of actions that completed successfully, including reused outputs."""

    failed: int
    """Number of actions that failed."""

    reused: int
    """Number of completed actions that reused an existing output.

    Included in completed.
    """

    skipped: int
    """Number of actions skipped without producing an output."""

    total: int
    """Total number of actions in the run, including unfinished actions."""


class WorkflowRun(BaseModel):
    """
    One execution of Workflow rules for an Asset, started by an event or by updating to a newer revision.
    """

    id: str
    """Unique Workflow run ID."""

    actions: Actions
    """Counts of action outcomes in this run.

    Reused actions are included in completed.
    """

    asset_execution_status: Literal["pending", "running", "completed", "failed", "cancelled"]
    """
    AssetExecutionStatus specifies the combined status of this revision for the
    Asset across retained runs. Any failed action or run makes it failed. Pending or
    active work, or an Asset still preparing for an unarchived Workflow, makes it
    running. Otherwise it is completed.
    """

    asset_id: str
    """ID of the Asset processed by this run."""

    completed_at: Optional[datetime] = None
    """When the run completed, failed, or was cancelled.

    Null while the run is pending or running.
    """

    created_at: datetime
    """When the run was created."""

    event: str
    """
    Event specifies the Asset lifecycle event that triggered this run, or manual
    when the Asset was updated to a newer revision. Action details are available
    from the run's actions endpoint.
    """

    event_id: Optional[str] = None
    """EventId specifies the event that triggered this run.

    Null when the Asset was updated to a newer revision.
    """

    revision: int
    """Pinned Workflow revision used by this run."""

    root_run_id: str
    """ID of the first run in this event chain.

    Equals id when this run starts the chain.
    """

    status: Literal["pending", "running", "completed", "failed", "cancelled"]
    """Current status of this event run, based on its own actions."""

    updated_at: datetime
    """When the run was last updated."""

    workflow_id: str
    """ID of the Workflow executed by this run."""

    error: Optional[str] = None
    """Reason the run failed. Omitted when no failure message is available."""
