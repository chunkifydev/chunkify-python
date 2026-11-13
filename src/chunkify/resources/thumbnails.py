# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ..types import thumbnail_list_params, thumbnail_create_params, thumbnail_delete_params
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
from ..types.thumbnail import Thumbnail

__all__ = ["ThumbnailsResource", "AsyncThumbnailsResource"]


class ThumbnailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ThumbnailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return ThumbnailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThumbnailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return ThumbnailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        source_id: str,
        count: int | Omit = omit,
        format: Literal["jpeg", "webp"] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        output: Literal["images", "sprites"] | Omit = omit,
        range: thumbnail_create_params.Range | Omit = omit,
        size: int | Omit = omit,
        storage: thumbnail_create_params.Storage | Omit = omit,
        timestamps: Iterable[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Thumbnail:
        """Generate individual images or sprite sheets from a Source.

        Each accepted request
        creates a new resource. Processing continues after the response.

        Args:
          source_id: SourceId identifies a video Source in this Project.

          count: Count specifies 1 to 100 thumbnails at the middle of equal sections of the
              selected range.

          format: Format selects JPEG or WebP. Defaults to JPEG.

          metadata: Metadata attaches string values to this request. The serialized object may
              contain at most 2048 bytes.

          output: Output selects images or sprites. Defaults to images.

          range: Range limits sampling to part of the Source. Defaults to the whole Source
              duration.

          size: Size specifies the maximum image or tile edge in pixels, from 64 to 1920.
              Defaults to 320. Odd sizes are supported. Preserves display aspect ratio without
              cropping or upscaling.

          storage: Storage overrides the Project output destination and names the output files.
              Source storage remains independent.

          timestamps: Timestamps specifies 1 to 100 Source-relative target times in seconds. Every
              time must be within the selected range. Repeated targets produce separate
              outputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/thumbnails",
            body=maybe_transform(
                {
                    "source_id": source_id,
                    "count": count,
                    "format": format,
                    "metadata": metadata,
                    "output": output,
                    "range": range,
                    "size": size,
                    "storage": storage,
                    "timestamps": timestamps,
                },
                thumbnail_create_params.ThumbnailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Thumbnail]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Thumbnail], DataWrapper[Thumbnail]),
        )

    def retrieve(
        self,
        thumbnail_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Thumbnail:
        """
        Retrieve the accepted settings, published files and current state of one
        Thumbnail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thumbnail_id:
            raise ValueError(f"Expected a non-empty value for `thumbnail_id` but received {thumbnail_id!r}")
        return self._get(
            path_template("/thumbnails/{thumbnail_id}", thumbnail_id=thumbnail_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Thumbnail]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Thumbnail], DataWrapper[Thumbnail]),
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        created: thumbnail_list_params.Created | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        source_id: str | Omit = omit,
        status: Literal["preparing", "ready", "failed", "expired"] | Omit = omit,
        storage_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResults[Thumbnail]:
        """
        List Thumbnails in the authenticated Project, newest first by default.

        Args:
          id: Id filters by an exact Thumbnail ID. Omit to include all matching resources.

          limit: Maximum number of Thumbnails to return.

          offset: Number of Thumbnails to skip.

          source_id: Filter Thumbnails linked to this Source. Omit to include Thumbnails from all
              Sources in the Project.

          status: Filter by Thumbnail status.

          storage_id: Filter by output Storage ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/thumbnails",
            page=SyncPaginatedResults[Thumbnail],
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
                    thumbnail_list_params.ThumbnailListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Thumbnail,
        )

    def delete(
        self,
        thumbnail_id: str,
        *,
        delete_files: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a ready, failed or expired Thumbnail after all workers have stopped.

        The
        Source and settled usage are preserved. Files remain unless delete_files is
        true; temporary files retain their original 24-hour expiry. Deletion remains
        available for inactive teams.

        Args:
          delete_files: DeleteFiles specifies whether to permanently delete this Thumbnail's owned
              images, sprite sheets, VTT and partial outputs at their saved storage prefix.
              Defaults to false. The Source and unrelated files are preserved. If deletion
              fails, records remain for retry, but some files may already be deleted.
              Temporary outputs still expire when this option is false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thumbnail_id:
            raise ValueError(f"Expected a non-empty value for `thumbnail_id` but received {thumbnail_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/thumbnails/{thumbnail_id}", thumbnail_id=thumbnail_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"delete_files": delete_files}, thumbnail_delete_params.ThumbnailDeleteParams),
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class AsyncThumbnailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncThumbnailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncThumbnailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThumbnailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncThumbnailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        source_id: str,
        count: int | Omit = omit,
        format: Literal["jpeg", "webp"] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        output: Literal["images", "sprites"] | Omit = omit,
        range: thumbnail_create_params.Range | Omit = omit,
        size: int | Omit = omit,
        storage: thumbnail_create_params.Storage | Omit = omit,
        timestamps: Iterable[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Thumbnail:
        """Generate individual images or sprite sheets from a Source.

        Each accepted request
        creates a new resource. Processing continues after the response.

        Args:
          source_id: SourceId identifies a video Source in this Project.

          count: Count specifies 1 to 100 thumbnails at the middle of equal sections of the
              selected range.

          format: Format selects JPEG or WebP. Defaults to JPEG.

          metadata: Metadata attaches string values to this request. The serialized object may
              contain at most 2048 bytes.

          output: Output selects images or sprites. Defaults to images.

          range: Range limits sampling to part of the Source. Defaults to the whole Source
              duration.

          size: Size specifies the maximum image or tile edge in pixels, from 64 to 1920.
              Defaults to 320. Odd sizes are supported. Preserves display aspect ratio without
              cropping or upscaling.

          storage: Storage overrides the Project output destination and names the output files.
              Source storage remains independent.

          timestamps: Timestamps specifies 1 to 100 Source-relative target times in seconds. Every
              time must be within the selected range. Repeated targets produce separate
              outputs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/thumbnails",
            body=await async_maybe_transform(
                {
                    "source_id": source_id,
                    "count": count,
                    "format": format,
                    "metadata": metadata,
                    "output": output,
                    "range": range,
                    "size": size,
                    "storage": storage,
                    "timestamps": timestamps,
                },
                thumbnail_create_params.ThumbnailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Thumbnail]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Thumbnail], DataWrapper[Thumbnail]),
        )

    async def retrieve(
        self,
        thumbnail_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Thumbnail:
        """
        Retrieve the accepted settings, published files and current state of one
        Thumbnail.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thumbnail_id:
            raise ValueError(f"Expected a non-empty value for `thumbnail_id` but received {thumbnail_id!r}")
        return await self._get(
            path_template("/thumbnails/{thumbnail_id}", thumbnail_id=thumbnail_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Thumbnail]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Thumbnail], DataWrapper[Thumbnail]),
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        created: thumbnail_list_params.Created | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        source_id: str | Omit = omit,
        status: Literal["preparing", "ready", "failed", "expired"] | Omit = omit,
        storage_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Thumbnail, AsyncPaginatedResults[Thumbnail]]:
        """
        List Thumbnails in the authenticated Project, newest first by default.

        Args:
          id: Id filters by an exact Thumbnail ID. Omit to include all matching resources.

          limit: Maximum number of Thumbnails to return.

          offset: Number of Thumbnails to skip.

          source_id: Filter Thumbnails linked to this Source. Omit to include Thumbnails from all
              Sources in the Project.

          status: Filter by Thumbnail status.

          storage_id: Filter by output Storage ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/thumbnails",
            page=AsyncPaginatedResults[Thumbnail],
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
                    thumbnail_list_params.ThumbnailListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Thumbnail,
        )

    async def delete(
        self,
        thumbnail_id: str,
        *,
        delete_files: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a ready, failed or expired Thumbnail after all workers have stopped.

        The
        Source and settled usage are preserved. Files remain unless delete_files is
        true; temporary files retain their original 24-hour expiry. Deletion remains
        available for inactive teams.

        Args:
          delete_files: DeleteFiles specifies whether to permanently delete this Thumbnail's owned
              images, sprite sheets, VTT and partial outputs at their saved storage prefix.
              Defaults to false. The Source and unrelated files are preserved. If deletion
              fails, records remain for retry, but some files may already be deleted.
              Temporary outputs still expire when this option is false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not thumbnail_id:
            raise ValueError(f"Expected a non-empty value for `thumbnail_id` but received {thumbnail_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/thumbnails/{thumbnail_id}", thumbnail_id=thumbnail_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"delete_files": delete_files}, thumbnail_delete_params.ThumbnailDeleteParams
                ),
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class ThumbnailsResourceWithRawResponse:
    def __init__(self, thumbnails: ThumbnailsResource) -> None:
        self._thumbnails = thumbnails

        self.create = to_raw_response_wrapper(
            thumbnails.create,
        )
        self.retrieve = to_raw_response_wrapper(
            thumbnails.retrieve,
        )
        self.list = to_raw_response_wrapper(
            thumbnails.list,
        )
        self.delete = to_raw_response_wrapper(
            thumbnails.delete,
        )


class AsyncThumbnailsResourceWithRawResponse:
    def __init__(self, thumbnails: AsyncThumbnailsResource) -> None:
        self._thumbnails = thumbnails

        self.create = async_to_raw_response_wrapper(
            thumbnails.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            thumbnails.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            thumbnails.list,
        )
        self.delete = async_to_raw_response_wrapper(
            thumbnails.delete,
        )


class ThumbnailsResourceWithStreamingResponse:
    def __init__(self, thumbnails: ThumbnailsResource) -> None:
        self._thumbnails = thumbnails

        self.create = to_streamed_response_wrapper(
            thumbnails.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            thumbnails.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            thumbnails.list,
        )
        self.delete = to_streamed_response_wrapper(
            thumbnails.delete,
        )


class AsyncThumbnailsResourceWithStreamingResponse:
    def __init__(self, thumbnails: AsyncThumbnailsResource) -> None:
        self._thumbnails = thumbnails

        self.create = async_to_streamed_response_wrapper(
            thumbnails.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            thumbnails.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            thumbnails.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            thumbnails.delete,
        )
