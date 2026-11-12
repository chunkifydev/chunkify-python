# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from chunkify import Chunkify, AsyncChunkify
from tests.utils import assert_matches_type
from chunkify.pagination import SyncPaginatedResults, AsyncPaginatedResults
from chunkify.types.assets import AssetOutput

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOutputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Chunkify) -> None:
        output = client.assets.outputs.create(
            asset_id="assetId",
            params={},
            type="caption",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Chunkify) -> None:
        output = client.assets.outputs.create(
            asset_id="assetId",
            params={
                "language_code": "en",
                "source_caption_id": "x",
            },
            type="caption",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Chunkify) -> None:
        response = client.assets.outputs.with_raw_response.create(
            asset_id="assetId",
            params={},
            type="caption",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Chunkify) -> None:
        with client.assets.outputs.with_streaming_response.create(
            asset_id="assetId",
            params={},
            type="caption",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(AssetOutput, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_1(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.outputs.with_raw_response.create(
                asset_id="",
                params={},
                type="caption",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Chunkify) -> None:
        output = client.assets.outputs.create(
            asset_id="assetId",
            params={"resolution": "highest"},
            type="static_rendition",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Chunkify) -> None:
        response = client.assets.outputs.with_raw_response.create(
            asset_id="assetId",
            params={"resolution": "highest"},
            type="static_rendition",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Chunkify) -> None:
        with client.assets.outputs.with_streaming_response.create(
            asset_id="assetId",
            params={"resolution": "highest"},
            type="static_rendition",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(AssetOutput, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_2(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.outputs.with_raw_response.create(
                asset_id="",
                params={"resolution": "highest"},
                type="static_rendition",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: Chunkify) -> None:
        output = client.assets.outputs.create(
            asset_id="assetId",
            params={},
            type="thumbnail",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Chunkify) -> None:
        output = client.assets.outputs.create(
            asset_id="assetId",
            params={
                "count": 1,
                "format": "jpeg",
                "metadata": {"foo": "string"},
                "output": "images",
                "range": {
                    "end": 1,
                    "start": 0,
                },
                "size": 64,
                "timestamps": [0],
            },
            type="thumbnail",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Chunkify) -> None:
        response = client.assets.outputs.with_raw_response.create(
            asset_id="assetId",
            params={},
            type="thumbnail",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Chunkify) -> None:
        with client.assets.outputs.with_streaming_response.create(
            asset_id="assetId",
            params={},
            type="thumbnail",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(AssetOutput, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_3(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.outputs.with_raw_response.create(
                asset_id="",
                params={},
                type="thumbnail",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_4(self, client: Chunkify) -> None:
        output = client.assets.outputs.create(
            asset_id="assetId",
            params={},
            type="transcript",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Chunkify) -> None:
        response = client.assets.outputs.with_raw_response.create(
            asset_id="assetId",
            params={},
            type="transcript",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Chunkify) -> None:
        with client.assets.outputs.with_streaming_response.create(
            asset_id="assetId",
            params={},
            type="transcript",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(AssetOutput, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_overload_4(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.outputs.with_raw_response.create(
                asset_id="",
                params={},
                type="transcript",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Chunkify) -> None:
        output = client.assets.outputs.retrieve(
            output_id="outputId",
            asset_id="assetId",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Chunkify) -> None:
        response = client.assets.outputs.with_raw_response.retrieve(
            output_id="outputId",
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Chunkify) -> None:
        with client.assets.outputs.with_streaming_response.retrieve(
            output_id="outputId",
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(AssetOutput, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.outputs.with_raw_response.retrieve(
                output_id="outputId",
                asset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `output_id` but received ''"):
            client.assets.outputs.with_raw_response.retrieve(
                output_id="",
                asset_id="assetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Chunkify) -> None:
        output = client.assets.outputs.list(
            asset_id="assetId",
        )
        assert_matches_type(SyncPaginatedResults[AssetOutput], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Chunkify) -> None:
        output = client.assets.outputs.list(
            asset_id="assetId",
            limit=1,
            offset=0,
            status="preparing",
            type="caption",
        )
        assert_matches_type(SyncPaginatedResults[AssetOutput], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Chunkify) -> None:
        response = client.assets.outputs.with_raw_response.list(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(SyncPaginatedResults[AssetOutput], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Chunkify) -> None:
        with client.assets.outputs.with_streaming_response.list(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(SyncPaginatedResults[AssetOutput], output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.outputs.with_raw_response.list(
                asset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Chunkify) -> None:
        output = client.assets.outputs.delete(
            output_id="outputId",
            asset_id="assetId",
        )
        assert output is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Chunkify) -> None:
        output = client.assets.outputs.delete(
            output_id="outputId",
            asset_id="assetId",
            delete_files=True,
        )
        assert output is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Chunkify) -> None:
        response = client.assets.outputs.with_raw_response.delete(
            output_id="outputId",
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert output is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Chunkify) -> None:
        with client.assets.outputs.with_streaming_response.delete(
            output_id="outputId",
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert output is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Chunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.assets.outputs.with_raw_response.delete(
                output_id="outputId",
                asset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `output_id` but received ''"):
            client.assets.outputs.with_raw_response.delete(
                output_id="",
                asset_id="assetId",
            )


class TestAsyncOutputs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncChunkify) -> None:
        output = await async_client.assets.outputs.create(
            asset_id="assetId",
            params={},
            type="caption",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncChunkify) -> None:
        output = await async_client.assets.outputs.create(
            asset_id="assetId",
            params={
                "language_code": "en",
                "source_caption_id": "x",
            },
            type="caption",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncChunkify) -> None:
        response = await async_client.assets.outputs.with_raw_response.create(
            asset_id="assetId",
            params={},
            type="caption",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncChunkify) -> None:
        async with async_client.assets.outputs.with_streaming_response.create(
            asset_id="assetId",
            params={},
            type="caption",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(AssetOutput, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.outputs.with_raw_response.create(
                asset_id="",
                params={},
                type="caption",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncChunkify) -> None:
        output = await async_client.assets.outputs.create(
            asset_id="assetId",
            params={"resolution": "highest"},
            type="static_rendition",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncChunkify) -> None:
        response = await async_client.assets.outputs.with_raw_response.create(
            asset_id="assetId",
            params={"resolution": "highest"},
            type="static_rendition",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncChunkify) -> None:
        async with async_client.assets.outputs.with_streaming_response.create(
            asset_id="assetId",
            params={"resolution": "highest"},
            type="static_rendition",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(AssetOutput, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.outputs.with_raw_response.create(
                asset_id="",
                params={"resolution": "highest"},
                type="static_rendition",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncChunkify) -> None:
        output = await async_client.assets.outputs.create(
            asset_id="assetId",
            params={},
            type="thumbnail",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncChunkify) -> None:
        output = await async_client.assets.outputs.create(
            asset_id="assetId",
            params={
                "count": 1,
                "format": "jpeg",
                "metadata": {"foo": "string"},
                "output": "images",
                "range": {
                    "end": 1,
                    "start": 0,
                },
                "size": 64,
                "timestamps": [0],
            },
            type="thumbnail",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncChunkify) -> None:
        response = await async_client.assets.outputs.with_raw_response.create(
            asset_id="assetId",
            params={},
            type="thumbnail",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncChunkify) -> None:
        async with async_client.assets.outputs.with_streaming_response.create(
            asset_id="assetId",
            params={},
            type="thumbnail",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(AssetOutput, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.outputs.with_raw_response.create(
                asset_id="",
                params={},
                type="thumbnail",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncChunkify) -> None:
        output = await async_client.assets.outputs.create(
            asset_id="assetId",
            params={},
            type="transcript",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncChunkify) -> None:
        response = await async_client.assets.outputs.with_raw_response.create(
            asset_id="assetId",
            params={},
            type="transcript",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncChunkify) -> None:
        async with async_client.assets.outputs.with_streaming_response.create(
            asset_id="assetId",
            params={},
            type="transcript",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(AssetOutput, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.outputs.with_raw_response.create(
                asset_id="",
                params={},
                type="transcript",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncChunkify) -> None:
        output = await async_client.assets.outputs.retrieve(
            output_id="outputId",
            asset_id="assetId",
        )
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncChunkify) -> None:
        response = await async_client.assets.outputs.with_raw_response.retrieve(
            output_id="outputId",
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(AssetOutput, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncChunkify) -> None:
        async with async_client.assets.outputs.with_streaming_response.retrieve(
            output_id="outputId",
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(AssetOutput, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.outputs.with_raw_response.retrieve(
                output_id="outputId",
                asset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `output_id` but received ''"):
            await async_client.assets.outputs.with_raw_response.retrieve(
                output_id="",
                asset_id="assetId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncChunkify) -> None:
        output = await async_client.assets.outputs.list(
            asset_id="assetId",
        )
        assert_matches_type(AsyncPaginatedResults[AssetOutput], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncChunkify) -> None:
        output = await async_client.assets.outputs.list(
            asset_id="assetId",
            limit=1,
            offset=0,
            status="preparing",
            type="caption",
        )
        assert_matches_type(AsyncPaginatedResults[AssetOutput], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncChunkify) -> None:
        response = await async_client.assets.outputs.with_raw_response.list(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(AsyncPaginatedResults[AssetOutput], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncChunkify) -> None:
        async with async_client.assets.outputs.with_streaming_response.list(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(AsyncPaginatedResults[AssetOutput], output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.outputs.with_raw_response.list(
                asset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncChunkify) -> None:
        output = await async_client.assets.outputs.delete(
            output_id="outputId",
            asset_id="assetId",
        )
        assert output is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncChunkify) -> None:
        output = await async_client.assets.outputs.delete(
            output_id="outputId",
            asset_id="assetId",
            delete_files=True,
        )
        assert output is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncChunkify) -> None:
        response = await async_client.assets.outputs.with_raw_response.delete(
            output_id="outputId",
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert output is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncChunkify) -> None:
        async with async_client.assets.outputs.with_streaming_response.delete(
            output_id="outputId",
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert output is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncChunkify) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.assets.outputs.with_raw_response.delete(
                output_id="outputId",
                asset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `output_id` but received ''"):
            await async_client.assets.outputs.with_raw_response.delete(
                output_id="",
                asset_id="assetId",
            )
