# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .job_create_format_params import JobCreateFormatParams
from .job_create_storage_params import JobCreateStorageParams
from .job_create_transcoder_params import JobCreateTranscoderParams

__all__ = ["JobCreateParams"]


class JobCreateParams(TypedDict, total=False):
    format: Required[JobCreateFormatParams]
    """
    Required format configuration, one and only one valid format configuration must
    be provided. If you want to use a format without specifying any configuration,
    use an empty object in the corresponding field.
    """

    source_id: Required[str]
    """The ID of the source file to transcode"""

    hls_manifest_id: str
    """
    Optional HLS manifest configuration Use the same hls manifest ID to group
    multiple jobs into a single HLS manifest By default, it's automatically
    generated if no set for HLS jobs
    """

    metadata: Dict[str, str]
    """Optional metadata to attach to the job, the maximum size allowed is 2048 bytes"""

    storage: JobCreateStorageParams
    """Optional storage configuration"""

    transcoder: JobCreateTranscoderParams
    """Optional transcoder configuration.

    If not provided, the system will automatically calculate the optimal quantity
    and CPU type based on the source file specifications and output requirements.
    This auto-scaling ensures efficient resource utilization.
    """
