# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from ...asset_action_type import AssetActionType
from ...asset_action_input import AssetActionInput
from ...asset_action_result import AssetActionResult
from ...asset_action_status import AssetActionStatus

__all__ = ["AssetActionRun"]


class AssetActionRun(BaseModel):
    """
    One execution of an Asset action, started by a Workflow or a direct output request.
    """

    id: str
    """Unique action execution ID, prefixed with acr\\__."""

    asset_id: str
    """ID of the Asset processed by this action."""

    completed_at: Optional[datetime] = None
    """When the action completed, failed, was skipped, or was cancelled.

    Null while work remains.
    """

    created_at: datetime
    """When the action was accepted."""

    input: AssetActionInput
    """Resolved parameters and input references for this execution."""

    status: AssetActionStatus
    """Current execution status of the action."""

    type: AssetActionType
    """Type of action performed."""

    updated_at: datetime
    """When the action was last updated."""

    workflow_run_id: Optional[str] = None
    """ID of the Workflow run that started the action.

    Null for direct output requests.
    """

    action_id: Optional[str] = None
    """Action key within the rule. Omitted for direct output requests."""

    error: Optional[str] = None
    """Reason the action failed. Omitted when no failure message is available."""

    reason: Optional[str] = None
    """Machine-readable reason for waiting, skipping, failure, or cancellation.

    Omitted when no reason applies.
    """

    result: Optional[AssetActionResult] = None
    """Output reference and reuse flag.

    Included when the action completes successfully.
    """

    rule_id: Optional[str] = None
    """Rule key from the Workflow definition. Omitted for direct output requests."""
