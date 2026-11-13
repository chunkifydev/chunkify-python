# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .workflow_rule_params import WorkflowRuleParams

__all__ = ["WorkflowUpdateParams"]


class WorkflowUpdateParams(TypedDict, total=False):
    expected_revision: int
    """ExpectedRevision specifies the current Workflow revision when replacing rules.

    The update returns a conflict if it no longer matches. Required when rules is
    provided. Must be at least 1.
    """

    name: str
    """Name specifies the Workflow name. Use 1 to 128 characters."""

    rules: Iterable[WorkflowRuleParams]
    """
    Rules specifies the event subscriptions and actions in this definition. Provide
    exactly one asset.ready rule and up to 15 connected rules, with at most 32
    actions and 65536 encoded bytes across all rules. Array order affects display
    only. Replaces the complete definition and requires schema_version and
    expected_revision. Existing Assets and Uploads keep their pinned revision.
    """

    schema_version: Literal[1]
    """SchemaVersion specifies the Workflow definition format.

    The supported version is 1. Required when rules is provided.
    """
