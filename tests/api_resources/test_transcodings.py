# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from chunkify import Chunkify, AsyncChunkify
from tests.utils import assert_matches_type
from chunkify.types import (
    Transcoding,
)
from chunkify.pagination import SyncPaginatedResults, AsyncPaginatedResults

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranscodings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Chunkify) -> None:
        transcoding = client.transcodings.create(
            format={"id": "mp4_h264"},
            source_id="src_example",
        )
        assert_matches_type(Transcoding, transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Chunkify) -> None:
        transcoding = client.transcodings.create(
            format={
                "id": "mp4_h264",
                "audio_bitrate": 32000,
                "audio_samplerate": 8000,
                "bufsize": 100000,
                "channels": 1,
                "crf": 23,
                "disable_audio": True,
                "disable_video": True,
                "duration": 1,
                "framerate": 0.001,
                "gop": 1,
                "height": 720,
                "level": 41,
                "maxrate": 100000,
                "movflags": "faststart",
                "per_title": True,
                "pixfmt": "yuv420p",
                "preset": "medium",
                "profilev": "high",
                "seek": 0,
                "video_bitrate": 1000,
                "width": -2,
                "x264_keyint": 60,
            },
            source_id="src_example",
            metadata={"foo": "string"},
            storage={
                "id": "stor_example",
                "path": "exports/video.mp4",
            },
        )
        assert_matches_type(Transcoding, transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Chunkify) -> None:
        response = client.transcodings.with_raw_response.create(
            format={"id": "mp4_h264"},
            source_id="src_example",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcoding = response.parse()
        assert_matches_type(Transcoding, transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Chunkify) -> None:
        with client.transcodings.with_streaming_response.create(
            format={"id": "mp4_h264"},
            source_id="src_example",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcoding = response.parse()
            assert_matches_type(Transcoding, transcoding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Chunkify) -> None:
        transcoding = client.transcodings.retrieve(
            "transcodingId",
        )
        assert_matches_type(Transcoding, transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Chunkify) -> None:
        response = client.transcodings.with_raw_response.retrieve(
            "transcodingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcoding = response.parse()
        assert_matches_type(Transcoding, transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Chunkify) -> None:
        with client.transcodings.with_streaming_response.retrieve(
            "transcodingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcoding = response.parse()
            assert_matches_type(Transcoding, transcoding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcoding_id` but received ''"):
            client.transcodings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Chunkify) -> None:
        transcoding = client.transcodings.list()
        assert_matches_type(SyncPaginatedResults[Transcoding], transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Chunkify) -> None:
        transcoding = client.transcodings.list(
            id="x",
            created={
                "gte": 0,
                "lte": 0,
                "sort": "asc",
            },
            limit=1,
            offset=0,
            source_id="x",
            status="preparing",
            storage_id="x",
        )
        assert_matches_type(SyncPaginatedResults[Transcoding], transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Chunkify) -> None:
        response = client.transcodings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcoding = response.parse()
        assert_matches_type(SyncPaginatedResults[Transcoding], transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Chunkify) -> None:
        with client.transcodings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcoding = response.parse()
            assert_matches_type(SyncPaginatedResults[Transcoding], transcoding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Chunkify) -> None:
        transcoding = client.transcodings.delete(
            transcoding_id="transcodingId",
        )
        assert transcoding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Chunkify) -> None:
        transcoding = client.transcodings.delete(
            transcoding_id="transcodingId",
            delete_files=True,
        )
        assert transcoding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Chunkify) -> None:
        response = client.transcodings.with_raw_response.delete(
            transcoding_id="transcodingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcoding = response.parse()
        assert transcoding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Chunkify) -> None:
        with client.transcodings.with_streaming_response.delete(
            transcoding_id="transcodingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcoding = response.parse()
            assert transcoding is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcoding_id` but received ''"):
            client.transcodings.with_raw_response.delete(
                transcoding_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Chunkify) -> None:
        transcoding = client.transcodings.cancel(
            "transcodingId",
        )
        assert transcoding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Chunkify) -> None:
        response = client.transcodings.with_raw_response.cancel(
            "transcodingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcoding = response.parse()
        assert transcoding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Chunkify) -> None:
        with client.transcodings.with_streaming_response.cancel(
            "transcodingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcoding = response.parse()
            assert transcoding is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcoding_id` but received ''"):
            client.transcodings.with_raw_response.cancel(
                "",
            )


class TestAsyncTranscodings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncChunkify) -> None:
        transcoding = await async_client.transcodings.create(
            format={"id": "mp4_h264"},
            source_id="src_example",
        )
        assert_matches_type(Transcoding, transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncChunkify) -> None:
        transcoding = await async_client.transcodings.create(
            format={
                "id": "mp4_h264",
                "audio_bitrate": 32000,
                "audio_samplerate": 8000,
                "bufsize": 100000,
                "channels": 1,
                "crf": 23,
                "disable_audio": True,
                "disable_video": True,
                "duration": 1,
                "framerate": 0.001,
                "gop": 1,
                "height": 720,
                "level": 41,
                "maxrate": 100000,
                "movflags": "faststart",
                "per_title": True,
                "pixfmt": "yuv420p",
                "preset": "medium",
                "profilev": "high",
                "seek": 0,
                "video_bitrate": 1000,
                "width": -2,
                "x264_keyint": 60,
            },
            source_id="src_example",
            metadata={"foo": "string"},
            storage={
                "id": "stor_example",
                "path": "exports/video.mp4",
            },
        )
        assert_matches_type(Transcoding, transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncChunkify) -> None:
        response = await async_client.transcodings.with_raw_response.create(
            format={"id": "mp4_h264"},
            source_id="src_example",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcoding = await response.parse()
        assert_matches_type(Transcoding, transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncChunkify) -> None:
        async with async_client.transcodings.with_streaming_response.create(
            format={"id": "mp4_h264"},
            source_id="src_example",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcoding = await response.parse()
            assert_matches_type(Transcoding, transcoding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncChunkify) -> None:
        transcoding = await async_client.transcodings.retrieve(
            "transcodingId",
        )
        assert_matches_type(Transcoding, transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncChunkify) -> None:
        response = await async_client.transcodings.with_raw_response.retrieve(
            "transcodingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcoding = await response.parse()
        assert_matches_type(Transcoding, transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncChunkify) -> None:
        async with async_client.transcodings.with_streaming_response.retrieve(
            "transcodingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcoding = await response.parse()
            assert_matches_type(Transcoding, transcoding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcoding_id` but received ''"):
            await async_client.transcodings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncChunkify) -> None:
        transcoding = await async_client.transcodings.list()
        assert_matches_type(AsyncPaginatedResults[Transcoding], transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncChunkify) -> None:
        transcoding = await async_client.transcodings.list(
            id="x",
            created={
                "gte": 0,
                "lte": 0,
                "sort": "asc",
            },
            limit=1,
            offset=0,
            source_id="x",
            status="preparing",
            storage_id="x",
        )
        assert_matches_type(AsyncPaginatedResults[Transcoding], transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncChunkify) -> None:
        response = await async_client.transcodings.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcoding = await response.parse()
        assert_matches_type(AsyncPaginatedResults[Transcoding], transcoding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncChunkify) -> None:
        async with async_client.transcodings.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcoding = await response.parse()
            assert_matches_type(AsyncPaginatedResults[Transcoding], transcoding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncChunkify) -> None:
        transcoding = await async_client.transcodings.delete(
            transcoding_id="transcodingId",
        )
        assert transcoding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncChunkify) -> None:
        transcoding = await async_client.transcodings.delete(
            transcoding_id="transcodingId",
            delete_files=True,
        )
        assert transcoding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncChunkify) -> None:
        response = await async_client.transcodings.with_raw_response.delete(
            transcoding_id="transcodingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcoding = await response.parse()
        assert transcoding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncChunkify) -> None:
        async with async_client.transcodings.with_streaming_response.delete(
            transcoding_id="transcodingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcoding = await response.parse()
            assert transcoding is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcoding_id` but received ''"):
            await async_client.transcodings.with_raw_response.delete(
                transcoding_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncChunkify) -> None:
        transcoding = await async_client.transcodings.cancel(
            "transcodingId",
        )
        assert transcoding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncChunkify) -> None:
        response = await async_client.transcodings.with_raw_response.cancel(
            "transcodingId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transcoding = await response.parse()
        assert transcoding is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncChunkify) -> None:
        async with async_client.transcodings.with_streaming_response.cancel(
            "transcodingId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transcoding = await response.parse()
            assert transcoding is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transcoding_id` but received ''"):
            await async_client.transcodings.with_raw_response.cancel(
                "",
            )
