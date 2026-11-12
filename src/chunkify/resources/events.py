# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast
from typing_extensions import Literal

import httpx

from ..types import event_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.event import Event
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Event:
        """
        Retrieve a retained event, its frozen payload, related resources, and up to 100
        delivery attempts. No webhook configuration is required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return self._get(
            path_template("/events/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Event]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Event], DataWrapper[Event]),
        )

    def list(
        self,
        *,
        created: event_list_params.Created | Omit = omit,
        events: List[
            Literal[
                "job.created",
                "job.completed",
                "job.failed",
                "job.cancelled",
                "source.created",
                "source.deleted",
                "upload.created",
                "upload.completed",
                "upload.failed",
                "upload.expired",
                "asset.created",
                "asset.ready",
                "asset.playback_ready",
                "asset.failed",
                "asset.expired",
                "asset.deleted",
                "asset.output.created",
                "asset.output.ready",
                "asset.output.failed",
                "asset.output.deleted",
                "workflow_run.created",
                "workflow_run.completed",
                "workflow_run.failed",
                "workflow_run.cancelled",
                "transcoding.created",
                "transcoding.ready",
                "transcoding.failed",
                "transcoding.cancelled",
                "transcoding.expired",
                "transcoding.deleted",
                "thumbnail.created",
                "thumbnail.ready",
                "thumbnail.failed",
                "thumbnail.expired",
                "thumbnail.deleted",
            ]
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        object_id: str | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResults[Event]:
        """List lifecycle events recorded with or without webhooks.

        Events and their
        deliveries expire according to the plan retention deadline. Historical
        notifications recorded before the event log remain available through
        Notifications.

        Args:
          events: Filter by events

          limit: Pagination limit (max 100)

          object_id: Filter by the primary or a related resource ID, including retained associations
              after resource deletion.

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events",
            page=SyncPaginatedResults[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created": created,
                        "events": events,
                        "limit": limit,
                        "object_id": object_id,
                        "offset": offset,
                    },
                    event_list_params.EventListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Event,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        event_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Event:
        """
        Retrieve a retained event, its frozen payload, related resources, and up to 100
        delivery attempts. No webhook configuration is required.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_id:
            raise ValueError(f"Expected a non-empty value for `event_id` but received {event_id!r}")
        return await self._get(
            path_template("/events/{event_id}", event_id=event_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Event]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Event], DataWrapper[Event]),
        )

    def list(
        self,
        *,
        created: event_list_params.Created | Omit = omit,
        events: List[
            Literal[
                "job.created",
                "job.completed",
                "job.failed",
                "job.cancelled",
                "source.created",
                "source.deleted",
                "upload.created",
                "upload.completed",
                "upload.failed",
                "upload.expired",
                "asset.created",
                "asset.ready",
                "asset.playback_ready",
                "asset.failed",
                "asset.expired",
                "asset.deleted",
                "asset.output.created",
                "asset.output.ready",
                "asset.output.failed",
                "asset.output.deleted",
                "workflow_run.created",
                "workflow_run.completed",
                "workflow_run.failed",
                "workflow_run.cancelled",
                "transcoding.created",
                "transcoding.ready",
                "transcoding.failed",
                "transcoding.cancelled",
                "transcoding.expired",
                "transcoding.deleted",
                "thumbnail.created",
                "thumbnail.ready",
                "thumbnail.failed",
                "thumbnail.expired",
                "thumbnail.deleted",
            ]
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        object_id: str | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Event, AsyncPaginatedResults[Event]]:
        """List lifecycle events recorded with or without webhooks.

        Events and their
        deliveries expire according to the plan retention deadline. Historical
        notifications recorded before the event log remain available through
        Notifications.

        Args:
          events: Filter by events

          limit: Pagination limit (max 100)

          object_id: Filter by the primary or a related resource ID, including retained associations
              after resource deletion.

          offset: Pagination offset

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events",
            page=AsyncPaginatedResults[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created": created,
                        "events": events,
                        "limit": limit,
                        "object_id": object_id,
                        "offset": offset,
                    },
                    event_list_params.EventListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Event,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.retrieve = to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            events.list,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.retrieve = async_to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            events.list,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.retrieve = to_streamed_response_wrapper(
            events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            events.list,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.retrieve = async_to_streamed_response_wrapper(
            events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
