# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from chunkify import Chunkify, AsyncChunkify
from tests.utils import assert_matches_type
from chunkify.types import (
    MetricsUsage,
    MetricsAssets,
    MetricsStorage,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_assets(self, client: Chunkify) -> None:
        metric = client.metrics.assets()
        assert_matches_type(MetricsAssets, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_assets_with_all_params(self, client: Chunkify) -> None:
        metric = client.metrics.assets(
            format="json",
            from_="7321-69-10",
            to="7321-69-10",
        )
        assert_matches_type(MetricsAssets, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_assets(self, client: Chunkify) -> None:
        response = client.metrics.with_raw_response.assets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricsAssets, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_assets(self, client: Chunkify) -> None:
        with client.metrics.with_streaming_response.assets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricsAssets, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_storage(self, client: Chunkify) -> None:
        metric = client.metrics.storage()
        assert_matches_type(MetricsStorage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_storage_with_all_params(self, client: Chunkify) -> None:
        metric = client.metrics.storage(
            format="json",
            from_="7321-69-10",
            storage_id="x",
            to="7321-69-10",
        )
        assert_matches_type(MetricsStorage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_storage(self, client: Chunkify) -> None:
        response = client.metrics.with_raw_response.storage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricsStorage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_storage(self, client: Chunkify) -> None:
        with client.metrics.with_streaming_response.storage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricsStorage, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_usage(self, client: Chunkify) -> None:
        metric = client.metrics.usage()
        assert_matches_type(MetricsUsage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_usage_with_all_params(self, client: Chunkify) -> None:
        metric = client.metrics.usage(
            format="json",
            from_="7321-69-10",
            to="7321-69-10",
        )
        assert_matches_type(MetricsUsage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_usage(self, client: Chunkify) -> None:
        response = client.metrics.with_raw_response.usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = response.parse()
        assert_matches_type(MetricsUsage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_usage(self, client: Chunkify) -> None:
        with client.metrics.with_streaming_response.usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = response.parse()
            assert_matches_type(MetricsUsage, metric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_assets(self, async_client: AsyncChunkify) -> None:
        metric = await async_client.metrics.assets()
        assert_matches_type(MetricsAssets, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_assets_with_all_params(self, async_client: AsyncChunkify) -> None:
        metric = await async_client.metrics.assets(
            format="json",
            from_="7321-69-10",
            to="7321-69-10",
        )
        assert_matches_type(MetricsAssets, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_assets(self, async_client: AsyncChunkify) -> None:
        response = await async_client.metrics.with_raw_response.assets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricsAssets, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_assets(self, async_client: AsyncChunkify) -> None:
        async with async_client.metrics.with_streaming_response.assets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricsAssets, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_storage(self, async_client: AsyncChunkify) -> None:
        metric = await async_client.metrics.storage()
        assert_matches_type(MetricsStorage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_storage_with_all_params(self, async_client: AsyncChunkify) -> None:
        metric = await async_client.metrics.storage(
            format="json",
            from_="7321-69-10",
            storage_id="x",
            to="7321-69-10",
        )
        assert_matches_type(MetricsStorage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_storage(self, async_client: AsyncChunkify) -> None:
        response = await async_client.metrics.with_raw_response.storage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricsStorage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_storage(self, async_client: AsyncChunkify) -> None:
        async with async_client.metrics.with_streaming_response.storage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricsStorage, metric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_usage(self, async_client: AsyncChunkify) -> None:
        metric = await async_client.metrics.usage()
        assert_matches_type(MetricsUsage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_usage_with_all_params(self, async_client: AsyncChunkify) -> None:
        metric = await async_client.metrics.usage(
            format="json",
            from_="7321-69-10",
            to="7321-69-10",
        )
        assert_matches_type(MetricsUsage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_usage(self, async_client: AsyncChunkify) -> None:
        response = await async_client.metrics.with_raw_response.usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metric = await response.parse()
        assert_matches_type(MetricsUsage, metric, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_usage(self, async_client: AsyncChunkify) -> None:
        async with async_client.metrics.with_streaming_response.usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metric = await response.parse()
            assert_matches_type(MetricsUsage, metric, path=["response"])

        assert cast(Any, response.is_closed) is True
