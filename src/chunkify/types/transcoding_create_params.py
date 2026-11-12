# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "TranscodingCreateParams",
    "Format",
    "FormatMP4H264",
    "FormatMP4H265",
    "FormatMP4Av1",
    "FormatWebmVp9",
    "FormatM4aAac",
    "Storage",
]


class TranscodingCreateParams(TypedDict, total=False):
    format: Required[Format]
    """Format specifies the requested encoding settings."""

    source_id: Required[str]
    """SourceId identifies a Source in this Project."""

    metadata: Dict[str, str]
    """Metadata attaches string values to the Transcoding.

    The serialized object may contain at most 2048 bytes.
    """

    storage: Storage
    """Storage overrides the Project output destination.

    Source storage remains independent.
    """


class FormatMP4H264(TypedDict, total=False):
    id: Required[Literal["mp4_h264"]]
    """Id specifies the output format."""

    audio_bitrate: int
    """AudioBitrate specifies the output audio bitrate in bits per second.

    Defaults to 128000.
    """

    audio_samplerate: Literal[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000]
    """AudioSamplerate specifies the output sample rate in Hz.

    Defaults to 48000. WebM Opus audio uses 48000.
    """

    channels: Literal[1, 2, 6, 8]
    """Channels specifies the output channel count.

    Defaults to stereo. Six channels means 5.1; eight means 7.1.
    """

    crf: int
    """
    Crf (Constant Rate Factor) controls the quality of the output video. Lower
    values mean better quality but larger file size. Range: 16 to 35. Recommended
    values: 18-28 for high quality, 23-28 for good quality, 28-35 for acceptable
    quality.
    """

    duration: float
    """Duration specifies the requested output length in seconds.

    Defaults to the remaining source duration and is capped at the source end.
    Audio-only output must resolve to at least 0.001 seconds after trimming and
    sample rounding. The accepted interval determines the fixed price.
    """

    level: Literal[10, 11, 12, 13, 20, 21, 22, 30, 31, 32, 40, 41, 42, 50, 51]
    """
    Level specifies the H.264 decoder level using its two-digit representation, such
    as 41 for level 4.1. The dimensions, frame rate and rate controls must fit this
    level and the effective profile. Omitted rate limits resolve to level-compatible
    defaults.
    """

    movflags: Literal["faststart"]
    """Movflags specifies MP4 packaging.

    Defaults to faststart, which places playback metadata before the media.
    """

    pixfmt: Literal["yuv420p", "yuv422p", "yuv444p", "yuv420p10le", "yuv422p10le", "yuv444p10le"]
    """Pixfmt specifies the output pixel format.

    Defaults to yuv420p. The selected profile must support it.
    """

    preset: Literal["ultrafast", "superfast", "veryfast", "faster", "fast", "medium"]
    """Preset specifies the encoding speed preset.

    Valid values (from fastest to slowest):

    - ultrafast: Fastest encoding, lowest quality
    - superfast: Very fast encoding, lower quality
    - veryfast: Fast encoding, moderate quality
    - faster: Faster encoding, good quality
    - fast: Fast encoding, better quality
    - medium: Balanced preset, best quality
    """

    profilev: Literal["baseline", "main", "high", "high10", "high422", "high444"]
    """Profilev specifies the H.264 profile. Valid values:

    - baseline: Basic profile, good for mobile devices
    - main: Main profile, good for most applications
    - high: High profile, best quality but requires more processing
    - high10: High 10-bit profile, supports 10-bit color
    - high422: High 4:2:2 profile, supports 4:2:2 color sampling
    - high444: High 4:4:4 profile, supports 4:4:4 color sampling
    """

    seek: float
    """Seek specifies the start in source seconds.

    Defaults to zero and must precede the source end. The accepted interval uses the
    output frame or sample timeline. Audio-only output must retain at least 0.001
    seconds after sample rounding.
    """

    x264_keyint: int
    """
    X264KeyInt specifies the maximum number of frames between keyframes for H.264
    encoding. Range: 1 to 960. Higher values can improve compression but may affect
    seeking.
    """


