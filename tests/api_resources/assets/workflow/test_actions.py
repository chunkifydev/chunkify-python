# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from chunkify import Chunkify, AsyncChunkify
from tests.utils import assert_matches_type
from chunkify.pagination import SyncPaginatedResults, AsyncPaginatedResults
from chunkify.types.assets.workflow import AssetActionRun

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Chunkify) -> None:
        action = client.assets.workflow.actions.list(
            asset_id="assetId",
        )
        assert_matches_type(SyncPaginatedResults[AssetActionRun], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Chunkify) -> None:
        action = client.assets.workflow.actions.list(
            asset_id="assetId",
            created={
                "gte": 0,
                "lte": 0,
            },
            latest_per_action=True,
            limit=1,
            offset=0,
            revision=1,
            status="pending",
            type="create_static_rendition",
        )
        assert_matches_type(SyncPaginatedResults[AssetActionRun], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Chunkify) -> None:
        response = client.assets.workflow.actions.with_raw_response.list(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = response.parse()
        assert_matches_type(SyncPaginatedResults[AssetActionRun], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Chunkify) -> None:
        with client.assets.workflow.actions.with_streaming_response.list(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = response.parse()
            assert_matches_type(SyncPaginatedResults[AssetActionRun], action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.workflow.actions.with_raw_response.list(
                asset_id="",
            )


class TestAsyncActions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncChunkify) -> None:
        action = await async_client.assets.workflow.actions.list(
            asset_id="assetId",
        )
        assert_matches_type(AsyncPaginatedResults[AssetActionRun], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncChunkify) -> None:
        action = await async_client.assets.workflow.actions.list(
            asset_id="assetId",
            created={
                "gte": 0,
                "lte": 0,
            },
            latest_per_action=True,
            limit=1,
            offset=0,
            revision=1,
            status="pending",
            type="create_static_rendition",
        )
        assert_matches_type(AsyncPaginatedResults[AssetActionRun], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncChunkify) -> None:
        response = await async_client.assets.workflow.actions.with_raw_response.list(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        action = await response.parse()
        assert_matches_type(AsyncPaginatedResults[AssetActionRun], action, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncChunkify) -> None:
        async with async_client.assets.workflow.actions.with_streaming_response.list(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            action = await response.parse()
            assert_matches_type(AsyncPaginatedResults[AssetActionRun], action, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.workflow.actions.with_raw_response.list(
                asset_id="",
            )
