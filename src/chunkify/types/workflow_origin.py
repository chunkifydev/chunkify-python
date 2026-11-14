# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WorkflowOrigin"]


class WorkflowOrigin(BaseModel):
    """
    Connects this rule to the output created or reused by an action in the same Workflow revision.
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
