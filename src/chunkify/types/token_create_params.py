# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .token_scope import TokenScope

__all__ = ["TokenCreateParams"]


class TokenCreateParams(TypedDict, total=False):
    scope: Required[TokenScope]
    """
    Scope specifies the scope of the token, which must be either "team" or
    "project".
    """

    name: str
    """Name is the name of the token, which can be up to 64 characters long."""

    project_id: str
    """ProjectId is required if the scope is set to "project"."""
