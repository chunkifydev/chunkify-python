# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .thumbnail_crop import ThumbnailCrop

__all__ = ["ThumbnailSample"]


class ThumbnailSample(BaseModel):
    """One successfully published requested sample.

    Repeated samples remain separate entries.
    """

    height: int
    """Height specifies this image or tile height in pixels."""

    path: str
    """Path identifies the image or sprite sheet in files."""

    timestamp: float
    """
    Timestamp specifies the measured Source-relative presentation time of the
    selected frame in seconds. Compatible cached inputs use millisecond timestamps,
    which can select a neighboring frame compared with the original Source.
    """

    width: int
    """Width specifies this image or tile width in pixels."""

    crop: Optional[ThumbnailCrop] = None
    """Crop specifies the tile origin in its sprite sheet.

    Omitted for individual images; width and height give the tile dimensions.
    """
