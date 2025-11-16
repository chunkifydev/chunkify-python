# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "JobCreateParams",
    "Format",
    "FormatHlsAv1",
    "FormatHlsH264",
    "FormatHlsH265",
    "FormatJpg",
    "FormatMP4Av1",
    "FormatMP4H264",
    "FormatMP4H265",
    "FormatWebmVp9",
    "Storage",
    "Transcoder",
]


class JobCreateParams(TypedDict, total=False):
    format: Required[Format]
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
    """Optional metadata to attach to the job (max 1024 bytes)"""

    storage: Storage
    """Optional storage configuration"""

    transcoder: Transcoder
    """Optional transcoder configuration.

    If not provided, the system will automatically calculate the optimal quantity
    and CPU type based on the source file specifications and output requirements.
    This auto-scaling ensures efficient resource utilization.
    """


class FormatHlsAv1(TypedDict, total=False):
    audio_bitrate: int
    """
    AudioBitrate specifies the audio bitrate in bits per second. Must be between
    32Kbps and 512Kbps.
    """

    bufsize: int
    """
    Bufsize specifies the video buffer size in bits. Must be between 100Kbps and
    50Mbps.
    """

    channels: Literal[1, 2, 5, 7]
    """
    Channels specifies the number of audio channels. Valid values: 1 (mono), 2
    (stereo), 5 (5.1), 7 (7.1)
    """

    crf: int
    """
    Crf (Constant Rate Factor) controls the quality of the output video. Lower
    values mean better quality but larger file size. Range: 16 to 63. Recommended
    values: 16-35 for high quality, 35-45 for good quality, 45-63 for acceptable
    quality.
    """

    disable_audio: bool
    """DisableAudio indicates whether to disable audio processing."""

    disable_video: bool
    """DisableVideo indicates whether to disable video processing."""

    duration: int
    """
    Duration specifies the duration to process in seconds. Must be a positive value.
    """

    framerate: float
    """
    Framerate specifies the output video frame rate. Must be between 15 and 120 fps.
    """

    gop: int
    """Gop specifies the Group of Pictures (GOP) size. Must be between 1 and 300."""

    height: int
    """Height specifies the output video height in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """

    hls_enc: bool
    """HlsEnc enables encryption for HLS segments when set to true."""

    hls_enc_iv: str
    """HlsEncIv specifies the initialization vector for encryption.

    Maximum length: 64 characters. Required when HlsEnc is true.
    """

    hls_enc_key: str
    """HlsEncKey specifies the encryption key for HLS segments.

    Maximum length: 64 characters. Required when HlsEnc is true.
    """

    hls_enc_key_url: str
    """
    HlsEncKeyUrl specifies the URL where clients can fetch the encryption key.
    Required when HlsEnc is true.
    """

    hls_segment_type: Literal["mpegts", "fmp4"]
    """HlsSegmentType specifies the type of HLS segments. Valid values:

    - mpegts: Traditional MPEG-TS segments, better compatibility
    - fmp4: Fragmented MP4 segments, better efficiency
    """

    hls_time: int
    """HlsTime specifies the duration of each HLS segment in seconds.

    Range: 1 to 10. Shorter segments provide faster startup but more overhead,
    longer segments are more efficient.
    """

    level: Literal[30, 31, 41]
    """Level specifies the AV1 profile level.

    Valid values: 30-31 (main), 41 (main10). Higher levels support higher
    resolutions and bitrates but require more processing power.
    """

    maxrate: int
    """
    Maxrate specifies the maximum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    minrate: int
    """
    Minrate specifies the minimum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    movflags: str

    pixfmt: Literal[
        "yuv410p",
        "yuv411p",
        "yuv420p",
        "yuv422p",
        "yuv440p",
        "yuv444p",
        "yuvJ411p",
        "yuvJ420p",
        "yuvJ422p",
        "yuvJ440p",
        "yuvJ444p",
        "yuv420p10le",
        "yuv422p10le",
        "yuv440p10le",
        "yuv444p10le",
        "yuv420p12le",
        "yuv422p12le",
        "yuv440p12le",
        "yuv444p12le",
        "yuv420p10be",
        "yuv422p10be",
        "yuv440p10be",
        "yuv444p10be",
        "yuv420p12be",
        "yuv422p12be",
        "yuv440p12be",
        "yuv444p12be",
    ]
    """PixFmt specifies the pixel format. Valid value: yuv420p"""

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

    profilev: Literal["main", "main10", "mainstillpicture"]
    """Profilev specifies the AV1 profile. Valid values:

    - main: Main profile, good for most applications
    - main10: Main 10-bit profile, supports 10-bit color
    - mainstillpicture: Still picture profile, optimized for single images
    """

    seek: int
    """
    Seek specifies the timestamp to start processing from (in seconds). Must be a
    positive value.
    """

    video_bitrate: int
    """
    VideoBitrate specifies the video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    width: int
    """Width specifies the output video width in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """


class FormatHlsH264(TypedDict, total=False):
    audio_bitrate: int
    """
    AudioBitrate specifies the audio bitrate in bits per second. Must be between
    32Kbps and 512Kbps.
    """

    bufsize: int
    """
    Bufsize specifies the video buffer size in bits. Must be between 100Kbps and
    50Mbps.
    """

    channels: Literal[1, 2, 5, 7]
    """
    Channels specifies the number of audio channels. Valid values: 1 (mono), 2
    (stereo), 5 (5.1), 7 (7.1)
    """

    crf: int
    """
    Crf (Constant Rate Factor) controls the quality of the output video. Lower
    values mean better quality but larger file size. Range: 16 to 35. Recommended
    values: 18-28 for high quality, 23-28 for good quality, 28-35 for acceptable
    quality.
    """

    disable_audio: bool
    """DisableAudio indicates whether to disable audio processing."""

    disable_video: bool
    """DisableVideo indicates whether to disable video processing."""

    duration: int
    """
    Duration specifies the duration to process in seconds. Must be a positive value.
    """

    framerate: float
    """
    Framerate specifies the output video frame rate. Must be between 15 and 120 fps.
    """

    gop: int
    """Gop specifies the Group of Pictures (GOP) size. Must be between 1 and 300."""

    height: int
    """Height specifies the output video height in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """

    hls_enc: bool
    """HlsEnc enables encryption for HLS segments when set to true."""

    hls_enc_iv: str
    """HlsEncIv specifies the initialization vector for encryption.

    Maximum length: 64 characters. Required when HlsEnc is true.
    """

    hls_enc_key: str
    """HlsEncKey specifies the encryption key for HLS segments.

    Maximum length: 64 characters. Required when HlsEnc is true.
    """

    hls_enc_key_url: str
    """
    HlsEncKeyUrl specifies the URL where clients can fetch the encryption key.
    Required when HlsEnc is true.
    """

    hls_segment_type: Literal["mpegts", "fmp4"]
    """HlsSegmentType specifies the type of HLS segments. Valid values:

    - mpegts: Traditional MPEG-TS segments, better compatibility
    - fmp4: Fragmented MP4 segments, better efficiency
    """

    hls_time: int
    """HlsTime specifies the duration of each HLS segment in seconds.

    Range: 1 to 10. Shorter segments provide faster startup but more overhead,
    longer segments are more efficient.
    """

    level: Literal[10, 11, 12, 13, 20, 21, 22, 30, 31, 32, 40, 41, 42, 50, 51]
    """Level specifies the H.264 profile level.

    Valid values: 10-13 (baseline), 20-22 (main), 30-32 (high), 40-42 (high), 50-51
    (high). Higher levels support higher resolutions and bitrates but require more
    processing power.
    """

    maxrate: int
    """
    Maxrate specifies the maximum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    minrate: int
    """
    Minrate specifies the minimum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    movflags: str

    pixfmt: Literal[
        "yuv410p",
        "yuv411p",
        "yuv420p",
        "yuv422p",
        "yuv440p",
        "yuv444p",
        "yuvJ411p",
        "yuvJ420p",
        "yuvJ422p",
        "yuvJ440p",
        "yuvJ444p",
        "yuv420p10le",
        "yuv422p10le",
        "yuv440p10le",
        "yuv444p10le",
        "yuv420p12le",
        "yuv422p12le",
        "yuv440p12le",
        "yuv444p12le",
        "yuv420p10be",
        "yuv422p10be",
        "yuv440p10be",
        "yuv444p10be",
        "yuv420p12be",
        "yuv422p12be",
        "yuv440p12be",
        "yuv444p12be",
    ]
    """PixFmt specifies the pixel format. Valid value: yuv420p"""

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

    seek: int
    """
    Seek specifies the timestamp to start processing from (in seconds). Must be a
    positive value.
    """

    video_bitrate: int
    """
    VideoBitrate specifies the video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    width: int
    """Width specifies the output video width in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """

    x264_keyint: int
    """
    X264KeyInt specifies the maximum number of frames between keyframes for H.264
    encoding. Range: 1 to 300. Higher values can improve compression but may affect
    seeking.
    """


