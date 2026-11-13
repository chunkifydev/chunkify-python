# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["MetricsUsageTranscodings"]


class MetricsUsageTranscodings(BaseModel):
    """Standalone Transcoding usage."""

    audio_output_seconds: int
    """AudioOutputSeconds specifies the audio-only subset of output_seconds."""

    failed: int
    """Failed specifies recorded failed Transcoding outcomes."""

    output_seconds: int
    """
    OutputSeconds specifies settled billable output duration, including audio-only
    output.
    """

    output_seconds_by_resolution: Dict[str, int]
    """Video duration in seconds by pricing resolution tier.

    Contains sd, hd, 2k and uhd keys; audio is reported separately.
    """

    ready: int
    """Ready specifies recorded successful Transcoding outcomes."""