class FormatMP4H265(TypedDict, total=False):
    id: Required[Literal["mp4_h265"]]
    """Id specifies the output format."""

    audio_bitrate: int
    """AudioBitrate specifies the output audio bitrate in bits per second.

    Defaults to 128000.
    """

    audio_samplerate: Literal[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000]
    """AudioSamplerate specifies the output sample rate in Hz.

    Defaults to 48000. WebM Opus audio uses 48000.
    """

    channels: Literal[1, 2, 6, 8]
    """Channels specifies the output channel count.

    Defaults to stereo. Six channels means 5.1; eight means 7.1.
    """

    crf: int
    """
    Crf (Constant Rate Factor) controls the quality of the output video. Lower
    values mean better quality but larger file size. Range: 16 to 35. Recommended
    values: 18-28 for high quality, 23-28 for good quality, 28-35 for acceptable
    quality.
    """

    duration: float
    """Duration specifies the requested output length in seconds.

    Defaults to the remaining source duration and is capped at the source end.
    Audio-only output must resolve to at least 0.001 seconds after trimming and
    sample rounding. The accepted interval determines the fixed price.
    """

    level: Literal[30, 31, 41]
    """
    Level specifies the HEVC level using its two-digit representation, such as 31
    for level 3.1. The dimensions, frame rate and rate controls must fit this level.
    Omitted rate limits resolve to level-compatible defaults.
    """

    movflags: Literal["faststart"]
    """Movflags specifies MP4 packaging.

    Defaults to faststart, which places playback metadata before the media.
    """

    pixfmt: Literal[
        "yuv420p",
        "yuv422p",
        "yuv444p",
        "yuv420p10le",
        "yuv422p10le",
        "yuv444p10le",
        "yuv420p12le",
        "yuv422p12le",
        "yuv444p12le",
    ]
    """Pixfmt specifies the output pixel format.

    Defaults to yuv420p. The selected profile must support it.
    """

    preset: Literal["ultrafast", "superfast", "veryfast", "faster", "fast", "medium"]
    """Preset specifies the encoding speed preset.

    Valid values (from fastest to slowest):

    - ultrafast: Fastest encoding, lowest quality
    - superfast: Very fast encoding, lower quality
    - veryfast: Fast encoding, moderate quality
    - faster: Faster encoding, good quality
    - fast: Fast encoding, better quality
    - medium: Balanced preset, best quality
    """

    profilev: Literal["main", "main10", "main12", "main422-10", "main422-12", "main444-8", "main444-10", "main444-12"]
    """Profilev selects the HEVC profile. It must support the requested pixel format."""

    seek: float
    """Seek specifies the start in source seconds.

    Defaults to zero and must precede the source end. The accepted interval uses the
    output frame or sample timeline. Audio-only output must retain at least 0.001
    seconds after sample rounding.
    """

    x265_keyint: int
    """
    X265KeyInt specifies the maximum number of frames between keyframes for H.265
    encoding. Range: 1 to 300. Higher values can improve compression but may affect
    seeking.
    """


class FormatMP4Av1(TypedDict, total=False):
    id: Required[Literal["mp4_av1"]]
    """Id specifies the output format."""

    audio_bitrate: int
    """AudioBitrate specifies the output audio bitrate in bits per second.

    Defaults to 128000.
    """

    audio_samplerate: Literal[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000]
    """AudioSamplerate specifies the output sample rate in Hz.

    Defaults to 48000. WebM Opus audio uses 48000.
    """

    channels: Literal[1, 2, 6, 8]
    """Channels specifies the output channel count.

    Defaults to stereo. Six channels means 5.1; eight means 7.1.
    """

    crf: int
    """
    Crf (Constant Rate Factor) controls the quality of the output video. Lower
    values mean better quality but larger file size. Range: 16 to 63. Recommended
    values: 16-35 for high quality, 35-45 for good quality, 45-63 for acceptable
    quality.
    """

    duration: float
    """Duration specifies the requested output length in seconds.

    Defaults to the remaining source duration and is capped at the source end.
    Audio-only output must resolve to at least 0.001 seconds after trimming and
    sample rounding. The accepted interval determines the fixed price.
    """

    level: Literal[30, 31, 41]
    """
    Level specifies the AV1 level using its two-digit representation, such as 31 for
    level 3.1. The dimensions, frame rate and rate controls must fit this level.
    Omitted rate limits resolve to level-compatible defaults.
    """

    movflags: Literal["faststart"]
    """Movflags specifies MP4 packaging.

    Defaults to faststart, which places playback metadata before the media.
    """

    pixfmt: Literal["yuv420p", "yuv420p10le"]
    """Pixfmt specifies the output pixel format.

    Defaults to yuv420p. The selected profile must support it.
    """

    preset: Literal["6", "7", "8", "9", "10", "11", "12", "13"]
    """Preset controls the encoding efficiency and processing intensity.

    Lower presets use more optimization features, creating smaller files with better
    quality but requiring more compute time. Higher presets encode faster but
    produce larger files.

    Preset ranges:

    - 6-7: Fast encoding for real-time applications (smaller files)
    - 8-10: Balanced efficiency and speed for general use
    - 11-13: Fastest encoding for real-time applications (larger files)
    """

    profilev: Literal["main"]
    """Profilev selects the AV1 Main profile.

    Use pixfmt to select 8-bit or 10-bit output.
    """

    seek: float
    """Seek specifies the start in source seconds.

    Defaults to zero and must precede the source end. The accepted interval uses the
    output frame or sample timeline. Audio-only output must retain at least 0.001
    seconds after sample rounding.
    """


