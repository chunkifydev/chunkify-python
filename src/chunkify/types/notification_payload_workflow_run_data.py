# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .workflows.workflow_run import WorkflowRun
from .assets.workflow.asset_action_run import AssetActionRun

__all__ = ["NotificationPayloadWorkflowRunData"]


class NotificationPayloadWorkflowRunData(BaseModel):
    """
    Payload for workflow_run.created, workflow_run.completed, workflow_run.failed, and workflow_run.cancelled. The run and its actions are snapshots taken when the event was recorded.
    """

    action_runs: List[AssetActionRun]
    """
    ActionRuns specifies every action admitted by this run, including its rule and
    action IDs, type, input, status, output reference, and any skip or failure
    reason. Actions from other runs are excluded.
    """

    workflow_run: WorkflowRun
    """Snapshot of the Workflow run when the event was recorded."""
