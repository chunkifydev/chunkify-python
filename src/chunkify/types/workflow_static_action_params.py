# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .workflow_static_params import WorkflowStaticParams

__all__ = ["WorkflowStaticActionParams"]


class WorkflowStaticActionParams(TypedDict, total=False):
    """Creates or reuses one static rendition for the Asset."""

    id: Required[str]
    """
    Id specifies a stable action key, unique within its rule. Use 1 to 64
    characters, starting with a letter and containing only letters, digits, or
    underscores.
    """

    params: Required[WorkflowStaticParams]
    """Params specifies the static rendition resolution."""

    type: Required[Literal["create_static_rendition"]]
    """Type specifies the action to perform. Must be create_static_rendition."""
