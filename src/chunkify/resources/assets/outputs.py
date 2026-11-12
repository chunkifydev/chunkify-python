# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..._base_client import AsyncPaginator, make_request_options
from ...types.assets import output_list_params, output_create_params, output_delete_params
from ...types.assets.asset_output import AssetOutput

__all__ = ["OutputsResource", "AsyncOutputsResource"]


class OutputsResource(SyncAPIResource):
    """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""

    @cached_property
    def with_raw_response(self) -> OutputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return OutputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return OutputsResourceWithStreamingResponse(self)

    def create(
        self,
        asset_id: str,
        *,
        output: output_create_params.Output,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetOutput:
        """Create one caption, static rendition or additional thumbnail output.

        The
        accepted output processes asynchronously and is returned in the same envelope as
        output reads.

        Args:
          output: Create one output for an Asset. Type selects its required, strictly validated
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return cast(
            AssetOutput,
            self._post(
                path_template("/assets/{asset_id}/outputs", asset_id=asset_id),
                body=maybe_transform(output, output_create_params.OutputCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=DataWrapper[AssetOutput]._unwrapper,
                    security={"project_access_token": True},
                ),
                cast_to=cast(
                    Any, DataWrapper[AssetOutput]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve(
        self,
        output_id: str,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetOutput:
        """
        Retrieve one output belonging to the specified Asset and authenticated Project.
        Delivery URLs follow the output resource retention and expiry rules.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if not output_id:
            raise ValueError(f"Expected a non-empty value for `output_id` but received {output_id!r}")
        return cast(
            AssetOutput,
            self._get(
                path_template("/assets/{asset_id}/outputs/{output_id}", asset_id=asset_id, output_id=output_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=DataWrapper[AssetOutput]._unwrapper,
                    security={"project_access_token": True},
                ),
                cast_to=cast(
                    Any, DataWrapper[AssetOutput]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        asset_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["preparing", "ready", "failed", "expired"] | Omit = omit,
        type: Literal["caption", "transcript", "static_rendition", "thumbnail"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResults[AssetOutput]:
        """List outputs requested directly or by a Workflow.

        Results are ordered by
        creation date, newest first, with descending output ID as a tie-breaker.
        Pagination and total apply after type and status filters. Core playback, poster
        and default timeline previews remain on the Asset.

        Args:
          limit: Limit specifies the maximum number of results to return. Accepts 1 to 100.
              Defaults to 100.

          offset: Offset specifies the number of matching results to skip. Must be at least 0.
              Defaults to 0.

          status: Status specifies the current output state to include. Omit it to include all
              states.

          type: Type specifies the output kind to include. Omit it to include all kinds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get_api_list(
            path_template("/assets/{asset_id}/outputs", asset_id=asset_id),
            page=SyncPaginatedResults[AssetOutput],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                        "type": type,
                    },
                    output_list_params.OutputListParams,
                ),
                security={"project_access_token": True},
            ),
            model=cast(Any, AssetOutput),  # Union types cannot be passed in as arguments in the type system
        )

    def delete(
        self,
        output_id: str,
        *,
        asset_id: str,
        delete_files: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete one output belonging to this Asset and Project.

        Its type is resolved from
        the output ID. Type-specific processing and dependency restrictions still apply.

        Args:
          delete_files: DeleteFiles specifies whether to remove this output's published media files from
              Storage. Defaults to false, preserving those files. Transcript deletion always
              schedules removal of its private text and saved subtitle copy, regardless of
              this option. The Asset, Source, and other outputs are preserved. File cleanup
              failures retain the output record for retry; files already removed cannot be
              restored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if not output_id:
            raise ValueError(f"Expected a non-empty value for `output_id` but received {output_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/assets/{asset_id}/outputs/{output_id}", asset_id=asset_id, output_id=output_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"delete_files": delete_files}, output_delete_params.OutputDeleteParams),
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class AsyncOutputsResource(AsyncAPIResource):
    """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""

    @cached_property
    def with_raw_response(self) -> AsyncOutputsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOutputsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutputsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncOutputsResourceWithStreamingResponse(self)

    async def create(
        self,
        asset_id: str,
        *,
        output: output_create_params.Output,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetOutput:
        """Create one caption, static rendition or additional thumbnail output.

        The
        accepted output processes asynchronously and is returned in the same envelope as
        output reads.

        Args:
          output: Create one output for an Asset. Type selects its required, strictly validated
              parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return cast(
            AssetOutput,
            await self._post(
                path_template("/assets/{asset_id}/outputs", asset_id=asset_id),
                body=await async_maybe_transform(output, output_create_params.OutputCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=DataWrapper[AssetOutput]._unwrapper,
                    security={"project_access_token": True},
                ),
                cast_to=cast(
                    Any, DataWrapper[AssetOutput]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve(
        self,
        output_id: str,
        *,
        asset_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetOutput:
        """
        Retrieve one output belonging to the specified Asset and authenticated Project.
        Delivery URLs follow the output resource retention and expiry rules.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if not output_id:
            raise ValueError(f"Expected a non-empty value for `output_id` but received {output_id!r}")
        return cast(
            AssetOutput,
            await self._get(
                path_template("/assets/{asset_id}/outputs/{output_id}", asset_id=asset_id, output_id=output_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=DataWrapper[AssetOutput]._unwrapper,
                    security={"project_access_token": True},
                ),
                cast_to=cast(
                    Any, DataWrapper[AssetOutput]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        asset_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["preparing", "ready", "failed", "expired"] | Omit = omit,
        type: Literal["caption", "transcript", "static_rendition", "thumbnail"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AssetOutput, AsyncPaginatedResults[AssetOutput]]:
        """List outputs requested directly or by a Workflow.

        Results are ordered by
        creation date, newest first, with descending output ID as a tie-breaker.
        Pagination and total apply after type and status filters. Core playback, poster
        and default timeline previews remain on the Asset.

        Args:
          limit: Limit specifies the maximum number of results to return. Accepts 1 to 100.
              Defaults to 100.

          offset: Offset specifies the number of matching results to skip. Must be at least 0.
              Defaults to 0.

          status: Status specifies the current output state to include. Omit it to include all
              states.

          type: Type specifies the output kind to include. Omit it to include all kinds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get_api_list(
            path_template("/assets/{asset_id}/outputs", asset_id=asset_id),
            page=AsyncPaginatedResults[AssetOutput],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                        "type": type,
                    },
                    output_list_params.OutputListParams,
                ),
                security={"project_access_token": True},
            ),
            model=cast(Any, AssetOutput),  # Union types cannot be passed in as arguments in the type system
        )

    async def delete(
        self,
        output_id: str,
        *,
        asset_id: str,
        delete_files: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete one output belonging to this Asset and Project.

        Its type is resolved from
        the output ID. Type-specific processing and dependency restrictions still apply.

        Args:
          delete_files: DeleteFiles specifies whether to remove this output's published media files from
              Storage. Defaults to false, preserving those files. Transcript deletion always
              schedules removal of its private text and saved subtitle copy, regardless of
              this option. The Asset, Source, and other outputs are preserved. File cleanup
              failures retain the output record for retry; files already removed cannot be
              restored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        if not output_id:
            raise ValueError(f"Expected a non-empty value for `output_id` but received {output_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/assets/{asset_id}/outputs/{output_id}", asset_id=asset_id, output_id=output_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"delete_files": delete_files}, output_delete_params.OutputDeleteParams
                ),
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class OutputsResourceWithRawResponse:
    def __init__(self, outputs: OutputsResource) -> None:
        self._outputs = outputs

        self.create = to_raw_response_wrapper(
            outputs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            outputs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            outputs.list,
        )
        self.delete = to_raw_response_wrapper(
            outputs.delete,
        )


class AsyncOutputsResourceWithRawResponse:
    def __init__(self, outputs: AsyncOutputsResource) -> None:
        self._outputs = outputs

        self.create = async_to_raw_response_wrapper(
            outputs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            outputs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            outputs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            outputs.delete,
        )


class OutputsResourceWithStreamingResponse:
    def __init__(self, outputs: OutputsResource) -> None:
        self._outputs = outputs

        self.create = to_streamed_response_wrapper(
            outputs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            outputs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            outputs.list,
        )
        self.delete = to_streamed_response_wrapper(
            outputs.delete,
        )


class AsyncOutputsResourceWithStreamingResponse:
    def __init__(self, outputs: AsyncOutputsResource) -> None:
        self._outputs = outputs

        self.create = async_to_streamed_response_wrapper(
            outputs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            outputs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            outputs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            outputs.delete,
        )
