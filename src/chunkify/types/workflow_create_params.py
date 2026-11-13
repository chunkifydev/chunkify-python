# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .workflow_rule_params import WorkflowRuleParams

__all__ = ["WorkflowCreateParams"]


class WorkflowCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name specifies the Workflow name. Use 1 to 128 characters."""

    rules: Required[Iterable[WorkflowRuleParams]]
    """
    Rules specifies the event subscriptions and actions in this definition. Provide
    exactly one asset.ready rule and up to 15 connected rules, with at most 32
    actions and 65536 encoded bytes across all rules. Array order affects display
    only.
    """

    schema_version: Required[Literal[1]]
    """SchemaVersion specifies the Workflow definition format.

    The supported version is 1.
    """
