# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["KeyCreateParams"]


class KeyCreateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    purpose: Required[Literal["player", "read", "mcp"]]
    """
    Purpose distinguishes player ingestion, read-only API access and a separate
    read-only MCP credential. Read and MCP keys have the same collector permissions.
    """
