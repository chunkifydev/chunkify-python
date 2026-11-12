# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast

import httpx

from ..types import storage_create_params, storage_update_params
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
from .._base_client import make_request_options
from ..types.storage import Storage
from ..types.storage_list_response import StorageListResponse

__all__ = ["StoragesResource", "AsyncStoragesResource"]


class StoragesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StoragesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return StoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StoragesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return StoragesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        storage: storage_create_params.Storage,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """
        Create a new storage configuration for cloud storage providers like AWS S3,
        Cloudflare R2, etc. The storage credentials will be validated before saving.

        Args:
          storage: The parameters for creating a new storage configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Storage,
            self._post(
                "/storages",
                body=maybe_transform(storage, storage_create_params.StorageCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=DataWrapper[Storage]._unwrapper,
                    security={"project_access_token": True},
                ),
                cast_to=cast(
                    Any, DataWrapper[Storage]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve(
        self,
        storage_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """
        Retrieve details of a specific storage configuration by its id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not storage_id:
            raise ValueError(f"Expected a non-empty value for `storage_id` but received {storage_id!r}")
        return cast(
            Storage,
            self._get(
                path_template("/storages/{storage_id}", storage_id=storage_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=DataWrapper[Storage]._unwrapper,
                    security={"project_access_token": True},
                ),
                cast_to=cast(
                    Any, DataWrapper[Storage]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        storage_id: str,
        *,
        access_key_id: str | Omit = omit,
        base_prefix: str | Omit = omit,
        cdn_base_url: Optional[str] | Omit = omit,
        secret_access_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Update customer-owned storage settings.

        Send access_key_id and secret_access_key
        together to rotate credentials for AWS S3, Cloudflare R2, or S3-compatible
        storage. Both values must be non-empty and non-null. Omitting both preserves the
        saved pair and skips connection validation. Replacement credentials are checked
        against the saved bucket, endpoint, region, and addressing style using the
        creation upload, metadata, and download checks with best-effort probe cleanup. A
        prefix changed in the same request is used for validation. Both credentials are
        encrypted and saved atomically with other settings; a failed update preserves
        the previous values. Credential-only updates keep the Storage ID, resource
        associations, object paths, and Project default. Subsequent storage lookups use
        the new pair; running work may retain an existing client or signed URL. Rotation
        does not renew issued URLs, and revoking old keys can invalidate them. Prefix
        changes apply to final outputs that have not been uploaded yet. Existing files
        keep their stored object keys.

        Args:
          access_key_id: Replacement access key ID for customer-managed storage. Send with a non-empty
              secret_access_key. Omit both credential fields to keep the saved pair. Null and
              empty values are rejected. Credentials are validated before either value is
              saved and are never returned.

          base_prefix: Object-key prefix for future final job outputs. Existing files keep their stored
              object keys. Send an empty string to use the bucket root.

          cdn_base_url: Customer-managed HTTPS delivery origin, or null to remove the current value.

          secret_access_key: Replacement secret access key. Required with access_key_id; cannot be null or
              empty. The pair is encrypted and saved atomically only after validation
              succeeds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not storage_id:
            raise ValueError(f"Expected a non-empty value for `storage_id` but received {storage_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/storages/{storage_id}", storage_id=storage_id),
            body=maybe_transform(
                {
                    "access_key_id": access_key_id,
                    "base_prefix": base_prefix,
                    "cdn_base_url": cdn_base_url,
                    "secret_access_key": secret_access_key,
                },
                storage_update_params.StorageUpdateParams,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StorageListResponse:
        """Retrieve a list of all storage configurations for the current project."""
        return self._get(
            "/storages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=StorageListResponse,
        )

    def delete(
        self,
        storage_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a storage configuration.

        The storage must not be currently attached to
        the project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not storage_id:
            raise ValueError(f"Expected a non-empty value for `storage_id` but received {storage_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/storages/{storage_id}", storage_id=storage_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class AsyncStoragesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStoragesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStoragesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncStoragesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        storage: storage_create_params.Storage,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """
        Create a new storage configuration for cloud storage providers like AWS S3,
        Cloudflare R2, etc. The storage credentials will be validated before saving.

        Args:
          storage: The parameters for creating a new storage configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            Storage,
            await self._post(
                "/storages",
                body=await async_maybe_transform(storage, storage_create_params.StorageCreateParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=DataWrapper[Storage]._unwrapper,
                    security={"project_access_token": True},
                ),
                cast_to=cast(
                    Any, DataWrapper[Storage]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve(
        self,
        storage_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        """
        Retrieve details of a specific storage configuration by its id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not storage_id:
            raise ValueError(f"Expected a non-empty value for `storage_id` but received {storage_id!r}")
        return cast(
            Storage,
            await self._get(
                path_template("/storages/{storage_id}", storage_id=storage_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=DataWrapper[Storage]._unwrapper,
                    security={"project_access_token": True},
                ),
                cast_to=cast(
                    Any, DataWrapper[Storage]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        storage_id: str,
        *,
        access_key_id: str | Omit = omit,
        base_prefix: str | Omit = omit,
        cdn_base_url: Optional[str] | Omit = omit,
        secret_access_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Update customer-owned storage settings.

        Send access_key_id and secret_access_key
        together to rotate credentials for AWS S3, Cloudflare R2, or S3-compatible
        storage. Both values must be non-empty and non-null. Omitting both preserves the
        saved pair and skips connection validation. Replacement credentials are checked
        against the saved bucket, endpoint, region, and addressing style using the
        creation upload, metadata, and download checks with best-effort probe cleanup. A
        prefix changed in the same request is used for validation. Both credentials are
        encrypted and saved atomically with other settings; a failed update preserves
        the previous values. Credential-only updates keep the Storage ID, resource
        associations, object paths, and Project default. Subsequent storage lookups use
        the new pair; running work may retain an existing client or signed URL. Rotation
        does not renew issued URLs, and revoking old keys can invalidate them. Prefix
        changes apply to final outputs that have not been uploaded yet. Existing files
        keep their stored object keys.

        Args:
          access_key_id: Replacement access key ID for customer-managed storage. Send with a non-empty
              secret_access_key. Omit both credential fields to keep the saved pair. Null and
              empty values are rejected. Credentials are validated before either value is
              saved and are never returned.

          base_prefix: Object-key prefix for future final job outputs. Existing files keep their stored
              object keys. Send an empty string to use the bucket root.

          cdn_base_url: Customer-managed HTTPS delivery origin, or null to remove the current value.

          secret_access_key: Replacement secret access key. Required with access_key_id; cannot be null or
              empty. The pair is encrypted and saved atomically only after validation
              succeeds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not storage_id:
            raise ValueError(f"Expected a non-empty value for `storage_id` but received {storage_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/storages/{storage_id}", storage_id=storage_id),
            body=await async_maybe_transform(
                {
                    "access_key_id": access_key_id,
                    "base_prefix": base_prefix,
                    "cdn_base_url": cdn_base_url,
                    "secret_access_key": secret_access_key,
                },
                storage_update_params.StorageUpdateParams,
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

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StorageListResponse:
        """Retrieve a list of all storage configurations for the current project."""
        return await self._get(
            "/storages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=StorageListResponse,
        )

    async def delete(
        self,
        storage_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a storage configuration.

        The storage must not be currently attached to
        the project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not storage_id:
            raise ValueError(f"Expected a non-empty value for `storage_id` but received {storage_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/storages/{storage_id}", storage_id=storage_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class StoragesResourceWithRawResponse:
    def __init__(self, storages: StoragesResource) -> None:
        self._storages = storages

        self.create = to_raw_response_wrapper(
            storages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            storages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            storages.update,
        )
        self.list = to_raw_response_wrapper(
            storages.list,
        )
        self.delete = to_raw_response_wrapper(
            storages.delete,
        )


class AsyncStoragesResourceWithRawResponse:
    def __init__(self, storages: AsyncStoragesResource) -> None:
        self._storages = storages

        self.create = async_to_raw_response_wrapper(
            storages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            storages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            storages.update,
        )
        self.list = async_to_raw_response_wrapper(
            storages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            storages.delete,
        )


class StoragesResourceWithStreamingResponse:
    def __init__(self, storages: StoragesResource) -> None:
        self._storages = storages

        self.create = to_streamed_response_wrapper(
            storages.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            storages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            storages.update,
        )
        self.list = to_streamed_response_wrapper(
            storages.list,
        )
        self.delete = to_streamed_response_wrapper(
            storages.delete,
        )


class AsyncStoragesResourceWithStreamingResponse:
    def __init__(self, storages: AsyncStoragesResource) -> None:
        self._storages = storages

        self.create = async_to_streamed_response_wrapper(
            storages.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            storages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            storages.update,
        )
        self.list = async_to_streamed_response_wrapper(
            storages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            storages.delete,
        )