class FormatHlsH265(TypedDict, total=False):
    audio_bitrate: int
    """
    AudioBitrate specifies the audio bitrate in bits per second. Must be between
    32Kbps and 512Kbps.
    """

    bufsize: int
    """
    Bufsize specifies the video buffer size in bits. Must be between 100Kbps and
    50Mbps.
    """

    channels: Literal[1, 2, 5, 7]
    """
    Channels specifies the number of audio channels. Valid values: 1 (mono), 2
    (stereo), 5 (5.1), 7 (7.1)
    """

    crf: int
    """
    Crf (Constant Rate Factor) controls the quality of the output video. Lower
    values mean better quality but larger file size. Range: 16 to 35. Recommended
    values: 18-28 for high quality, 23-28 for good quality, 28-35 for acceptable
    quality.
    """

    disable_audio: bool
    """DisableAudio indicates whether to disable audio processing."""

    disable_video: bool
    """DisableVideo indicates whether to disable video processing."""

    duration: int
    """
    Duration specifies the duration to process in seconds. Must be a positive value.
    """

    framerate: float
    """
    Framerate specifies the output video frame rate. Must be between 15 and 120 fps.
    """

    gop: int
    """Gop specifies the Group of Pictures (GOP) size. Must be between 1 and 300."""

    height: int
    """Height specifies the output video height in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """

    hls_enc: bool
    """HlsEnc enables encryption for HLS segments when set to true."""

    hls_enc_iv: str
    """HlsEncIv specifies the initialization vector for encryption.

    Maximum length: 64 characters. Required when HlsEnc is true.
    """

    hls_enc_key: str
    """HlsEncKey specifies the encryption key for HLS segments.

    Maximum length: 64 characters. Required when HlsEnc is true.
    """

    hls_enc_key_url: str
    """
    HlsEncKeyUrl specifies the URL where clients can fetch the encryption key.
    Required when HlsEnc is true.
    """

    hls_segment_type: Literal["mpegts", "fmp4"]
    """HlsSegmentType specifies the type of HLS segments. Valid values:

    - mpegts: Traditional MPEG-TS segments, better compatibility
    - fmp4: Fragmented MP4 segments, better efficiency
    """

    hls_time: int
    """HlsTime specifies the duration of each HLS segment in seconds.

    Range: 1 to 10. Shorter segments provide faster startup but more overhead,
    longer segments are more efficient.
    """

    level: Literal[30, 31, 41]
    """Level specifies the H.265 profile level.

    Valid values: 30-31 (main), 41 (main10). Higher levels support higher
    resolutions and bitrates but require more processing power.
    """

    maxrate: int
    """
    Maxrate specifies the maximum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    minrate: int
    """
    Minrate specifies the minimum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    movflags: str

    pixfmt: Literal[
        "yuv410p",
        "yuv411p",
        "yuv420p",
        "yuv422p",
        "yuv440p",
        "yuv444p",
        "yuvJ411p",
        "yuvJ420p",
        "yuvJ422p",
        "yuvJ440p",
        "yuvJ444p",
        "yuv420p10le",
        "yuv422p10le",
        "yuv440p10le",
        "yuv444p10le",
        "yuv420p12le",
        "yuv422p12le",
        "yuv440p12le",
        "yuv444p12le",
        "yuv420p10be",
        "yuv422p10be",
        "yuv440p10be",
        "yuv444p10be",
        "yuv420p12be",
        "yuv422p12be",
        "yuv440p12be",
        "yuv444p12be",
    ]
    """PixFmt specifies the pixel format. Valid value: yuv420p"""

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

    profilev: Literal["main", "main10", "mainstillpicture"]
    """Profilev specifies the H.265 profile. Valid values:

    - main: Main profile, good for most applications
    - main10: Main 10-bit profile, supports 10-bit color
    - mainstillpicture: Still picture profile, optimized for single images
    """

    seek: int
    """
    Seek specifies the timestamp to start processing from (in seconds). Must be a
    positive value.
    """

    video_bitrate: int
    """
    VideoBitrate specifies the video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    width: int
    """Width specifies the output video width in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """

    x265_keyint: int
    """
    X265KeyInt specifies the maximum number of frames between keyframes for H.265
    encoding. Range: 1 to 300. Higher values can improve compression but may affect
    seeking.
    """


class FormatJpg(TypedDict, total=False):
    interval: Required[int]
    """
    Time interval in seconds at which frames are extracted from the video (e.g.,
    interval=10 extracts frames at 0s, 10s, 20s, etc.). Must be between 1 and 60
    seconds.
    """

    chunk_duration: int

    duration: int
    """
    Duration specifies the duration to process in seconds. Must be a positive value.
    """

    frames: int

    height: int

    seek: int
    """
    Seek specifies the timestamp to start processing from (in seconds). Must be a
    positive value.
    """

    sprite: bool

    width: int


class FormatMP4Av1(TypedDict, total=False):
    audio_bitrate: int
    """
    AudioBitrate specifies the audio bitrate in bits per second. Must be between
    32Kbps and 512Kbps.
    """

    bufsize: int
    """
    Bufsize specifies the video buffer size in bits. Must be between 100Kbps and
    50Mbps.
    """

    channels: Literal[1, 2, 5, 7]
    """
    Channels specifies the number of audio channels. Valid values: 1 (mono), 2
    (stereo), 5 (5.1), 7 (7.1)
    """

    crf: int
    """
    Crf (Constant Rate Factor) controls the quality of the output video. Lower
    values mean better quality but larger file size. Range: 16 to 63. Recommended
    values: 16-35 for high quality, 35-45 for good quality, 45-63 for acceptable
    quality.
    """

    disable_audio: bool
    """DisableAudio indicates whether to disable audio processing."""

    disable_video: bool
    """DisableVideo indicates whether to disable video processing."""

    duration: int
    """
    Duration specifies the duration to process in seconds. Must be a positive value.
    """

    framerate: float
    """
    Framerate specifies the output video frame rate. Must be between 15 and 120 fps.
    """

    gop: int
    """Gop specifies the Group of Pictures (GOP) size. Must be between 1 and 300."""

    height: int
    """Height specifies the output video height in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """

    level: Literal[30, 31, 41]
    """Level specifies the AV1 profile level.

    Valid values: 30-31 (main), 41 (main10). Higher levels support higher
    resolutions and bitrates but require more processing power.
    """

    maxrate: int
    """
    Maxrate specifies the maximum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    minrate: int
    """
    Minrate specifies the minimum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    movflags: str

    pixfmt: Literal[
        "yuv410p",
        "yuv411p",
        "yuv420p",
        "yuv422p",
        "yuv440p",
        "yuv444p",
        "yuvJ411p",
        "yuvJ420p",
        "yuvJ422p",
        "yuvJ440p",
        "yuvJ444p",
        "yuv420p10le",
        "yuv422p10le",
        "yuv440p10le",
        "yuv444p10le",
        "yuv420p12le",
        "yuv422p12le",
        "yuv440p12le",
        "yuv444p12le",
        "yuv420p10be",
        "yuv422p10be",
        "yuv440p10be",
        "yuv444p10be",
        "yuv420p12be",
        "yuv422p12be",
        "yuv440p12be",
        "yuv444p12be",
    ]
    """PixFmt specifies the pixel format. Valid value: yuv420p"""

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

    profilev: Literal["main", "main10", "mainstillpicture"]
    """Profilev specifies the AV1 profile. Valid values:

    - main: Main profile, good for most applications
    - main10: Main 10-bit profile, supports 10-bit color
    - mainstillpicture: Still picture profile, optimized for single images
    """

    seek: int
    """
    Seek specifies the timestamp to start processing from (in seconds). Must be a
    positive value.
    """

    video_bitrate: int
    """
    VideoBitrate specifies the video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    width: int
    """Width specifies the output video width in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """


