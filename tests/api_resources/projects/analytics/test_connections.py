# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from chunkify import Chunkify, AsyncChunkify
from tests.utils import assert_matches_type
from chunkify.types.projects.analytics import (
    AnalyticsConnection,
    ConnectionListResponse,
    ConnectionCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Chunkify) -> None:
        connection = client.projects.analytics.connections.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Chunkify) -> None:
        connection = client.projects.analytics.connections.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
            endpoint="https://analytics.example.com",
            public_ingest_key="ck_public_de90a6057194afc9913a4adcd7ef960db1a91a48d2a13b6b2f7dfe671fd5be36",
            read_key="YOUR_READ_ONLY_KEY",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Chunkify) -> None:
        response = client.projects.analytics.connections.with_raw_response.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Chunkify) -> None:
        with client.projects.analytics.connections.with_streaming_response.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics.connections.with_raw_response.create(
                project_id="",
                name="Website analytics",
                type="custom",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Chunkify) -> None:
        connection = client.projects.analytics.connections.retrieve(
            project_id="projectId",
            connection_id="connectionId",
        )
        assert_matches_type(AnalyticsConnection, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Chunkify) -> None:
        response = client.projects.analytics.connections.with_raw_response.retrieve(
            project_id="projectId",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(AnalyticsConnection, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Chunkify) -> None:
        with client.projects.analytics.connections.with_streaming_response.retrieve(
            project_id="projectId",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(AnalyticsConnection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics.connections.with_raw_response.retrieve(
                project_id="",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.projects.analytics.connections.with_raw_response.retrieve(
                project_id="projectId",
                connection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Chunkify) -> None:
        connection = client.projects.analytics.connections.update(
            project_id="projectId",
            connection_id="connectionId",
        )
        assert_matches_type(AnalyticsConnection, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Chunkify) -> None:
        connection = client.projects.analytics.connections.update(
            project_id="projectId",
            connection_id="connectionId",
            allowed_origins=["string"],
            default_for_dashboard=True,
            endpoint="endpoint",
            name="Production analytics",
            public_ingest_key="ck_public_de90a6057194afc9913a4adcd7ef960db1a91a48d2a13b6b2f7dfe671fd5be36",
            read_key="x",
        )
        assert_matches_type(AnalyticsConnection, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Chunkify) -> None:
        response = client.projects.analytics.connections.with_raw_response.update(
            project_id="projectId",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(AnalyticsConnection, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Chunkify) -> None:
        with client.projects.analytics.connections.with_streaming_response.update(
            project_id="projectId",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(AnalyticsConnection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics.connections.with_raw_response.update(
                project_id="",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.projects.analytics.connections.with_raw_response.update(
                project_id="projectId",
                connection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Chunkify) -> None:
        connection = client.projects.analytics.connections.list(
            "projectId",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Chunkify) -> None:
        response = client.projects.analytics.connections.with_raw_response.list(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Chunkify) -> None:
        with client.projects.analytics.connections.with_streaming_response.list(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics.connections.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Chunkify) -> None:
        connection = client.projects.analytics.connections.delete(
            project_id="projectId",
            connection_id="connectionId",
        )
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Chunkify) -> None:
        response = client.projects.analytics.connections.with_raw_response.delete(
            project_id="projectId",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = response.parse()
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Chunkify) -> None:
        with client.projects.analytics.connections.with_streaming_response.delete(
            project_id="projectId",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics.connections.with_raw_response.delete(
                project_id="",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.projects.analytics.connections.with_raw_response.delete(
                project_id="projectId",
                connection_id="",
            )


class TestAsyncConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncChunkify) -> None:
        connection = await async_client.projects.analytics.connections.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncChunkify) -> None:
        connection = await async_client.projects.analytics.connections.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
            endpoint="https://analytics.example.com",
            public_ingest_key="ck_public_de90a6057194afc9913a4adcd7ef960db1a91a48d2a13b6b2f7dfe671fd5be36",
            read_key="YOUR_READ_ONLY_KEY",
        )
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics.connections.with_raw_response.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics.connections.with_streaming_response.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionCreateResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics.connections.with_raw_response.create(
                project_id="",
                name="Website analytics",
                type="custom",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncChunkify) -> None:
        connection = await async_client.projects.analytics.connections.retrieve(
            project_id="projectId",
            connection_id="connectionId",
        )
        assert_matches_type(AnalyticsConnection, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics.connections.with_raw_response.retrieve(
            project_id="projectId",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(AnalyticsConnection, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics.connections.with_streaming_response.retrieve(
            project_id="projectId",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(AnalyticsConnection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics.connections.with_raw_response.retrieve(
                project_id="",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.projects.analytics.connections.with_raw_response.retrieve(
                project_id="projectId",
                connection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncChunkify) -> None:
        connection = await async_client.projects.analytics.connections.update(
            project_id="projectId",
            connection_id="connectionId",
        )
        assert_matches_type(AnalyticsConnection, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncChunkify) -> None:
        connection = await async_client.projects.analytics.connections.update(
            project_id="projectId",
            connection_id="connectionId",
            allowed_origins=["string"],
            default_for_dashboard=True,
            endpoint="endpoint",
            name="Production analytics",
            public_ingest_key="ck_public_de90a6057194afc9913a4adcd7ef960db1a91a48d2a13b6b2f7dfe671fd5be36",
            read_key="x",
        )
        assert_matches_type(AnalyticsConnection, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics.connections.with_raw_response.update(
            project_id="projectId",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(AnalyticsConnection, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics.connections.with_streaming_response.update(
            project_id="projectId",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(AnalyticsConnection, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics.connections.with_raw_response.update(
                project_id="",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.projects.analytics.connections.with_raw_response.update(
                project_id="projectId",
                connection_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncChunkify) -> None:
        connection = await async_client.projects.analytics.connections.list(
            "projectId",
        )
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics.connections.with_raw_response.list(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert_matches_type(ConnectionListResponse, connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics.connections.with_streaming_response.list(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert_matches_type(ConnectionListResponse, connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics.connections.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncChunkify) -> None:
        connection = await async_client.projects.analytics.connections.delete(
            project_id="projectId",
            connection_id="connectionId",
        )
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics.connections.with_raw_response.delete(
            project_id="projectId",
            connection_id="connectionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connection = await response.parse()
        assert connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics.connections.with_streaming_response.delete(
            project_id="projectId",
            connection_id="connectionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connection = await response.parse()
            assert connection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics.connections.with_raw_response.delete(
                project_id="",
                connection_id="connectionId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.projects.analytics.connections.with_raw_response.delete(
                project_id="projectId",
                connection_id="",
            )