class FormatWebmVp9(TypedDict, total=False):
    id: Required[Literal["webm_vp9"]]
    """Id specifies the output format."""

    audio_bitrate: int
    """AudioBitrate specifies the output audio bitrate in bits per second.

    Defaults to 128000.
    """

    audio_samplerate: Literal[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000]
    """AudioSamplerate specifies the output sample rate in Hz.

    Defaults to 48000. WebM Opus audio uses 48000.
    """

    channels: Literal[1, 2, 6, 8]
    """Channels specifies the output channel count.

    Defaults to stereo. Six channels means 5.1; eight means 7.1.
    """

    cpu_used: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    """CpuUsed specifies the CPU usage level for VP9 encoding.

    Range: 0 to 8. Lower values mean better quality but slower encoding, higher
    values mean faster encoding but lower quality. Recommended values: 0-2 for high
    quality, 2-4 for good quality, 4-6 for balanced, 6-8 for speed
    """

    crf: int
    """
    Crf (Constant Rate Factor) controls the quality of the output video. Lower
    values mean better quality but larger file size. Range: 15 to 35. Recommended
    values: 18-28 for high quality, 23-28 for good quality, 28-35 for acceptable
    quality.
    """

    duration: float
    """Duration specifies the requested output length in seconds.

    Defaults to the remaining source duration and is capped at the source end.
    Audio-only output must resolve to at least 0.001 seconds after trimming and
    sample rounding. The accepted interval determines the fixed price.
    """

    minrate: int
    """Minrate selects VP9 constant bitrate when equal to video_bitrate and maxrate.

    Other minimum-rate combinations are unsupported.
    """

    pixfmt: Literal[
        "yuv420p",
        "yuv422p",
        "yuv440p",
        "yuv444p",
        "yuv420p10le",
        "yuv422p10le",
        "yuv440p10le",
        "yuv444p10le",
        "yuv420p12le",
        "yuv422p12le",
        "yuv440p12le",
        "yuv444p12le",
    ]
    """Pixfmt specifies the output pixel format.

    Defaults to yuv420p. The selected profile must support it.
    """

    quality: Literal["good", "best", "realtime"]
    """Quality specifies the VP9 encoding quality preset. Valid values:

    - good: Balanced quality preset, good for most applications
    - best: Best quality preset, slower encoding
    - realtime: Fast encoding preset, suitable for live streaming
    """

    seek: float
    """Seek specifies the start in source seconds.

    Defaults to zero and must precede the source end. The accepted interval uses the
    output frame or sample timeline. Audio-only output must retain at least 0.001
    seconds after sample rounding.
    """


class FormatM4aAac(TypedDict, total=False):
    id: Required[Literal["m4a_aac"]]
    """Id specifies an AAC M4A export."""

    audio_bitrate: int
    """AudioBitrate specifies the output audio bitrate in bits per second.

    Defaults to 128000.
    """

    audio_samplerate: Literal[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000]
    """AudioSamplerate specifies the output sample rate in Hz.

    Defaults to 48000. WebM Opus audio uses 48000.
    """

    channels: Literal[1, 2, 6, 8]
    """Channels specifies the output channel count.

    Defaults to stereo. Six channels means 5.1; eight means 7.1.
    """

    duration: float
    """Duration specifies the requested output length in seconds.

    Defaults to the remaining source duration and is capped at the source end.
    Audio-only output must resolve to at least 0.001 seconds after trimming and
    sample rounding. The accepted interval determines the fixed price.
    """

    seek: float
    """Seek specifies the start in source seconds.

    Defaults to zero and must precede the source end. The accepted interval uses the
    output frame or sample timeline. Audio-only output must retain at least 0.001
    seconds after sample rounding.
    """


Format: TypeAlias = Union[FormatMP4H264, FormatMP4H265, FormatMP4Av1, FormatWebmVp9, FormatM4aAac]


class Storage(TypedDict, total=False):
    """Storage overrides the Project output destination.

    Source storage remains independent.
    """

    id: str
    """Id specifies a Storage in this Project. Defaults to the Project output storage."""

    path: str
    """
    Path specifies the output object path relative to the selected Storage
    base_prefix. Required for customer storage; generated for Chunkify temporary
    storage. The extension must match the resolved output format. The combined path
    may contain at most 1024 bytes.
    """
