# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...types import (
    AssetStatus,
    AssetCreateStorageParams,
    asset_list_params,
    asset_create_params,
    asset_delete_params,
    asset_update_params,
)
from .outputs import (
    OutputsResource,
    AsyncOutputsResource,
    OutputsResourceWithRawResponse,
    AsyncOutputsResourceWithRawResponse,
    OutputsResourceWithStreamingResponse,
    AsyncOutputsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import DataWrapper
from ...pagination import SyncPaginatedResults, AsyncPaginatedResults
from ...types.asset import Asset
from ..._base_client import AsyncPaginator, make_request_options
from .workflow.workflow import (
    WorkflowResource,
    AsyncWorkflowResource,
    WorkflowResourceWithRawResponse,
    AsyncWorkflowResourceWithRawResponse,
    WorkflowResourceWithStreamingResponse,
    AsyncWorkflowResourceWithStreamingResponse,
)
from ...types.asset_status import AssetStatus
from ...types.asset_create_storage_params import AssetCreateStorageParams

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""

    @cached_property
    def outputs(self) -> OutputsResource:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return OutputsResource(self._client)

    @cached_property
    def workflow(self) -> WorkflowResource:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return WorkflowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AssetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        source_id: str,
        max_resolution: Literal["1080p", "2160p"] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        min_resolution: Literal["auto", "240p", "360p", "540p", "720p", "1080p", "1440p", "2160p"] | Omit = omit,
        path_template: str | Omit = omit,
        preview_enabled: bool | Omit = omit,
        storage: AssetCreateStorageParams | Omit = omit,
        title: str | Omit = omit,
        workflow_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Asset:
        """Create an Asset from a video Source.

        Processing starts asynchronously.

        Args:
          source_id: ID of the video Source to process.

          max_resolution: Maximum streaming resolution. Omit to use the Project default, or the plan
              maximum if unset. 2160p requires Starter or above. Smaller sources are not
              upscaled. Does not affect static renditions.

          metadata: String metadata with a maximum encoded JSON size of 2048 bytes.

          min_resolution: Minimum streaming resolution. Omit to use the Project default; auto removes the
              minimum. Must not exceed max_resolution. Smaller sources are not upscaled. Does
              not affect static renditions.

          path_template: PathTemplate specifies the Asset output folder relative to Storage base_prefix.
              Supports {assetID} and case-sensitive {metadata.<key>}; referenced values must
              be non-empty. Ignored for Chunkify storage, which always uses {assetID}.
              Overrides the Project default. Defaults to {assetID} when neither is set.
              Maximum template size: 1024 UTF-8 bytes. Expanded prefix: 768 bytes including
              base_prefix and trailing slash.

          preview_enabled: Allow public preview access without an API token. Omit to use the Project
              default. Does not control CDN or static download access.

          storage: Output Storage. Omit to use the Project default. The path_template controls the
              folder for generated output paths.

          title: Asset title, up to 256 characters. Defaults to an empty string.

          workflow_id: WorkflowId specifies the Workflow to select. Omit to use the Project default.
              Set null to disable automatic actions. The current revision is pinned when
              creation is accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/assets",
            body=maybe_transform(
                {
                    "source_id": source_id,
                    "max_resolution": max_resolution,
                    "metadata": metadata,
                    "min_resolution": min_resolution,
                    "path_template": path_template,
                    "preview_enabled": preview_enabled,
                    "storage": storage,
                    "title": title,
                    "workflow_id": workflow_id,
                },
                asset_create_params.AssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Asset]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Asset], DataWrapper[Asset]),
        )

    def retrieve(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Asset:
        """
        Retrieve an Asset and its streaming, static, poster, and timeline outputs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get(
            path_template("/assets/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Asset]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Asset], DataWrapper[Asset]),
        )

    def update(
        self,
        asset_id: str,
        *,
        metadata: Dict[str, str] | Omit = omit,
        preview_enabled: bool | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Update the title, metadata, or public preview access.

        Omitted fields remain
        unchanged.

        Args:
          metadata: Replaces all metadata. Send {} to clear it; omit to leave unchanged. Maximum
              encoded JSON size: 2,048 bytes.

          preview_enabled: Allow public preview access without an API token. Does not control CDN or static
              download access. Disabling it does not revoke signed URLs already issued.

          title: Asset title, up to 256 characters. Send an empty string to clear it; omit to
              leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/assets/{asset_id}", asset_id=asset_id),
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "preview_enabled": preview_enabled,
                    "title": title,
                },
                asset_update_params.AssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        created: asset_list_params.Created | Omit = omit,
        limit: int | Omit = omit,
        metadata: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        source_id: str | Omit = omit,
        status: AssetStatus | Omit = omit,
        storage_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResults[Asset]:
        """
        List Assets in the Project, with filtering and pagination.

        Args:
          limit: Maximum number of Assets to return.

          metadata: Repeat key:value pairs to match all supplied metadata conditions.

          offset: Number of Assets to skip.

          search: Case-insensitive search of Asset IDs and titles.

          source_id: Filter Assets linked to this Source. Omit to include Assets from all Sources in
              the Project.

          status: Filter by Asset status.

          storage_id: Filter by output Storage ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/assets",
            page=SyncPaginatedResults[Asset],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created": created,
                        "limit": limit,
                        "metadata": metadata,
                        "offset": offset,
                        "search": search,
                        "source_id": source_id,
                        "status": status,
                        "storage_id": storage_id,
                    },
                    asset_list_params.AssetListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Asset,
        )

    def delete(
        self,
        asset_id: str,
        *,
        delete_files: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an Asset after all processing finishes.

        Files remain in Storage unless
        delete_files is true.

        Args:
          delete_files: Also delete all files under the Asset's storage prefix, including streaming and
              static outputs. Other files and the original input are preserved. Defaults to
              false, which preserves published media files. Private transcript text and saved
              subtitle copies are always scheduled for removal. File deletion is irreversible.
              If cleanup fails, records remain for retry, but files may already be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/assets/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"delete_files": delete_files}, asset_delete_params.AssetDeleteParams),
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class AsyncAssetsResource(AsyncAPIResource):
    """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""

    @cached_property
    def outputs(self) -> AsyncOutputsResource:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return AsyncOutputsResource(self._client)

    @cached_property
    def workflow(self) -> AsyncWorkflowResource:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return AsyncWorkflowResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncAssetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        source_id: str,
        max_resolution: Literal["1080p", "2160p"] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        min_resolution: Literal["auto", "240p", "360p", "540p", "720p", "1080p", "1440p", "2160p"] | Omit = omit,
        path_template: str | Omit = omit,
        preview_enabled: bool | Omit = omit,
        storage: AssetCreateStorageParams | Omit = omit,
        title: str | Omit = omit,
        workflow_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Asset:
        """Create an Asset from a video Source.

        Processing starts asynchronously.

        Args:
          source_id: ID of the video Source to process.

          max_resolution: Maximum streaming resolution. Omit to use the Project default, or the plan
              maximum if unset. 2160p requires Starter or above. Smaller sources are not
              upscaled. Does not affect static renditions.

          metadata: String metadata with a maximum encoded JSON size of 2048 bytes.

          min_resolution: Minimum streaming resolution. Omit to use the Project default; auto removes the
              minimum. Must not exceed max_resolution. Smaller sources are not upscaled. Does
              not affect static renditions.

          path_template: PathTemplate specifies the Asset output folder relative to Storage base_prefix.
              Supports {assetID} and case-sensitive {metadata.<key>}; referenced values must
              be non-empty. Ignored for Chunkify storage, which always uses {assetID}.
              Overrides the Project default. Defaults to {assetID} when neither is set.
              Maximum template size: 1024 UTF-8 bytes. Expanded prefix: 768 bytes including
              base_prefix and trailing slash.

          preview_enabled: Allow public preview access without an API token. Omit to use the Project
              default. Does not control CDN or static download access.

          storage: Output Storage. Omit to use the Project default. The path_template controls the
              folder for generated output paths.

          title: Asset title, up to 256 characters. Defaults to an empty string.

          workflow_id: WorkflowId specifies the Workflow to select. Omit to use the Project default.
              Set null to disable automatic actions. The current revision is pinned when
              creation is accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/assets",
            body=await async_maybe_transform(
                {
                    "source_id": source_id,
                    "max_resolution": max_resolution,
                    "metadata": metadata,
                    "min_resolution": min_resolution,
                    "path_template": path_template,
                    "preview_enabled": preview_enabled,
                    "storage": storage,
                    "title": title,
                    "workflow_id": workflow_id,
                },
                asset_create_params.AssetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Asset]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Asset], DataWrapper[Asset]),
        )

    async def retrieve(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Asset:
        """
        Retrieve an Asset and its streaming, static, poster, and timeline outputs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._get(
            path_template("/assets/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Asset]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Asset], DataWrapper[Asset]),
        )

    async def update(
        self,
        asset_id: str,
        *,
        metadata: Dict[str, str] | Omit = omit,
        preview_enabled: bool | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Update the title, metadata, or public preview access.

        Omitted fields remain
        unchanged.

        Args:
          metadata: Replaces all metadata. Send {} to clear it; omit to leave unchanged. Maximum
              encoded JSON size: 2,048 bytes.

          preview_enabled: Allow public preview access without an API token. Does not control CDN or static
              download access. Disabling it does not revoke signed URLs already issued.

          title: Asset title, up to 256 characters. Send an empty string to clear it; omit to
              leave unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/assets/{asset_id}", asset_id=asset_id),
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "preview_enabled": preview_enabled,
                    "title": title,
                },
                asset_update_params.AssetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        created: asset_list_params.Created | Omit = omit,
        limit: int | Omit = omit,
        metadata: SequenceNotStr[str] | Omit = omit,
        offset: int | Omit = omit,
        search: str | Omit = omit,
        source_id: str | Omit = omit,
        status: AssetStatus | Omit = omit,
        storage_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Asset, AsyncPaginatedResults[Asset]]:
        """
        List Assets in the Project, with filtering and pagination.

        Args:
          limit: Maximum number of Assets to return.

          metadata: Repeat key:value pairs to match all supplied metadata conditions.

          offset: Number of Assets to skip.

          search: Case-insensitive search of Asset IDs and titles.

          source_id: Filter Assets linked to this Source. Omit to include Assets from all Sources in
              the Project.

          status: Filter by Asset status.

          storage_id: Filter by output Storage ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/assets",
            page=AsyncPaginatedResults[Asset],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created": created,
                        "limit": limit,
                        "metadata": metadata,
                        "offset": offset,
                        "search": search,
                        "source_id": source_id,
                        "status": status,
                        "storage_id": storage_id,
                    },
                    asset_list_params.AssetListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Asset,
        )

    async def delete(
        self,
        asset_id: str,
        *,
        delete_files: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an Asset after all processing finishes.

        Files remain in Storage unless
        delete_files is true.

        Args:
          delete_files: Also delete all files under the Asset's storage prefix, including streaming and
              static outputs. Other files and the original input are preserved. Defaults to
              false, which preserves published media files. Private transcript text and saved
              subtitle copies are always scheduled for removal. File deletion is irreversible.
              If cleanup fails, records remain for retry, but files may already be deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/assets/{asset_id}", asset_id=asset_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"delete_files": delete_files}, asset_delete_params.AssetDeleteParams
                ),
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_raw_response_wrapper(
            assets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            assets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            assets.update,
        )
        self.list = to_raw_response_wrapper(
            assets.list,
        )
        self.delete = to_raw_response_wrapper(
            assets.delete,
        )

    @cached_property
    def outputs(self) -> OutputsResourceWithRawResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return OutputsResourceWithRawResponse(self._assets.outputs)

    @cached_property
    def workflow(self) -> WorkflowResourceWithRawResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return WorkflowResourceWithRawResponse(self._assets.workflow)


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_raw_response_wrapper(
            assets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            assets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            assets.update,
        )
        self.list = async_to_raw_response_wrapper(
            assets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            assets.delete,
        )

    @cached_property
    def outputs(self) -> AsyncOutputsResourceWithRawResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return AsyncOutputsResourceWithRawResponse(self._assets.outputs)

    @cached_property
    def workflow(self) -> AsyncWorkflowResourceWithRawResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return AsyncWorkflowResourceWithRawResponse(self._assets.workflow)


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.create = to_streamed_response_wrapper(
            assets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            assets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            assets.update,
        )
        self.list = to_streamed_response_wrapper(
            assets.list,
        )
        self.delete = to_streamed_response_wrapper(
            assets.delete,
        )

    @cached_property
    def outputs(self) -> OutputsResourceWithStreamingResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return OutputsResourceWithStreamingResponse(self._assets.outputs)

    @cached_property
    def workflow(self) -> WorkflowResourceWithStreamingResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return WorkflowResourceWithStreamingResponse(self._assets.workflow)


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.create = async_to_streamed_response_wrapper(
            assets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            assets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            assets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            assets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            assets.delete,
        )

    @cached_property
    def outputs(self) -> AsyncOutputsResourceWithStreamingResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return AsyncOutputsResourceWithStreamingResponse(self._assets.outputs)

    @cached_property
    def workflow(self) -> AsyncWorkflowResourceWithStreamingResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return AsyncWorkflowResourceWithStreamingResponse(self._assets.workflow)
