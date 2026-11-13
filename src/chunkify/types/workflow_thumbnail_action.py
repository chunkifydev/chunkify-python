# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .workflow_thumbnail import WorkflowThumbnail

__all__ = ["WorkflowThumbnailAction"]


class WorkflowThumbnailAction(BaseModel):
    """Creates an independent thumbnail request after asset.ready.

    Replaying this action uses its accepted request; separate actions create separate requests.
    """

    id: str
    """Id specifies a stable action key, unique within its rule."""

    params: WorkflowThumbnail
    """Params specifies sampling and image settings.

    Outputs use the Asset folder and Storage.
    """

    type: Literal["create_thumbnails"]
    """Type specifies the action to perform. Must be create_thumbnails."""