class FormatMP4H264(TypedDict, total=False):
    audio_bitrate: int
    """
    AudioBitrate specifies the audio bitrate in bits per second. Must be between
    32Kbps and 512Kbps.
    """

    bufsize: int
    """
    Bufsize specifies the video buffer size in bits. Must be between 100Kbps and
    50Mbps.
    """

    channels: Literal[1, 2, 5, 7]
    """
    Channels specifies the number of audio channels. Valid values: 1 (mono), 2
    (stereo), 5 (5.1), 7 (7.1)
    """

    crf: int
    """
    Crf (Constant Rate Factor) controls the quality of the output video. Lower
    values mean better quality but larger file size. Range: 16 to 35. Recommended
    values: 18-28 for high quality, 23-28 for good quality, 28-35 for acceptable
    quality.
    """

    disable_audio: bool
    """DisableAudio indicates whether to disable audio processing."""

    disable_video: bool
    """DisableVideo indicates whether to disable video processing."""

    duration: int
    """
    Duration specifies the duration to process in seconds. Must be a positive value.
    """

    framerate: float
    """
    Framerate specifies the output video frame rate. Must be between 15 and 120 fps.
    """

    gop: int
    """Gop specifies the Group of Pictures (GOP) size. Must be between 1 and 300."""

    height: int
    """Height specifies the output video height in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """

    level: Literal[10, 11, 12, 13, 20, 21, 22, 30, 31, 32, 40, 41, 42, 50, 51]
    """Level specifies the H.264 profile level.

    Valid values: 10-13 (baseline), 20-22 (main), 30-32 (high), 40-42 (high), 50-51
    (high). Higher levels support higher resolutions and bitrates but require more
    processing power.
    """

    maxrate: int
    """
    Maxrate specifies the maximum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    minrate: int
    """
    Minrate specifies the minimum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    movflags: str

    pixfmt: Literal[
        "yuv410p",
        "yuv411p",
        "yuv420p",
        "yuv422p",
        "yuv440p",
        "yuv444p",
        "yuvJ411p",
        "yuvJ420p",
        "yuvJ422p",
        "yuvJ440p",
        "yuvJ444p",
        "yuv420p10le",
        "yuv422p10le",
        "yuv440p10le",
        "yuv444p10le",
        "yuv420p12le",
        "yuv422p12le",
        "yuv440p12le",
        "yuv444p12le",
        "yuv420p10be",
        "yuv422p10be",
        "yuv440p10be",
        "yuv444p10be",
        "yuv420p12be",
        "yuv422p12be",
        "yuv440p12be",
        "yuv444p12be",
    ]
    """PixFmt specifies the pixel format. Valid value: yuv420p"""

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

    seek: int
    """
    Seek specifies the timestamp to start processing from (in seconds). Must be a
    positive value.
    """

    video_bitrate: int
    """
    VideoBitrate specifies the video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    width: int
    """Width specifies the output video width in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """

    x264_keyint: int
    """
    X264KeyInt specifies the maximum number of frames between keyframes for H.264
    encoding. Range: 1 to 300. Higher values can improve compression but may affect
    seeking.
    """


class FormatMP4H265(TypedDict, total=False):
    audio_bitrate: int
    """
    AudioBitrate specifies the audio bitrate in bits per second. Must be between
    32Kbps and 512Kbps.
    """

    bufsize: int
    """
    Bufsize specifies the video buffer size in bits. Must be between 100Kbps and
    50Mbps.
    """

    channels: Literal[1, 2, 5, 7]
    """
    Channels specifies the number of audio channels. Valid values: 1 (mono), 2
    (stereo), 5 (5.1), 7 (7.1)
    """

    crf: int
    """
    Crf (Constant Rate Factor) controls the quality of the output video. Lower
    values mean better quality but larger file size. Range: 16 to 35. Recommended
    values: 18-28 for high quality, 23-28 for good quality, 28-35 for acceptable
    quality.
    """

    disable_audio: bool
    """DisableAudio indicates whether to disable audio processing."""

    disable_video: bool
    """DisableVideo indicates whether to disable video processing."""

    duration: int
    """
    Duration specifies the duration to process in seconds. Must be a positive value.
    """

    framerate: float
    """
    Framerate specifies the output video frame rate. Must be between 15 and 120 fps.
    """

    gop: int
    """Gop specifies the Group of Pictures (GOP) size. Must be between 1 and 300."""

    height: int
    """Height specifies the output video height in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """

    level: Literal[30, 31, 41]
    """Level specifies the H.265 profile level.

    Valid values: 30-31 (main), 41 (main10). Higher levels support higher
    resolutions and bitrates but require more processing power.
    """

    maxrate: int
    """
    Maxrate specifies the maximum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    minrate: int
    """
    Minrate specifies the minimum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    movflags: str

    pixfmt: Literal[
        "yuv410p",
        "yuv411p",
        "yuv420p",
        "yuv422p",
        "yuv440p",
        "yuv444p",
        "yuvJ411p",
        "yuvJ420p",
        "yuvJ422p",
        "yuvJ440p",
        "yuvJ444p",
        "yuv420p10le",
        "yuv422p10le",
        "yuv440p10le",
        "yuv444p10le",
        "yuv420p12le",
        "yuv422p12le",
        "yuv440p12le",
        "yuv444p12le",
        "yuv420p10be",
        "yuv422p10be",
        "yuv440p10be",
        "yuv444p10be",
        "yuv420p12be",
        "yuv422p12be",
        "yuv440p12be",
        "yuv444p12be",
    ]
    """PixFmt specifies the pixel format. Valid value: yuv420p"""

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

    profilev: Literal["main", "main10", "mainstillpicture"]
    """Profilev specifies the H.265 profile. Valid values:

    - main: Main profile, good for most applications
    - main10: Main 10-bit profile, supports 10-bit color
    - mainstillpicture: Still picture profile, optimized for single images
    """

    seek: int
    """
    Seek specifies the timestamp to start processing from (in seconds). Must be a
    positive value.
    """

    video_bitrate: int
    """
    VideoBitrate specifies the video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    width: int
    """Width specifies the output video width in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """

    x265_keyint: int
    """
    X265KeyInt specifies the maximum number of frames between keyframes for H.265
    encoding. Range: 1 to 300. Higher values can improve compression but may affect
    seeking.
    """


