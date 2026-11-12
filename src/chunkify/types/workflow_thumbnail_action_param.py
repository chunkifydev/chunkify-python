# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .workflow_thumbnail_params_param import WorkflowThumbnailParamsParam

__all__ = ["WorkflowThumbnailActionParam"]


class WorkflowThumbnailActionParam(TypedDict, total=False):
    """Creates an independent thumbnail request after asset.ready.

    Replaying this action uses its accepted request; separate actions create separate requests.
    """

    id: Required[str]
    """Id specifies a stable action key, unique within its rule."""

    params: Required[WorkflowThumbnailParamsParam]
    """Params specifies sampling and image settings.

    Outputs use the Asset folder and Storage.
    """

    type: Required[Literal["create_thumbnails"]]
    """Type specifies the action to perform. Must be create_thumbnails."""
