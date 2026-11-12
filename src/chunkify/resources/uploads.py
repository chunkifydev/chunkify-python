# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import upload_list_params, upload_create_params, upload_complete_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.upload import Upload

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return UploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return UploadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        create_asset: bool | Omit = omit,
        file_size_bytes: int | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        storage: upload_create_params.Storage | Omit = omit,
        upload_mode: Literal["single", "multipart", "auto"] | Omit = omit,
        validity_timeout: int | Omit = omit,
        workflow_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Upload:
        """Create an Upload session for a direct transfer to storage.

        Multipart creation
        returns every signed part URL. Retry parts with their original URLs and complete
        before expiry. Customer storage requires long-lived credentials and an
        incomplete-multipart lifecycle rule. Start a new Upload after abandoning a
        session.

        Args:
          create_asset: CreateAsset specifies whether to create an Asset after Upload completion.
              Defaults to false. Snapshots the Project output settings, including the path
              template. Referenced metadata must be non-empty in this request. Asset
              processing is billed separately.

          file_size_bytes: FileSizeBytes specifies the exact file size in bytes. Required when UploadMode
              is omitted, auto, or multipart. Optional for explicit single mode. Must fit the
              team's Source size limit. Single PUT supports up to 5 GiB, subject to the
              provider's limit; multipart supports up to 5 TiB.

          metadata: Metadata allows for additional information to be attached to the upload, with a
              maximum size of 2048 bytes.

          storage: Optional Storage override. Omit id to use the Project default.
              Customer-connected Storage requires path; Chunkify Storage generates its own
              path.

          upload_mode: UploadMode specifies the transfer method. Defaults to auto. Auto chooses
              multipart above 100 MiB and single PUT at or below 100 MiB for every Storage
              provider. Multipart requires a provider that supports the required multipart
              operations and signed part URLs. Provider failures return an error without
              falling back to single PUT.

          validity_timeout: ValidityTimeout specifies the session and signed URL lifetime in seconds. Single
              PUT defaults to 7200 and allows 300–36000. Multipart defaults to twice the
              transfer time at 5 Mbps plus 1800 seconds, bounded to 7200–172800; an explicit
              value allows 300–172800. Complete before expiry. Storage credentials and
              policies can shorten URL validity. Expired URLs cannot be refreshed.

          workflow_id: WorkflowId specifies the Workflow to select. Omit to use the Project default.
              Set null to disable automatic actions. The current revision is pinned when
              creation is accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/uploads",
            body=maybe_transform(
                {
                    "create_asset": create_asset,
                    "file_size_bytes": file_size_bytes,
                    "metadata": metadata,
                    "storage": storage,
                    "upload_mode": upload_mode,
                    "validity_timeout": validity_timeout,
                    "workflow_id": workflow_id,
                },
                upload_create_params.UploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Upload]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Upload], DataWrapper[Upload]),
        )

    def retrieve(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Upload:
        """
        Retrieve details of a specific upload by its ID, including metadata, status, and
        associated source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return self._get(
            path_template("/uploads/{upload_id}", upload_id=upload_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Upload]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Upload], DataWrapper[Upload]),
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        created: upload_list_params.Created | Omit = omit,
        limit: int | Omit = omit,
        metadata: Iterable[SequenceNotStr[str]] | Omit = omit,
        offset: int | Omit = omit,
        source_id: str | Omit = omit,
        status: Literal["waiting", "completed", "failed", "expired"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResults[Upload]:
        """
        Retrieve a list of all uploads with optional filtering and pagination.

        Args:
          id: Filter by upload ID

          limit: Pagination limit (max 100)

          metadata: Filter by metadata

          offset: Pagination offset

          source_id: Filter by source ID

          status: Filter by status (pending, completed, error)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/uploads",
            page=SyncPaginatedResults[Upload],
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
                        "metadata": metadata,
                        "offset": offset,
                        "source_id": source_id,
                        "status": status,
                    },
                    upload_list_params.UploadListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Upload,
        )

    def delete(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an upload.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/uploads/{upload_id}", upload_id=upload_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )

    def complete(
        self,
        token: str,
        *,
        parts: Iterable[upload_complete_params.Part],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """POST the returned completion_url before expires_at.

        Single-PUT Uploads send no
        body; multipart Uploads send every part number and storage ETag. Chunkify
        verifies the assembled object and atomically creates the Source and optional
        Asset. An Asset destination conflict returns 409 and fails the Upload without
        committing Source, Asset, or usage changes. Valid retries return 204 without
        duplicate side effects. Retry network errors, 429, and 5xx responses with
        bounded backoff.

        Args:
          parts: All uploaded parts in ascending part_number order, with the ETags returned by
              storage.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/uploads/completion/{token}", token=token),
            body=maybe_transform({"parts": parts}, upload_complete_params.UploadCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )


class AsyncUploadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncUploadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        create_asset: bool | Omit = omit,
        file_size_bytes: int | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        storage: upload_create_params.Storage | Omit = omit,
        upload_mode: Literal["single", "multipart", "auto"] | Omit = omit,
        validity_timeout: int | Omit = omit,
        workflow_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Upload:
        """Create an Upload session for a direct transfer to storage.

        Multipart creation
        returns every signed part URL. Retry parts with their original URLs and complete
        before expiry. Customer storage requires long-lived credentials and an
        incomplete-multipart lifecycle rule. Start a new Upload after abandoning a
        session.

        Args:
          create_asset: CreateAsset specifies whether to create an Asset after Upload completion.
              Defaults to false. Snapshots the Project output settings, including the path
              template. Referenced metadata must be non-empty in this request. Asset
              processing is billed separately.

          file_size_bytes: FileSizeBytes specifies the exact file size in bytes. Required when UploadMode
              is omitted, auto, or multipart. Optional for explicit single mode. Must fit the
              team's Source size limit. Single PUT supports up to 5 GiB, subject to the
              provider's limit; multipart supports up to 5 TiB.

          metadata: Metadata allows for additional information to be attached to the upload, with a
              maximum size of 2048 bytes.

          storage: Optional Storage override. Omit id to use the Project default.
              Customer-connected Storage requires path; Chunkify Storage generates its own
              path.

          upload_mode: UploadMode specifies the transfer method. Defaults to auto. Auto chooses
              multipart above 100 MiB and single PUT at or below 100 MiB for every Storage
              provider. Multipart requires a provider that supports the required multipart
              operations and signed part URLs. Provider failures return an error without
              falling back to single PUT.

          validity_timeout: ValidityTimeout specifies the session and signed URL lifetime in seconds. Single
              PUT defaults to 7200 and allows 300–36000. Multipart defaults to twice the
              transfer time at 5 Mbps plus 1800 seconds, bounded to 7200–172800; an explicit
              value allows 300–172800. Complete before expiry. Storage credentials and
              policies can shorten URL validity. Expired URLs cannot be refreshed.

          workflow_id: WorkflowId specifies the Workflow to select. Omit to use the Project default.
              Set null to disable automatic actions. The current revision is pinned when
              creation is accepted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/uploads",
            body=await async_maybe_transform(
                {
                    "create_asset": create_asset,
                    "file_size_bytes": file_size_bytes,
                    "metadata": metadata,
                    "storage": storage,
                    "upload_mode": upload_mode,
                    "validity_timeout": validity_timeout,
                    "workflow_id": workflow_id,
                },
                upload_create_params.UploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Upload]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Upload], DataWrapper[Upload]),
        )

    async def retrieve(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Upload:
        """
        Retrieve details of a specific upload by its ID, including metadata, status, and
        associated source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        return await self._get(
            path_template("/uploads/{upload_id}", upload_id=upload_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Upload]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Upload], DataWrapper[Upload]),
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        created: upload_list_params.Created | Omit = omit,
        limit: int | Omit = omit,
        metadata: Iterable[SequenceNotStr[str]] | Omit = omit,
        offset: int | Omit = omit,
        source_id: str | Omit = omit,
        status: Literal["waiting", "completed", "failed", "expired"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Upload, AsyncPaginatedResults[Upload]]:
        """
        Retrieve a list of all uploads with optional filtering and pagination.

        Args:
          id: Filter by upload ID

          limit: Pagination limit (max 100)

          metadata: Filter by metadata

          offset: Pagination offset

          source_id: Filter by source ID

          status: Filter by status (pending, completed, error)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/uploads",
            page=AsyncPaginatedResults[Upload],
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
                        "metadata": metadata,
                        "offset": offset,
                        "source_id": source_id,
                        "status": status,
                    },
                    upload_list_params.UploadListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Upload,
        )

    async def delete(
        self,
        upload_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an upload.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not upload_id:
            raise ValueError(f"Expected a non-empty value for `upload_id` but received {upload_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/uploads/{upload_id}", upload_id=upload_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )

    async def complete(
        self,
        token: str,
        *,
        parts: Iterable[upload_complete_params.Part],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """POST the returned completion_url before expires_at.

        Single-PUT Uploads send no
        body; multipart Uploads send every part number and storage ETag. Chunkify
        verifies the assembled object and atomically creates the Source and optional
        Asset. An Asset destination conflict returns 409 and fails the Upload without
        committing Source, Asset, or usage changes. Valid retries return 204 without
        duplicate side effects. Retry network errors, 429, and 5xx responses with
        bounded backoff.

        Args:
          parts: All uploaded parts in ascending part_number order, with the ETags returned by
              storage.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/uploads/completion/{token}", token=token),
            body=await async_maybe_transform({"parts": parts}, upload_complete_params.UploadCompleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={},
            ),
            cast_to=NoneType,
        )


class UploadsResourceWithRawResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_raw_response_wrapper(
            uploads.create,
        )
        self.retrieve = to_raw_response_wrapper(
            uploads.retrieve,
        )
        self.list = to_raw_response_wrapper(
            uploads.list,
        )
        self.delete = to_raw_response_wrapper(
            uploads.delete,
        )
        self.complete = to_raw_response_wrapper(
            uploads.complete,
        )


class AsyncUploadsResourceWithRawResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_raw_response_wrapper(
            uploads.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            uploads.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            uploads.list,
        )
        self.delete = async_to_raw_response_wrapper(
            uploads.delete,
        )
        self.complete = async_to_raw_response_wrapper(
            uploads.complete,
        )


class UploadsResourceWithStreamingResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_streamed_response_wrapper(
            uploads.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            uploads.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            uploads.list,
        )
        self.delete = to_streamed_response_wrapper(
            uploads.delete,
        )
        self.complete = to_streamed_response_wrapper(
            uploads.complete,
        )


class AsyncUploadsResourceWithStreamingResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_streamed_response_wrapper(
            uploads.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            uploads.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            uploads.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            uploads.delete,
        )
        self.complete = async_to_streamed_response_wrapper(
            uploads.complete,
        )