class FormatWebmVp9(TypedDict, total=False):
    audio_bitrate: int
    """
    AudioBitrate specifies the audio bitrate in bits per second. Must be between
    32Kbps and 512Kbps.
    """

    bufsize: int
    """
    Bufsize specifies the video buffer size in bits. Must be between 100Kbps and
    50Mbps.
    """

    channels: Literal[1, 2, 5, 7]
    """
    Channels specifies the number of audio channels. Valid values: 1 (mono), 2
    (stereo), 5 (5.1), 7 (7.1)
    """

    cpu_used: str
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
    """DisableAudio indicates whether to disable audio processing."""

    disable_video: bool
    """DisableVideo indicates whether to disable video processing."""

    duration: int
    """
    Duration specifies the duration to process in seconds. Must be a positive value.
    """

    framerate: float
    """
    Framerate specifies the output video frame rate. Must be between 15 and 120 fps.
    """

    gop: int
    """Gop specifies the Group of Pictures (GOP) size. Must be between 1 and 300."""

    height: int
    """Height specifies the output video height in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """

    maxrate: int
    """
    Maxrate specifies the maximum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    minrate: int
    """
    Minrate specifies the minimum video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    pixfmt: Literal[
        "yuv410p",
        "yuv411p",
        "yuv420p",
        "yuv422p",
        "yuv440p",
        "yuv444p",
        "yuvJ411p",
        "yuvJ420p",
        "yuvJ422p",
        "yuvJ440p",
        "yuvJ444p",
        "yuv420p10le",
        "yuv422p10le",
        "yuv440p10le",
        "yuv444p10le",
        "yuv420p12le",
        "yuv422p12le",
        "yuv440p12le",
        "yuv444p12le",
        "yuv420p10be",
        "yuv422p10be",
        "yuv440p10be",
        "yuv444p10be",
        "yuv420p12be",
        "yuv422p12be",
        "yuv440p12be",
        "yuv444p12be",
    ]
    """PixFmt specifies the pixel format. Valid value: yuv420p"""

    quality: Literal["good", "best", "realtime"]
    """Quality specifies the VP9 encoding quality preset. Valid values:

    - good: Balanced quality preset, good for most applications
    - best: Best quality preset, slower encoding
    - realtime: Fast encoding preset, suitable for live streaming
    """

    seek: int
    """
    Seek specifies the timestamp to start processing from (in seconds). Must be a
    positive value.
    """

    video_bitrate: int
    """
    VideoBitrate specifies the video bitrate in bits per second. Must be between
    100Kbps and 50Mbps.
    """

    width: int
    """Width specifies the output video width in pixels. Must be between -2 and 7680.

    Use -2 for automatic calculation while maintaining aspect ratio.
    """


