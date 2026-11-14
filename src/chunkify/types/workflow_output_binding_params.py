# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .workflow_output_binding_from import WorkflowOutputBindingFrom

__all__ = ["WorkflowOutputBindingParams"]

_WorkflowOutputBindingParamsReservedKeywords = TypedDict(
    "_WorkflowOutputBindingParamsReservedKeywords",
    {
        "from": WorkflowOutputBindingFrom,
    },
    total=False,
)


class WorkflowOutputBindingParams(_WorkflowOutputBindingParamsReservedKeywords, total=False):
    """Selects the output referenced by the triggering event."""

    pass
