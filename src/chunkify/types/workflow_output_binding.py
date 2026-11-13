# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow_output_binding_from import WorkflowOutputBindingFrom

__all__ = ["WorkflowOutputBinding"]


class WorkflowOutputBinding(BaseModel):
    """Selects the output referenced by the triggering event."""

    from_: WorkflowOutputBindingFrom = FieldInfo(alias="from")
    """From specifies where to read the input output ID.

    Use event.output.id to consume the output in the triggering asset.output.ready
    event.
    """
