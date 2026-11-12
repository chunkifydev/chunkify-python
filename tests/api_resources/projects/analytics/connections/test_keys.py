# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from chunkify import Chunkify, AsyncChunkify
from tests.utils import assert_matches_type
from chunkify.types.projects.analytics.connections import (
    KeyListResponse,
    KeyCreateResponse,
    KeyRotateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Chunkify) -> None:
        key = client.projects.analytics.connections.keys.create(
            project_id="projectId",
            connection_id="connectionId",
            purpose="player",
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Chunkify) -> None:
        response = client.projects.analytics.connections.keys.with_raw_response.create(
            project_id="projectId",
            connection_id="connectionId",
            purpose="player",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Chunkify) -> None:
        with client.projects.analytics.connections.keys.with_streaming_response.create(
            project_id="projectId",
            connection_id="connectionId",
            purpose="player",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyCreateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics.connections.keys.with_raw_response.create(
                project_id="",
                connection_id="connectionId",
                purpose="player",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.projects.analytics.connections.keys.with_raw_response.create(
                project_id="projectId",
                connection_id="",
                purpose="player",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Chunkify) -> None:
        key = client.projects.analytics.connections.keys.list(
            project_id="projectId",
            connection_id="connectionId",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Chunkify) -> None:
        response = client.projects.analytics.connections.keys.with_raw_response.list(
            project_id="projectId",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Chunkify) -> None:
        with client.projects.analytics.connections.keys.with_streaming_response.list(
            project_id="projectId",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics.connections.keys.with_raw_response.list(
                project_id="",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.projects.analytics.connections.keys.with_raw_response.list(
                project_id="projectId",
                connection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate(self, client: Chunkify) -> None:
        key = client.projects.analytics.connections.keys.rotate(
            project_id="projectId",
            connection_id="connectionId",
            key_id="keyId",
        )
        assert_matches_type(KeyRotateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rotate(self, client: Chunkify) -> None:
        response = client.projects.analytics.connections.keys.with_raw_response.rotate(
            project_id="projectId",
            connection_id="connectionId",
            key_id="keyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyRotateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rotate(self, client: Chunkify) -> None:
        with client.projects.analytics.connections.keys.with_streaming_response.rotate(
            project_id="projectId",
            connection_id="connectionId",
            key_id="keyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyRotateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rotate(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics.connections.keys.with_raw_response.rotate(
                project_id="",
                connection_id="connectionId",
                key_id="keyId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.projects.analytics.connections.keys.with_raw_response.rotate(
                project_id="projectId",
                connection_id="",
                key_id="keyId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            client.projects.analytics.connections.keys.with_raw_response.rotate(
                project_id="projectId",
                connection_id="connectionId",
                key_id="",
            )


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncChunkify) -> None:
        key = await async_client.projects.analytics.connections.keys.create(
            project_id="projectId",
            connection_id="connectionId",
            purpose="player",
        )
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics.connections.keys.with_raw_response.create(
            project_id="projectId",
            connection_id="connectionId",
            purpose="player",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyCreateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics.connections.keys.with_streaming_response.create(
            project_id="projectId",
            connection_id="connectionId",
            purpose="player",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyCreateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics.connections.keys.with_raw_response.create(
                project_id="",
                connection_id="connectionId",
                purpose="player",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.projects.analytics.connections.keys.with_raw_response.create(
                project_id="projectId",
                connection_id="",
                purpose="player",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncChunkify) -> None:
        key = await async_client.projects.analytics.connections.keys.list(
            project_id="projectId",
            connection_id="connectionId",
        )
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics.connections.keys.with_raw_response.list(
            project_id="projectId",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyListResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics.connections.keys.with_streaming_response.list(
            project_id="projectId",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyListResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics.connections.keys.with_raw_response.list(
                project_id="",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.projects.analytics.connections.keys.with_raw_response.list(
                project_id="projectId",
                connection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate(self, async_client: AsyncChunkify) -> None:
        key = await async_client.projects.analytics.connections.keys.rotate(
            project_id="projectId",
            connection_id="connectionId",
            key_id="keyId",
        )
        assert_matches_type(KeyRotateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rotate(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics.connections.keys.with_raw_response.rotate(
            project_id="projectId",
            connection_id="connectionId",
            key_id="keyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyRotateResponse, key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rotate(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics.connections.keys.with_streaming_response.rotate(
            project_id="projectId",
            connection_id="connectionId",
            key_id="keyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyRotateResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rotate(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics.connections.keys.with_raw_response.rotate(
                project_id="",
                connection_id="connectionId",
                key_id="keyId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.projects.analytics.connections.keys.with_raw_response.rotate(
                project_id="projectId",
                connection_id="",
                key_id="keyId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_id` but received ''"):
            await async_client.projects.analytics.connections.keys.with_raw_response.rotate(
                project_id="projectId",
                connection_id="connectionId",
                key_id="",
            )
