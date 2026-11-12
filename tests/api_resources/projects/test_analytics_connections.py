# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from chunkify import Chunkify, AsyncChunkify
from tests.utils import assert_matches_type
from chunkify.types.projects import (
    AnalyticsConnection,
    AnalyticsConnectionListResponse,
    AnalyticsConnectionCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnalyticsConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Chunkify) -> None:
        analytics_connection = client.projects.analytics_connections.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        )
        assert_matches_type(AnalyticsConnectionCreateResponse, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Chunkify) -> None:
        analytics_connection = client.projects.analytics_connections.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
            endpoint="https://analytics.example.com",
            public_ingest_key="ck_public_de90a6057194afc9913a4adcd7ef960db1a91a48d2a13b6b2f7dfe671fd5be36",
            read_key="YOUR_READ_ONLY_KEY",
        )
        assert_matches_type(AnalyticsConnectionCreateResponse, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Chunkify) -> None:
        response = client.projects.analytics_connections.with_raw_response.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_connection = response.parse()
        assert_matches_type(AnalyticsConnectionCreateResponse, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Chunkify) -> None:
        with client.projects.analytics_connections.with_streaming_response.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_connection = response.parse()
            assert_matches_type(AnalyticsConnectionCreateResponse, analytics_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics_connections.with_raw_response.create(
                project_id="",
                name="Website analytics",
                type="custom",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Chunkify) -> None:
        analytics_connection = client.projects.analytics_connections.retrieve(
            connection_id="connectionId",
            project_id="projectId",
        )
        assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Chunkify) -> None:
        response = client.projects.analytics_connections.with_raw_response.retrieve(
            connection_id="connectionId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_connection = response.parse()
        assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Chunkify) -> None:
        with client.projects.analytics_connections.with_streaming_response.retrieve(
            connection_id="connectionId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_connection = response.parse()
            assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics_connections.with_raw_response.retrieve(
                connection_id="connectionId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.projects.analytics_connections.with_raw_response.retrieve(
                connection_id="",
                project_id="projectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Chunkify) -> None:
        analytics_connection = client.projects.analytics_connections.update(
            connection_id="connectionId",
            project_id="projectId",
        )
        assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Chunkify) -> None:
        analytics_connection = client.projects.analytics_connections.update(
            connection_id="connectionId",
            project_id="projectId",
            allowed_origins=["string"],
            default_for_dashboard=True,
            endpoint="endpoint",
            name="Production analytics",
            public_ingest_key="ck_public_de90a6057194afc9913a4adcd7ef960db1a91a48d2a13b6b2f7dfe671fd5be36",
            read_key="x",
        )
        assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Chunkify) -> None:
        response = client.projects.analytics_connections.with_raw_response.update(
            connection_id="connectionId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_connection = response.parse()
        assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Chunkify) -> None:
        with client.projects.analytics_connections.with_streaming_response.update(
            connection_id="connectionId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_connection = response.parse()
            assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics_connections.with_raw_response.update(
                connection_id="connectionId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.projects.analytics_connections.with_raw_response.update(
                connection_id="",
                project_id="projectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Chunkify) -> None:
        analytics_connection = client.projects.analytics_connections.list(
            "projectId",
        )
        assert_matches_type(AnalyticsConnectionListResponse, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Chunkify) -> None:
        response = client.projects.analytics_connections.with_raw_response.list(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_connection = response.parse()
        assert_matches_type(AnalyticsConnectionListResponse, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Chunkify) -> None:
        with client.projects.analytics_connections.with_streaming_response.list(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_connection = response.parse()
            assert_matches_type(AnalyticsConnectionListResponse, analytics_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics_connections.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Chunkify) -> None:
        analytics_connection = client.projects.analytics_connections.delete(
            connection_id="connectionId",
            project_id="projectId",
        )
        assert analytics_connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Chunkify) -> None:
        response = client.projects.analytics_connections.with_raw_response.delete(
            connection_id="connectionId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_connection = response.parse()
        assert analytics_connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Chunkify) -> None:
        with client.projects.analytics_connections.with_streaming_response.delete(
            connection_id="connectionId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_connection = response.parse()
            assert analytics_connection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.projects.analytics_connections.with_raw_response.delete(
                connection_id="connectionId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            client.projects.analytics_connections.with_raw_response.delete(
                connection_id="",
                project_id="projectId",
            )


class TestAsyncAnalyticsConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncChunkify) -> None:
        analytics_connection = await async_client.projects.analytics_connections.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        )
        assert_matches_type(AnalyticsConnectionCreateResponse, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncChunkify) -> None:
        analytics_connection = await async_client.projects.analytics_connections.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
            endpoint="https://analytics.example.com",
            public_ingest_key="ck_public_de90a6057194afc9913a4adcd7ef960db1a91a48d2a13b6b2f7dfe671fd5be36",
            read_key="YOUR_READ_ONLY_KEY",
        )
        assert_matches_type(AnalyticsConnectionCreateResponse, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics_connections.with_raw_response.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_connection = await response.parse()
        assert_matches_type(AnalyticsConnectionCreateResponse, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics_connections.with_streaming_response.create(
            project_id="projectId",
            name="Website analytics",
            type="custom",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_connection = await response.parse()
            assert_matches_type(AnalyticsConnectionCreateResponse, analytics_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics_connections.with_raw_response.create(
                project_id="",
                name="Website analytics",
                type="custom",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncChunkify) -> None:
        analytics_connection = await async_client.projects.analytics_connections.retrieve(
            connection_id="connectionId",
            project_id="projectId",
        )
        assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics_connections.with_raw_response.retrieve(
            connection_id="connectionId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_connection = await response.parse()
        assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics_connections.with_streaming_response.retrieve(
            connection_id="connectionId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_connection = await response.parse()
            assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics_connections.with_raw_response.retrieve(
                connection_id="connectionId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.projects.analytics_connections.with_raw_response.retrieve(
                connection_id="",
                project_id="projectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncChunkify) -> None:
        analytics_connection = await async_client.projects.analytics_connections.update(
            connection_id="connectionId",
            project_id="projectId",
        )
        assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncChunkify) -> None:
        analytics_connection = await async_client.projects.analytics_connections.update(
            connection_id="connectionId",
            project_id="projectId",
            allowed_origins=["string"],
            default_for_dashboard=True,
            endpoint="endpoint",
            name="Production analytics",
            public_ingest_key="ck_public_de90a6057194afc9913a4adcd7ef960db1a91a48d2a13b6b2f7dfe671fd5be36",
            read_key="x",
        )
        assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics_connections.with_raw_response.update(
            connection_id="connectionId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_connection = await response.parse()
        assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics_connections.with_streaming_response.update(
            connection_id="connectionId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_connection = await response.parse()
            assert_matches_type(AnalyticsConnection, analytics_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics_connections.with_raw_response.update(
                connection_id="connectionId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.projects.analytics_connections.with_raw_response.update(
                connection_id="",
                project_id="projectId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncChunkify) -> None:
        analytics_connection = await async_client.projects.analytics_connections.list(
            "projectId",
        )
        assert_matches_type(AnalyticsConnectionListResponse, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics_connections.with_raw_response.list(
            "projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_connection = await response.parse()
        assert_matches_type(AnalyticsConnectionListResponse, analytics_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics_connections.with_streaming_response.list(
            "projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_connection = await response.parse()
            assert_matches_type(AnalyticsConnectionListResponse, analytics_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics_connections.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncChunkify) -> None:
        analytics_connection = await async_client.projects.analytics_connections.delete(
            connection_id="connectionId",
            project_id="projectId",
        )
        assert analytics_connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncChunkify) -> None:
        response = await async_client.projects.analytics_connections.with_raw_response.delete(
            connection_id="connectionId",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        analytics_connection = await response.parse()
        assert analytics_connection is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncChunkify) -> None:
        async with async_client.projects.analytics_connections.with_streaming_response.delete(
            connection_id="connectionId",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            analytics_connection = await response.parse()
            assert analytics_connection is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.projects.analytics_connections.with_raw_response.delete(
                connection_id="connectionId",
                project_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connection_id` but received ''"):
            await async_client.projects.analytics_connections.with_raw_response.delete(
                connection_id="",
                project_id="projectId",
            )
