# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from chunkify import Chunkify, AsyncChunkify
from tests.utils import assert_matches_type
from chunkify.pagination import SyncPaginatedResults, AsyncPaginatedResults
from chunkify.types.assets import AssetActionRun
from chunkify.types.workflows import WorkflowRun

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflow:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Chunkify) -> None:
        workflow = client.assets.workflow.update(
            "assetId",
        )
        assert_matches_type(WorkflowRun, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Chunkify) -> None:
        response = client.assets.workflow.with_raw_response.update(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowRun, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Chunkify) -> None:
        with client.assets.workflow.with_streaming_response.update(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowRun, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.workflow.with_raw_response.update(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_actions(self, client: Chunkify) -> None:
        workflow = client.assets.workflow.list_actions(
            asset_id="assetId",
        )
        assert_matches_type(SyncPaginatedResults[AssetActionRun], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_actions_with_all_params(self, client: Chunkify) -> None:
        workflow = client.assets.workflow.list_actions(
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
        assert_matches_type(SyncPaginatedResults[AssetActionRun], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_actions(self, client: Chunkify) -> None:
        response = client.assets.workflow.with_raw_response.list_actions(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(SyncPaginatedResults[AssetActionRun], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_actions(self, client: Chunkify) -> None:
        with client.assets.workflow.with_streaming_response.list_actions(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(SyncPaginatedResults[AssetActionRun], workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_actions(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.workflow.with_raw_response.list_actions(
                asset_id="",
            )


class TestAsyncWorkflow:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncChunkify) -> None:
        workflow = await async_client.assets.workflow.update(
            "assetId",
        )
        assert_matches_type(WorkflowRun, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncChunkify) -> None:
        response = await async_client.assets.workflow.with_raw_response.update(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowRun, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncChunkify) -> None:
        async with async_client.assets.workflow.with_streaming_response.update(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowRun, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.workflow.with_raw_response.update(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_actions(self, async_client: AsyncChunkify) -> None:
        workflow = await async_client.assets.workflow.list_actions(
            asset_id="assetId",
        )
        assert_matches_type(AsyncPaginatedResults[AssetActionRun], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_actions_with_all_params(self, async_client: AsyncChunkify) -> None:
        workflow = await async_client.assets.workflow.list_actions(
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
        assert_matches_type(AsyncPaginatedResults[AssetActionRun], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_actions(self, async_client: AsyncChunkify) -> None:
        response = await async_client.assets.workflow.with_raw_response.list_actions(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(AsyncPaginatedResults[AssetActionRun], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_actions(self, async_client: AsyncChunkify) -> None:
        async with async_client.assets.workflow.with_streaming_response.list_actions(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(AsyncPaginatedResults[AssetActionRun], workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_actions(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.workflow.with_raw_response.list_actions(
                asset_id="",
            )
