# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal, overload

import httpx

from ..types import storage_create_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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

        For more information, see https://www.github.com/stainless-sdks/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return StoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StoragesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/chunkify-python#with_streaming_response
        """
        return StoragesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        access_key_id: str,
        bucket: str,
        provider: Literal["aws"],
        region: Literal[
            "us-east-1",
            "us-east-2",
            "us-central-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "eu-north-1",
            "ap-east-1",
            "ap-east-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
        ],
        secret_access_key: str,
        public: bool | Omit = omit,
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
          access_key_id: AccessKeyId is the access key for the storage provider. Required if not using
              Chunkify storage.

          bucket: Bucket is the name of the storage bucket.

          provider: Provider specifies the storage provider.

          region: Region specifies the region of the storage provider.

          secret_access_key: SecretAccessKey is the secret key for the storage provider. Required if not
              using Chunkify storage.

          public: Public indicates whether the storage is publicly accessible.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        provider: Literal["chunkify"],
        region: Literal[
            "us-east-1",
            "us-east-2",
            "us-central-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "eu-north-1",
            "ap-east-1",
            "ap-east-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
        ],
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
          provider: Provider specifies the storage provider.

          region: Region specifies the region of the storage provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        access_key_id: str,
        bucket: str,
        endpoint: str,
        location: Literal["US", "EU", "ASIA"],
        provider: Literal["cloudflare"],
        region: Literal["auto"],
        secret_access_key: str,
        public: bool | Omit = omit,
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
          access_key_id: AccessKeyId is the access key for the storage provider.

          bucket: Bucket is the name of the storage bucket.

          endpoint: Endpoint is the endpoint of the storage provider.

          location: Location specifies the location of the storage provider.

          provider: Provider specifies the storage provider.

          region: Region must be set to 'auto'.

          secret_access_key: SecretAccessKey is the secret key for the storage provider.

          public: Public indicates whether the storage is publicly accessible.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["access_key_id", "bucket", "provider", "region", "secret_access_key"],
        ["provider", "region"],
        ["access_key_id", "bucket", "endpoint", "location", "provider", "region", "secret_access_key"],
    )
    def create(
        self,
        *,
        access_key_id: str | Omit = omit,
        bucket: str | Omit = omit,
        provider: Literal["aws"] | Literal["chunkify"] | Literal["cloudflare"],
        region: Literal[
            "us-east-1",
            "us-east-2",
            "us-central-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "eu-north-1",
            "ap-east-1",
            "ap-east-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
        ]
        | Literal["auto"],
        secret_access_key: str | Omit = omit,
        public: bool | Omit = omit,
        endpoint: str | Omit = omit,
        location: Literal["US", "EU", "ASIA"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        return self._post(
            "/api/storages",
            body=maybe_transform(
                {
                    "access_key_id": access_key_id,
                    "bucket": bucket,
                    "provider": provider,
                    "region": region,
                    "secret_access_key": secret_access_key,
                    "public": public,
                    "endpoint": endpoint,
                    "location": location,
                },
                storage_create_params.StorageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Storage]._unwrapper,
            ),
            cast_to=cast(Type[Storage], DataWrapper[Storage]),
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
        return self._get(
            f"/api/storages/{storage_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Storage]._unwrapper,
            ),
            cast_to=cast(Type[Storage], DataWrapper[Storage]),
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
            "/api/storages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
            f"/api/storages/{storage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncStoragesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStoragesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStoragesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStoragesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/chunkify-python#with_streaming_response
        """
        return AsyncStoragesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        access_key_id: str,
        bucket: str,
        provider: Literal["aws"],
        region: Literal[
            "us-east-1",
            "us-east-2",
            "us-central-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "eu-north-1",
            "ap-east-1",
            "ap-east-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
        ],
        secret_access_key: str,
        public: bool | Omit = omit,
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
          access_key_id: AccessKeyId is the access key for the storage provider. Required if not using
              Chunkify storage.

          bucket: Bucket is the name of the storage bucket.

          provider: Provider specifies the storage provider.

          region: Region specifies the region of the storage provider.

          secret_access_key: SecretAccessKey is the secret key for the storage provider. Required if not
              using Chunkify storage.

          public: Public indicates whether the storage is publicly accessible.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        provider: Literal["chunkify"],
        region: Literal[
            "us-east-1",
            "us-east-2",
            "us-central-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "eu-north-1",
            "ap-east-1",
            "ap-east-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
        ],
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
          provider: Provider specifies the storage provider.

          region: Region specifies the region of the storage provider.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        access_key_id: str,
        bucket: str,
        endpoint: str,
        location: Literal["US", "EU", "ASIA"],
        provider: Literal["cloudflare"],
        region: Literal["auto"],
        secret_access_key: str,
        public: bool | Omit = omit,
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
          access_key_id: AccessKeyId is the access key for the storage provider.

          bucket: Bucket is the name of the storage bucket.

          endpoint: Endpoint is the endpoint of the storage provider.

          location: Location specifies the location of the storage provider.

          provider: Provider specifies the storage provider.

          region: Region must be set to 'auto'.

          secret_access_key: SecretAccessKey is the secret key for the storage provider.

          public: Public indicates whether the storage is publicly accessible.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["access_key_id", "bucket", "provider", "region", "secret_access_key"],
        ["provider", "region"],
        ["access_key_id", "bucket", "endpoint", "location", "provider", "region", "secret_access_key"],
    )
    async def create(
        self,
        *,
        access_key_id: str | Omit = omit,
        bucket: str | Omit = omit,
        provider: Literal["aws"] | Literal["chunkify"] | Literal["cloudflare"],
        region: Literal[
            "us-east-1",
            "us-east-2",
            "us-central-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "eu-north-1",
            "ap-east-1",
            "ap-east-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
        ]
        | Literal["auto"],
        secret_access_key: str | Omit = omit,
        public: bool | Omit = omit,
        endpoint: str | Omit = omit,
        location: Literal["US", "EU", "ASIA"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Storage:
        return await self._post(
            "/api/storages",
            body=await async_maybe_transform(
                {
                    "access_key_id": access_key_id,
                    "bucket": bucket,
                    "provider": provider,
                    "region": region,
                    "secret_access_key": secret_access_key,
                    "public": public,
                    "endpoint": endpoint,
                    "location": location,
                },
                storage_create_params.StorageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Storage]._unwrapper,
            ),
            cast_to=cast(Type[Storage], DataWrapper[Storage]),
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
        return await self._get(
            f"/api/storages/{storage_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Storage]._unwrapper,
            ),
            cast_to=cast(Type[Storage], DataWrapper[Storage]),
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
            "/api/storages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
            f"/api/storages/{storage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        self.list = async_to_streamed_response_wrapper(
            storages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            storages.delete,
        )
