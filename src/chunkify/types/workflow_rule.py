# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .workflow_action import WorkflowAction

__all__ = ["WorkflowRule", "Origin"]


class Origin(BaseModel):
    """Origin specifies the action whose ready output starts this rule.

    Required for asset.output.ready; omit it for asset.ready. Translation steps must connect to a create_caption action.
    References must point to a compatible action in this definition and must not form a cycle.
    """

    action_id: str
    """
    ActionId specifies the ID of the producing action within that rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    rule_id: str
    """
    RuleId specifies the ID of the rule containing the producing action. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """


class WorkflowRule(BaseModel):
    """A starting or connected step with one or more independent actions."""

    id: str
    """
    Id specifies a stable rule key, unique within this Workflow definition. Use 1 to
    64 characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    actions: List[WorkflowAction]
    """Actions specifies the work to start when the rule matches.

    Actions can run concurrently; array order does not define execution order.
    Provide 1 to 32 actions per rule, with at most 32 across the definition.
    """

    event: Literal["asset.ready", "asset.output.ready"]
    """Event specifies when this rule starts.

    Use asset.ready for the single starting rule. Output ready events require an
    origin caption or static rendition action in this Workflow.
    """

    origin: Optional[Origin] = None
    """Origin specifies the action whose ready output starts this rule.

    Required for asset.output.ready; omit it for asset.ready. Translation steps must
    connect to a create_caption action. References must point to a compatible action
    in this definition and must not form a cycle.
    """
