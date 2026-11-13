# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .workflow_static import WorkflowStatic

__all__ = ["WorkflowStaticAction"]


class WorkflowStaticAction(BaseModel):
    """Creates or reuses one static rendition for the Asset."""

    id: str
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: WorkflowStatic
    """Params specifies the static rendition resolution."""

    type: Literal["create_static_rendition"]
    """Type specifies the action to perform. Must be create_static_rendition."""
