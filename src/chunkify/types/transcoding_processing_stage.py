# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TranscodingProcessingStage"]

TranscodingProcessingStage: TypeAlias = Literal["queued", "starting", "encoding", "finalizing", "uploading"]
