# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TranscodingWebmVp9Param"]


class TranscodingWebmVp9Param(TypedDict, total=False):
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

    bufsize: int
    """Bufsize specifies the video buffer size in bits, from 100000 through 50000000.

    H.264 and H.265 require maxrate. AV1 and VP9 require a bitrate-controlled mode.
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

    disable_audio: bool
    """DisableAudio omits the audio stream.

    Defaults to false. A source without audio produces video only.
    """

    disable_video: bool
    """DisableVideo selects an audio-only AAC M4A export.

    Defaults to false. The source must contain audio.
    """

    duration: float
    """Duration specifies the requested output length in seconds.

    Defaults to the remaining source duration and is capped at the source end.
    Audio-only output must resolve to at least 0.001 seconds after trimming and
    sample rounding. The accepted interval determines the fixed price.
    """

    framerate: float
    """Framerate specifies the output video frame rate.

    Defaults to the source rate and must be between 0.001 and 240 fps.
    """

    gop: int
    """Gop specifies the maximum keyframe interval in frames.

    Defaults to four seconds at the accepted frame rate, capped at 960 frames.
    """

    height: int
    """Height specifies the output dimension in pixels.

    Use -2 or omit one dimension to preserve the source aspect ratio. Explicit
    dimensions must be 2 to 7680 and even. Omitting both preserves the source
    dimensions rounded down to even pixels.
    """

    maxrate: int
    """
    Maxrate specifies the video buffer maximum rate in bits per second, from 100000
    through 50000000. H.264 and H.265 require bufsize. VP9 requires video_bitrate;
    AV1 requires CRF mode.
    """

    minrate: int
    """Minrate selects VP9 constant bitrate when equal to video_bitrate and maxrate.

    Other minimum-rate combinations are unsupported.
    """

    per_title: bool
    """
    PerTitle enables independent content-based bitrate prediction for each part of
    the video. Analysis uses only the selected trim interval. Defaults to false.
    Explicit rate-control settings cannot be combined with it.
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

    video_bitrate: int
    """
    VideoBitrate specifies the target video bitrate in bits per second, from 1000
    through 100000000. Omit it for CRF or per-title encoding.
    """

    width: int
    """Width specifies the output dimension in pixels.

    Use -2 or omit one dimension to preserve the source aspect ratio. Explicit
    dimensions must be 2 to 7680 and even. Omitting both preserves the source
    dimensions rounded down to even pixels.
    """
