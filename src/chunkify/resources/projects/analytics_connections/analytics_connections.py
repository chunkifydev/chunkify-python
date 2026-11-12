# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import DataWrapper
from ...._base_client import make_request_options
from ....types.projects import analytics_connection_create_params, analytics_connection_update_params
from ....types.projects.analytics_connection import AnalyticsConnection
from ....types.projects.analytics_connection_list_response import AnalyticsConnectionListResponse
from ....types.projects.analytics_connection_create_response import AnalyticsConnectionCreateResponse

__all__ = ["AnalyticsConnectionsResource", "AsyncAnalyticsConnectionsResource"]


class AnalyticsConnectionsResource(SyncAPIResource):
    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AnalyticsConnectionsResourceWithStreamingResponse(self)

    def create(
        self,
        project_id: str,
        *,
        name: str,
        type: Literal["hosted", "custom"],
        endpoint: str | Omit = omit,
        public_ingest_key: str | Omit = omit,
        read_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsConnectionCreateResponse:
        """Add a hosted connection or validate and save a custom server.

        Only team owners
        can create connections. Retry a known failed hosted setup with the same name to
        resume its saved project; an unknown creation outcome requires operator
        reconciliation.

        Args:
          name: Name identifies this connection in the dashboard.

          type: Type specifies whether Chunkify manages the analytics project.

          endpoint: Endpoint specifies the custom server base URL. Required for custom connections
              and omitted for hosted connections.

          public_ingest_key: PublicIngestKey optionally enables preview tracking for a custom connection.
              Supply the public ingestion key for the same analytics project as read_key. It
              is returned in connection reads and used in browser code. Omit for hosted
              connections.

          read_key: ReadKey supplies a read-only project credential for a custom connection.
              Required for custom connections and omitted for hosted connections. Stored
              encrypted and never returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            path_template("/projects/{project_id}/analytics/connections", project_id=project_id),
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "endpoint": endpoint,
                    "public_ingest_key": public_ingest_key,
                    "read_key": read_key,
                },
                analytics_connection_create_params.AnalyticsConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"team_access_token": True},
            ),
            cast_to=AnalyticsConnectionCreateResponse,
        )

    def retrieve(
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
    ) -> AnalyticsConnection:
        """
        Retrieve non-secret connection metadata within its owning project.

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
                "/projects/{project_id}/analytics/connections/{connection_id}",
                project_id=project_id,
                connection_id=connection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[AnalyticsConnection]._unwrapper,
                security={"team_access_token": True},
            ),
            cast_to=cast(Type[AnalyticsConnection], DataWrapper[AnalyticsConnection]),
        )

    def update(
        self,
        connection_id: str,
        *,
        project_id: str,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        default_for_dashboard: bool | Omit = omit,
        endpoint: str | Omit = omit,
        name: str | Omit = omit,
        public_ingest_key: str | Omit = omit,
        read_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsConnection:
        """Rename a connection or validate replacement custom credentials.

        Only team owners
        can update connections. Existing settings remain unchanged if validation fails.

        Args:
          allowed_origins: AllowedOrigins lists additional website origins permitted to ingest events for a
              hosted connection. Shared installation origins remain allowed. An empty list
              clears project-specific origins. Custom servers manage origins on their own
              infrastructure.

          default_for_dashboard: DefaultForDashboard selects this ready connection for Chunkify dashboard
              players, public previews, the playground and newly generated snippets. Requires
              a public ingest key. Setting true replaces the previous default atomically.
              Setting false disables dashboard tracking if no default remains; another
              connection is not selected automatically. Existing external players keep their
              own configuration.

          endpoint: Endpoint specifies a replacement custom server base URL. Supply read_key
              together with it.

          name: Name identifies this connection in the dashboard.

          public_ingest_key: PublicIngestKey optionally enables preview tracking for a custom connection.
              Supply the public ingestion key for the same analytics project as read_key. It
              is returned in connection reads and used in browser code. Omit for hosted
              connections. An empty string disables preview tracking. A replacement endpoint
              clears the saved public key unless a replacement is supplied.

          read_key: ReadKey replaces the custom connection credential after validation. Its value is
              never returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return self._patch(
            path_template(
                "/projects/{project_id}/analytics/connections/{connection_id}",
                project_id=project_id,
                connection_id=connection_id,
            ),
            body=maybe_transform(
                {
                    "allowed_origins": allowed_origins,
                    "default_for_dashboard": default_for_dashboard,
                    "endpoint": endpoint,
                    "name": name,
                    "public_ingest_key": public_ingest_key,
                    "read_key": read_key,
                },
                analytics_connection_update_params.AnalyticsConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[AnalyticsConnection]._unwrapper,
                security={"team_access_token": True},
            ),
            cast_to=cast(Type[AnalyticsConnection], DataWrapper[AnalyticsConnection]),
        )

    def list(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsConnectionListResponse:
        """List the saved connections for this project.

        No connection is activated by this
        request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/projects/{project_id}/analytics/connections", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"team_access_token": True},
            ),
            cast_to=AnalyticsConnectionListResponse,
        )

    def delete(
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
    ) -> None:
        """
        For hosted connections, delete the linked analytics project and invalidate its
        keys before removing the saved connection. Stored events expire under the
        collector retention policy. For custom connections, remove only the saved
        credentials and connection; the remote server, project and data remain
        unchanged. Only team owners can delete connections. An uncertain remote result
        preserves the connection for reconciliation.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/projects/{project_id}/analytics/connections/{connection_id}",
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
            cast_to=NoneType,
        )


class AsyncAnalyticsConnectionsResource(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsConnectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsConnectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsConnectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncAnalyticsConnectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        project_id: str,
        *,
        name: str,
        type: Literal["hosted", "custom"],
        endpoint: str | Omit = omit,
        public_ingest_key: str | Omit = omit,
        read_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsConnectionCreateResponse:
        """Add a hosted connection or validate and save a custom server.

        Only team owners
        can create connections. Retry a known failed hosted setup with the same name to
        resume its saved project; an unknown creation outcome requires operator
        reconciliation.

        Args:
          name: Name identifies this connection in the dashboard.

          type: Type specifies whether Chunkify manages the analytics project.

          endpoint: Endpoint specifies the custom server base URL. Required for custom connections
              and omitted for hosted connections.

          public_ingest_key: PublicIngestKey optionally enables preview tracking for a custom connection.
              Supply the public ingestion key for the same analytics project as read_key. It
              is returned in connection reads and used in browser code. Omit for hosted
              connections.

          read_key: ReadKey supplies a read-only project credential for a custom connection.
              Required for custom connections and omitted for hosted connections. Stored
              encrypted and never returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            path_template("/projects/{project_id}/analytics/connections", project_id=project_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "endpoint": endpoint,
                    "public_ingest_key": public_ingest_key,
                    "read_key": read_key,
                },
                analytics_connection_create_params.AnalyticsConnectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"team_access_token": True},
            ),
            cast_to=AnalyticsConnectionCreateResponse,
        )

    async def retrieve(
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
    ) -> AnalyticsConnection:
        """
        Retrieve non-secret connection metadata within its owning project.

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
                "/projects/{project_id}/analytics/connections/{connection_id}",
                project_id=project_id,
                connection_id=connection_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[AnalyticsConnection]._unwrapper,
                security={"team_access_token": True},
            ),
            cast_to=cast(Type[AnalyticsConnection], DataWrapper[AnalyticsConnection]),
        )

    async def update(
        self,
        connection_id: str,
        *,
        project_id: str,
        allowed_origins: SequenceNotStr[str] | Omit = omit,
        default_for_dashboard: bool | Omit = omit,
        endpoint: str | Omit = omit,
        name: str | Omit = omit,
        public_ingest_key: str | Omit = omit,
        read_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsConnection:
        """Rename a connection or validate replacement custom credentials.

        Only team owners
        can update connections. Existing settings remain unchanged if validation fails.

        Args:
          allowed_origins: AllowedOrigins lists additional website origins permitted to ingest events for a
              hosted connection. Shared installation origins remain allowed. An empty list
              clears project-specific origins. Custom servers manage origins on their own
              infrastructure.

          default_for_dashboard: DefaultForDashboard selects this ready connection for Chunkify dashboard
              players, public previews, the playground and newly generated snippets. Requires
              a public ingest key. Setting true replaces the previous default atomically.
              Setting false disables dashboard tracking if no default remains; another
              connection is not selected automatically. Existing external players keep their
              own configuration.

          endpoint: Endpoint specifies a replacement custom server base URL. Supply read_key
              together with it.

          name: Name identifies this connection in the dashboard.

          public_ingest_key: PublicIngestKey optionally enables preview tracking for a custom connection.
              Supply the public ingestion key for the same analytics project as read_key. It
              is returned in connection reads and used in browser code. Omit for hosted
              connections. An empty string disables preview tracking. A replacement endpoint
              clears the saved public key unless a replacement is supplied.

          read_key: ReadKey replaces the custom connection credential after validation. Its value is
              never returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not connection_id:
            raise ValueError(f"Expected a non-empty value for `connection_id` but received {connection_id!r}")
        return await self._patch(
            path_template(
                "/projects/{project_id}/analytics/connections/{connection_id}",
                project_id=project_id,
                connection_id=connection_id,
            ),
            body=await async_maybe_transform(
                {
                    "allowed_origins": allowed_origins,
                    "default_for_dashboard": default_for_dashboard,
                    "endpoint": endpoint,
                    "name": name,
                    "public_ingest_key": public_ingest_key,
                    "read_key": read_key,
                },
                analytics_connection_update_params.AnalyticsConnectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[AnalyticsConnection]._unwrapper,
                security={"team_access_token": True},
            ),
            cast_to=cast(Type[AnalyticsConnection], DataWrapper[AnalyticsConnection]),
        )

    async def list(
        self,
        project_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnalyticsConnectionListResponse:
        """List the saved connections for this project.

        No connection is activated by this
        request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/projects/{project_id}/analytics/connections", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"team_access_token": True},
            ),
            cast_to=AnalyticsConnectionListResponse,
        )

    async def delete(
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
    ) -> None:
        """
        For hosted connections, delete the linked analytics project and invalidate its
        keys before removing the saved connection. Stored events expire under the
        collector retention policy. For custom connections, remove only the saved
        credentials and connection; the remote server, project and data remain
        unchanged. Only team owners can delete connections. An uncertain remote result
        preserves the connection for reconciliation.

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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/projects/{project_id}/analytics/connections/{connection_id}",
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
            cast_to=NoneType,
        )