class Format(TypedDict, total=False):
    hls_av1: FormatHlsAv1
    """HLS AV1 configuration"""

    hls_h264: FormatHlsH264
    """HLS H264 configuration"""

    hls_h265: FormatHlsH265
    """HLS H265 configuration"""

    jpg: FormatJpg
    """FFmpeg encoding parameters specific to JPEG image extraction."""

    mp4_av1: FormatMP4Av1
    """AV1 configuration"""

    mp4_h264: FormatMP4H264
    """H264 configuration"""

    mp4_h265: FormatMP4H265
    """H265 configuration"""

    webm_vp9: FormatWebmVp9
    """VP9 configuration"""


class Storage(TypedDict, total=False):
    id: str
    """
    Storage Id specifies the storage configuration to use from pre-configured
    storage options. Must be 4-64 characters long and contain only alphanumeric
    characters, underscores and hyphens. Optional if Storage Path is provided.
    """

    path: str
    """
    Storage Path specifies a custom storage path where processed files will be
    stored. Must be a valid file path with max length of 1024 characters. Optional
    if Storage Id is provided.
    """


class Transcoder(TypedDict, total=False):
    quantity: int
    """
    Quantity specifies the number of transcoder instances to use (1-50). Required if
    Type is set.
    """

    type: Literal["4vCPU", "8vCPU", "16vCPU"]
    """
    Type specifies the CPU configuration for each transcoder instance. Required if
    Quantity is set.
    """
