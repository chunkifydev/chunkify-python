# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.projects.analytics.connections import key_create_params
from .....types.projects.analytics.connections.key_list_response import KeyListResponse
from .....types.projects.analytics.connections.key_create_response import KeyCreateResponse
from .....types.projects.analytics.connections.key_rotate_response import KeyRotateResponse

__all__ = ["KeysResource", "AsyncKeysResource"]


class KeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return KeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return KeysResourceWithStreamingResponse(self)

    def create(
        self,
        connection_id: str,
        *,
        project_id: str,
        purpose: Literal["player", "read", "mcp"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyCreateResponse:
        """
        Generate a public key for players to send events, or a read-only secret key for
        a dashboard or MCP client to query a hosted Chunkify Analytics server. Save
        secret keys when returned. Requires a team owner and a Team Access Key.

        Args:
          purpose: Purpose distinguishes player ingestion, read-only API access and a separate
              read-only MCP credential. Read and MCP keys have the same collector permissions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._post(
            path_template(
                "/projects/{project_id}/analytics/connections/{connection_id}/keys",
                project_id=project_id,
                connection_id=connection_id,
            ),
            body=maybe_transform({"purpose": purpose}, key_create_params.KeyCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"team_access_token": True},
            ),
            cast_to=KeyCreateResponse,
        )

    def list(
        self,
        connection_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyListResponse:
        """
        List keys for a hosted Chunkify Analytics server: the public key used by players
        to send events, and read-only secret key records for dashboard and MCP access.
        Secret values are not returned. Requires a team owner and a Team Access Key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._get(
            path_template(
                "/projects/{project_id}/analytics/connections/{connection_id}/keys",
                project_id=project_id,
                connection_id=connection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"team_access_token": True},
            ),
            cast_to=KeyListResponse,
        )

    def rotate(
        self,
        key_id: str,
        *,
        project_id: str,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyRotateResponse:
        """
        Rotate a public or read-only secret key for a hosted Chunkify Analytics server.
        Update the player, dashboard, or MCP client with the new key; the old key stops
        working immediately. Requires a team owner and a Team Access Key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return self._post(
            path_template(
                "/projects/{project_id}/analytics/connections/{connection_id}/keys/{key_id}/rotate",
                project_id=project_id,
                connection_id=connection_id,
                key_id=key_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"team_access_token": True},
            ),
            cast_to=KeyRotateResponse,
        )


class AsyncKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        connection_id: str,
        *,
        project_id: str,
        purpose: Literal["player", "read", "mcp"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyCreateResponse:
        """
        Generate a public key for players to send events, or a read-only secret key for
        a dashboard or MCP client to query a hosted Chunkify Analytics server. Save
        secret keys when returned. Requires a team owner and a Team Access Key.

        Args:
          purpose: Purpose distinguishes player ingestion, read-only API access and a separate
              read-only MCP credential. Read and MCP keys have the same collector permissions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._post(
            path_template(
                "/projects/{project_id}/analytics/connections/{connection_id}/keys",
                project_id=project_id,
                connection_id=connection_id,
            ),
            body=await async_maybe_transform({"purpose": purpose}, key_create_params.KeyCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"team_access_token": True},
            ),
            cast_to=KeyCreateResponse,
        )

    async def list(
        self,
        connection_id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyListResponse:
        """
        List keys for a hosted Chunkify Analytics server: the public key used by players
        to send events, and read-only secret key records for dashboard and MCP access.
        Secret values are not returned. Requires a team owner and a Team Access Key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._get(
            path_template(
                "/projects/{project_id}/analytics/connections/{connection_id}/keys",
                project_id=project_id,
                connection_id=connection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"team_access_token": True},
            ),
            cast_to=KeyListResponse,
        )

    async def rotate(
        self,
        key_id: str,
        *,
        project_id: str,
        connection_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KeyRotateResponse:
        """
        Rotate a public or read-only secret key for a hosted Chunkify Analytics server.
        Update the player, dashboard, or MCP client with the new key; the old key stops
        working immediately. Requires a team owner and a Team Access Key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        return await self._post(
            path_template(
                "/projects/{project_id}/analytics/connections/{connection_id}/keys/{key_id}/rotate",
                project_id=project_id,
                connection_id=connection_id,
                key_id=key_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"team_access_token": True},
            ),
            cast_to=KeyRotateResponse,
        )


class KeysResourceWithRawResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_raw_response_wrapper(
            keys.create,
        )
        self.list = to_raw_response_wrapper(
            keys.list,
        )
        self.rotate = to_raw_response_wrapper(
            keys.rotate,
        )


class AsyncKeysResourceWithRawResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_raw_response_wrapper(
            keys.create,
        )
        self.list = async_to_raw_response_wrapper(
            keys.list,
        )
        self.rotate = async_to_raw_response_wrapper(
            keys.rotate,
        )


class KeysResourceWithStreamingResponse:
    def __init__(self, keys: KeysResource) -> None:
        self._keys = keys

        self.create = to_streamed_response_wrapper(
            keys.create,
        )
        self.list = to_streamed_response_wrapper(
            keys.list,
        )
        self.rotate = to_streamed_response_wrapper(
            keys.rotate,
        )


class AsyncKeysResourceWithStreamingResponse:
    def __init__(self, keys: AsyncKeysResource) -> None:
        self._keys = keys

        self.create = async_to_streamed_response_wrapper(
            keys.create,
        )
        self.list = async_to_streamed_response_wrapper(
            keys.list,
        )
        self.rotate = async_to_streamed_response_wrapper(
            keys.rotate,
        )