class AnalyticsConnectionsResourceWithRawResponse:
    def __init__(self, analytics_connections: AnalyticsConnectionsResource) -> None:
        self._analytics_connections = analytics_connections

        self.create = to_raw_response_wrapper(
            analytics_connections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            analytics_connections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            analytics_connections.update,
        )
        self.list = to_raw_response_wrapper(
            analytics_connections.list,
        )
        self.delete = to_raw_response_wrapper(
            analytics_connections.delete,
        )

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._analytics_connections.keys)


class AsyncAnalyticsConnectionsResourceWithRawResponse:
    def __init__(self, analytics_connections: AsyncAnalyticsConnectionsResource) -> None:
        self._analytics_connections = analytics_connections

        self.create = async_to_raw_response_wrapper(
            analytics_connections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            analytics_connections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            analytics_connections.update,
        )
        self.list = async_to_raw_response_wrapper(
            analytics_connections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            analytics_connections.delete,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._analytics_connections.keys)


class AnalyticsConnectionsResourceWithStreamingResponse:
    def __init__(self, analytics_connections: AnalyticsConnectionsResource) -> None:
        self._analytics_connections = analytics_connections

        self.create = to_streamed_response_wrapper(
            analytics_connections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            analytics_connections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            analytics_connections.update,
        )
        self.list = to_streamed_response_wrapper(
            analytics_connections.list,
        )
        self.delete = to_streamed_response_wrapper(
            analytics_connections.delete,
        )

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._analytics_connections.keys)


class AsyncAnalyticsConnectionsResourceWithStreamingResponse:
    def __init__(self, analytics_connections: AsyncAnalyticsConnectionsResource) -> None:
        self._analytics_connections = analytics_connections

        self.create = async_to_streamed_response_wrapper(
            analytics_connections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            analytics_connections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            analytics_connections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            analytics_connections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            analytics_connections.delete,
        )

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._analytics_connections.keys)
