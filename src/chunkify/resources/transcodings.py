# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, cast
from typing_extensions import Literal

import httpx

from ..types import transcoding_list_params, transcoding_create_params, transcoding_delete_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import DataWrapper
from ..pagination import SyncPaginatedResults, AsyncPaginatedResults
from .._base_client import AsyncPaginator, make_request_options
from ..types.transcoding import Transcoding

__all__ = ["TranscodingsResource", "AsyncTranscodingsResource"]


class TranscodingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranscodingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return TranscodingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranscodingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return TranscodingsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        format: transcoding_create_params.Format,
        source_id: str,
        metadata: Dict[str, str] | Omit = omit,
        storage: transcoding_create_params.Storage | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transcoding:
        """
        Create a standalone file export with resolved encoding settings.

        Args:
          format: Format specifies the requested encoding settings.

          source_id: SourceId identifies a Source in this Project.

          metadata: Metadata attaches string values to the Transcoding. The serialized object may
              contain at most 2048 bytes.

          storage: Storage overrides the Project output destination. Source storage remains
              independent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/transcodings",
            body=maybe_transform(
                {
                    "format": format,
                    "source_id": source_id,
                    "metadata": metadata,
                    "storage": storage,
                },
                transcoding_create_params.TranscodingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Transcoding]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Transcoding], DataWrapper[Transcoding]),
        )

    def retrieve(
        self,
        transcoding_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transcoding:
        """
        Retrieve the accepted settings, published files and current state of one
        Transcoding.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transcoding_id:
            raise ValueError(f"Expected a non-empty value for `transcoding_id` but received {transcoding_id!r}")
        return self._get(
            path_template("/transcodings/{transcoding_id}", transcoding_id=transcoding_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Transcoding]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Transcoding], DataWrapper[Transcoding]),
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        created: transcoding_list_params.Created | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        source_id: str | Omit = omit,
        status: Literal["preparing", "ready", "failed", "cancelled", "expired"] | Omit = omit,
        storage_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResults[Transcoding]:
        """
        List Transcodings in the authenticated Project, newest first by default.

        Args:
          id: Id filters by an exact Transcoding ID. Omit to include all matching resources.

          limit: Maximum number of Transcodings to return.

          offset: Number of Transcodings to skip.

          source_id: Filter Transcodings linked to this Source. Omit to include Transcodings from all
              Sources in the Project.

          status: Filter by Transcoding status.

          storage_id: Filter by output Storage ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/transcodings",
            page=SyncPaginatedResults[Transcoding],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "created": created,
                        "limit": limit,
                        "offset": offset,
                        "source_id": source_id,
                        "status": status,
                        "storage_id": storage_id,
                    },
                    transcoding_list_params.TranscodingListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Transcoding,
        )

    def delete(
        self,
        transcoding_id: str,
        *,
        delete_files: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a ready, failed, cancelled or expired Transcoding and its file records.
        The Source and settled usage are preserved. Customer output files remain unless
        delete_files is true; temporary files retain their original 24-hour expiry.
        Deletion remains available for inactive teams.

        Args:
          delete_files: DeleteFiles specifies whether to permanently delete this Transcoding's output
              files at their saved storage paths. Defaults to false. The original Source and
              unrelated files are preserved. If deletion fails, records remain for retry, but
              some files may already be deleted. Managed dashboard images are removed with the
              resource; temporary outputs still expire after 24 hours when this option is
              false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transcoding_id:
            raise ValueError(f"Expected a non-empty value for `transcoding_id` but received {transcoding_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/transcodings/{transcoding_id}", transcoding_id=transcoding_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"delete_files": delete_files}, transcoding_delete_params.TranscodingDeleteParams
                ),
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )

    def cancel(
        self,
        transcoding_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Cancel a preparing Transcoding and release its unpaid reservation.

        Repeating an
        accepted cancellation succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transcoding_id:
            raise ValueError(f"Expected a non-empty value for `transcoding_id` but received {transcoding_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/transcodings/{transcoding_id}/cancel", transcoding_id=transcoding_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class AsyncTranscodingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranscodingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTranscodingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranscodingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncTranscodingsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        format: transcoding_create_params.Format,
        source_id: str,
        metadata: Dict[str, str] | Omit = omit,
        storage: transcoding_create_params.Storage | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transcoding:
        """
        Create a standalone file export with resolved encoding settings.

        Args:
          format: Format specifies the requested encoding settings.

          source_id: SourceId identifies a Source in this Project.

          metadata: Metadata attaches string values to the Transcoding. The serialized object may
              contain at most 2048 bytes.

          storage: Storage overrides the Project output destination. Source storage remains
              independent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/transcodings",
            body=await async_maybe_transform(
                {
                    "format": format,
                    "source_id": source_id,
                    "metadata": metadata,
                    "storage": storage,
                },
                transcoding_create_params.TranscodingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Transcoding]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Transcoding], DataWrapper[Transcoding]),
        )

    async def retrieve(
        self,
        transcoding_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Transcoding:
        """
        Retrieve the accepted settings, published files and current state of one
        Transcoding.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transcoding_id:
            raise ValueError(f"Expected a non-empty value for `transcoding_id` but received {transcoding_id!r}")
        return await self._get(
            path_template("/transcodings/{transcoding_id}", transcoding_id=transcoding_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Transcoding]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Transcoding], DataWrapper[Transcoding]),
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        created: transcoding_list_params.Created | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        source_id: str | Omit = omit,
        status: Literal["preparing", "ready", "failed", "cancelled", "expired"] | Omit = omit,
        storage_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Transcoding, AsyncPaginatedResults[Transcoding]]:
        """
        List Transcodings in the authenticated Project, newest first by default.

        Args:
          id: Id filters by an exact Transcoding ID. Omit to include all matching resources.

          limit: Maximum number of Transcodings to return.

          offset: Number of Transcodings to skip.

          source_id: Filter Transcodings linked to this Source. Omit to include Transcodings from all
              Sources in the Project.

          status: Filter by Transcoding status.

          storage_id: Filter by output Storage ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/transcodings",
            page=AsyncPaginatedResults[Transcoding],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "created": created,
                        "limit": limit,
                        "offset": offset,
                        "source_id": source_id,
                        "status": status,
                        "storage_id": storage_id,
                    },
                    transcoding_list_params.TranscodingListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Transcoding,
        )

    async def delete(
        self,
        transcoding_id: str,
        *,
        delete_files: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a ready, failed, cancelled or expired Transcoding and its file records.
        The Source and settled usage are preserved. Customer output files remain unless
        delete_files is true; temporary files retain their original 24-hour expiry.
        Deletion remains available for inactive teams.

        Args:
          delete_files: DeleteFiles specifies whether to permanently delete this Transcoding's output
              files at their saved storage paths. Defaults to false. The original Source and
              unrelated files are preserved. If deletion fails, records remain for retry, but
              some files may already be deleted. Managed dashboard images are removed with the
              resource; temporary outputs still expire after 24 hours when this option is
              false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transcoding_id:
            raise ValueError(f"Expected a non-empty value for `transcoding_id` but received {transcoding_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/transcodings/{transcoding_id}", transcoding_id=transcoding_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"delete_files": delete_files}, transcoding_delete_params.TranscodingDeleteParams
                ),
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )

    async def cancel(
        self,
        transcoding_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Cancel a preparing Transcoding and release its unpaid reservation.

        Repeating an
        accepted cancellation succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transcoding_id:
            raise ValueError(f"Expected a non-empty value for `transcoding_id` but received {transcoding_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/transcodings/{transcoding_id}/cancel", transcoding_id=transcoding_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class TranscodingsResourceWithRawResponse:
    def __init__(self, transcodings: TranscodingsResource) -> None:
        self._transcodings = transcodings

        self.create = to_raw_response_wrapper(
            transcodings.create,
        )
        self.retrieve = to_raw_response_wrapper(
            transcodings.retrieve,
        )
        self.list = to_raw_response_wrapper(
            transcodings.list,
        )
        self.delete = to_raw_response_wrapper(
            transcodings.delete,
        )
        self.cancel = to_raw_response_wrapper(
            transcodings.cancel,
        )


class AsyncTranscodingsResourceWithRawResponse:
    def __init__(self, transcodings: AsyncTranscodingsResource) -> None:
        self._transcodings = transcodings

        self.create = async_to_raw_response_wrapper(
            transcodings.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            transcodings.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            transcodings.list,
        )
        self.delete = async_to_raw_response_wrapper(
            transcodings.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            transcodings.cancel,
        )


class TranscodingsResourceWithStreamingResponse:
    def __init__(self, transcodings: TranscodingsResource) -> None:
        self._transcodings = transcodings

        self.create = to_streamed_response_wrapper(
            transcodings.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            transcodings.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            transcodings.list,
        )
        self.delete = to_streamed_response_wrapper(
            transcodings.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            transcodings.cancel,
        )


class AsyncTranscodingsResourceWithStreamingResponse:
    def __init__(self, transcodings: AsyncTranscodingsResource) -> None:
        self._transcodings = transcodings

        self.create = async_to_streamed_response_wrapper(
            transcodings.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            transcodings.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            transcodings.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            transcodings.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            transcodings.cancel,
        )
