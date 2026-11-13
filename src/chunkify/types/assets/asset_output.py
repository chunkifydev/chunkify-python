# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..asset_caption_output import AssetCaptionOutput
from ..asset_thumbnail_output import AssetThumbnailOutput
from ..asset_transcript_output import AssetTranscriptOutput
from ..asset_static_rendition_output import AssetStaticRenditionOutput

__all__ = ["AssetOutput"]

AssetOutput: TypeAlias = Annotated[
    Union[AssetCaptionOutput, AssetStaticRenditionOutput, AssetThumbnailOutput, AssetTranscriptOutput],
    PropertyInfo(discriminator="type"),
]
