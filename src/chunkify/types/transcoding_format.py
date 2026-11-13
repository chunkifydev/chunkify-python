# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TranscodingFormat"]


class TranscodingFormat(BaseModel):
    """Resolved encoding settings accepted at creation.

    Only settings applicable to the selected streams and codec are included.
    """

    id: Literal["mp4_h264", "mp4_h265", "mp4_av1", "webm_vp9", "m4a_aac"]
    """Id specifies the resolved container and codec selection."""

    duration: float
    """
    Duration specifies the accepted output duration in seconds, including normalized
    trims.
    """

    seek: float
    """
    Seek specifies the accepted start position in source seconds, normalized to the
    output timeline.
    """

    audio_bitrate: Optional[int] = None
    """AudioBitrate specifies the resolved audio bitrate in bits per second.

    Omitted for video-only output.
    """

    audio_samplerate: Optional[int] = None
    """AudioSamplerate specifies the resolved audio samples per second.

    Omitted for video-only output.
    """

    bufsize: Optional[int] = None
    """
    Bufsize specifies the resolved video buffer size in bits, including codec-level
    defaults. Omitted when no buffer applies.
    """

    channels: Optional[int] = None
    """Channels specifies the resolved audio channel count: 1, 2, 6 or 8.

    Omitted for video-only output.
    """

    cpu_used: Optional[str] = None
    """CpuUsed specifies the accepted VP9 encoder speed setting from 0 through 8.

    Omitted for other codecs.
    """

    crf: Optional[int] = None
    """Crf specifies the accepted constant quality.

    Omitted for bitrate-controlled, per-title and audio-only encoding.
    """

    disable_audio: Optional[bool] = None
    """DisableAudio is true for video-only output. Omitted when audio is selected."""

    framerate: Optional[float] = None
    """Framerate specifies the resolved video frames per second.

    Omitted for audio-only output.
    """

    gop: Optional[int] = None
    """Gop specifies the resolved maximum keyframe interval in frames.

    Omitted for audio-only output.
    """

    height: Optional[int] = None
    """Height specifies the resolved video height in pixels.

    Omitted for audio-only output.
    """

    level: Optional[int] = None
    """Level specifies the accepted codec level when explicitly selected."""

    maxrate: Optional[int] = None
    """
    Maxrate specifies the resolved maximum video bitrate in bits per second,
    including codec-level defaults. Omitted when no maximum applies.
    """

    minrate: Optional[int] = None
    """
    Minrate specifies the accepted minimum video bitrate in bits per second, when
    configured.
    """

    movflags: Optional[str] = None
    """Movflags specifies MP4 packaging. MP4 video exports use faststart."""

    per_title: Optional[bool] = None
    """
    PerTitle specifies whether video rate control is selected during content
    analysis. Omitted for audio-only output.
    """

    pixfmt: Optional[str] = None
    """Pixfmt specifies the accepted video pixel format.

    Omitted for audio-only output.
    """

    preset: Optional[str] = None
    """Preset specifies the accepted codec preset.

    Omitted when the codec does not use presets.
    """

    profilev: Optional[str] = None
    """Profilev specifies the accepted codec profile when explicitly selected."""

    quality: Optional[str] = None
    """Quality specifies the accepted VP9 deadline policy: good, best or realtime.

    Omitted for other codecs.
    """

    video_bitrate: Optional[int] = None
    """VideoBitrate specifies the accepted video bitrate in bits per second.

    Omitted for CRF and per-title encoding.
    """

    width: Optional[int] = None
    """Width specifies the resolved video width in pixels.

    Omitted for audio-only output.
    """
