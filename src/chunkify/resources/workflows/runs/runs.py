# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import DataWrapper
from ....pagination import SyncPaginatedResults, AsyncPaginatedResults
from ...._base_client import AsyncPaginator, make_request_options
from ....types.workflows import run_list_params
from ....types.workflows.workflow_run import WorkflowRun

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        run_id: str,
        *,
        workflow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRun:
        """
        Retrieve a retained run with its triggering event, status, and action counts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/workflows/{workflow_id}/runs/{run_id}", workflow_id=workflow_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[WorkflowRun]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[WorkflowRun], DataWrapper[WorkflowRun]),
        )

    def list(
        self,
        workflow_id: str,
        *,
        asset_id: str | Omit = omit,
        created: run_list_params.Created | Omit = omit,
        event_id: str | Omit = omit,
        latest_per_asset: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["pending", "running", "completed", "failed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResults[WorkflowRun]:
        """List retained runs for this Workflow, newest first.

        Each run corresponds to one
        matching Asset event.

        Args:
          asset_id: AssetId specifies the Asset whose results to return. Omit it to include all
              Assets.

          event_id: EventId specifies the triggering event ID to filter by. Omit it to include all
              events.

          latest_per_asset: LatestPerAsset specifies whether to return only the latest matching run for each
              Asset. Defaults to false. Pagination and total count apply to Assets when true.

          limit: Limit specifies the maximum number of results to return. Accepts 1 to 100.
              Defaults to 100.

          offset: Offset specifies the number of matching results to skip. Must be at least 0.
              Defaults to 0.

          status: Status specifies the run status to filter by. Omit it to include all statuses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return self._get_api_list(
            path_template("/workflows/{workflow_id}/runs", workflow_id=workflow_id),
            page=SyncPaginatedResults[WorkflowRun],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_id": asset_id,
                        "created": created,
                        "event_id": event_id,
                        "latest_per_asset": latest_per_asset,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    run_list_params.RunListParams,
                ),
                security={"project_access_token": True},
            ),
            model=WorkflowRun,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        run_id: str,
        *,
        workflow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRun:
        """
        Retrieve a retained run with its triggering event, status, and action counts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/workflows/{workflow_id}/runs/{run_id}", workflow_id=workflow_id, run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[WorkflowRun]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[WorkflowRun], DataWrapper[WorkflowRun]),
        )

    def list(
        self,
        workflow_id: str,
        *,
        asset_id: str | Omit = omit,
        created: run_list_params.Created | Omit = omit,
        event_id: str | Omit = omit,
        latest_per_asset: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["pending", "running", "completed", "failed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WorkflowRun, AsyncPaginatedResults[WorkflowRun]]:
        """List retained runs for this Workflow, newest first.

        Each run corresponds to one
        matching Asset event.

        Args:
          asset_id: AssetId specifies the Asset whose results to return. Omit it to include all
              Assets.

          event_id: EventId specifies the triggering event ID to filter by. Omit it to include all
              events.

          latest_per_asset: LatestPerAsset specifies whether to return only the latest matching run for each
              Asset. Defaults to false. Pagination and total count apply to Assets when true.

          limit: Limit specifies the maximum number of results to return. Accepts 1 to 100.
              Defaults to 100.

          offset: Offset specifies the number of matching results to skip. Must be at least 0.
              Defaults to 0.

          status: Status specifies the run status to filter by. Omit it to include all statuses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return self._get_api_list(
            path_template("/workflows/{workflow_id}/runs", workflow_id=workflow_id),
            page=AsyncPaginatedResults[WorkflowRun],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_id": asset_id,
                        "created": created,
                        "event_id": event_id,
                        "latest_per_asset": latest_per_asset,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    run_list_params.RunListParams,
                ),
                security={"project_access_token": True},
            ),
            model=WorkflowRun,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._runs.actions)


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._runs.actions)


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._runs.actions)


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._runs.actions)
