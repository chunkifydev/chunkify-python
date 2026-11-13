# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WorkflowActionCounts"]


class WorkflowActionCounts(BaseModel):
    """Counts of action outcomes in this run."""

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
