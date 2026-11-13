# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

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
from ....types.workflows.runs import action_list_params
from ....types.assets.workflow.asset_action_run import AssetActionRun

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        action_run_id: str,
        *,
        workflow_id: str,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetActionRun:
        """
        Retrieve one action execution in a retained Workflow run, including its resolved
        inputs, status, and result.

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
        if not action_run_id:
            raise ValueError(f"Expected a non-empty value for `action_run_id` but received {action_run_id!r}")
        return self._get(
            path_template(
                "/workflows/{workflow_id}/runs/{run_id}/actions/{action_run_id}",
                workflow_id=workflow_id,
                run_id=run_id,
                action_run_id=action_run_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[AssetActionRun]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[AssetActionRun], DataWrapper[AssetActionRun]),
        )

    def list(
        self,
        run_id: str,
        *,
        workflow_id: str,
        asset_id: str | Omit = omit,
        created: action_list_params.Created | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["pending", "running", "waiting", "completed", "failed", "skipped", "cancelled"] | Omit = omit,
        type: Literal["create_static_rendition", "create_caption", "create_transcript", "translate_caption"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResults[AssetActionRun]:
        """List actions in a retained Workflow run, newest first.

        Includes resolved inputs,
        statuses, output references, and skip or failure reasons.

        Args:
          asset_id: AssetId specifies the Asset whose results to return. Omit it to include all
              Assets.

          limit: Limit specifies the maximum number of results to return. Accepts 1 to 100.
              Defaults to 100.

          offset: Offset specifies the number of matching results to skip. Must be at least 0.
              Defaults to 0.

          status: Status specifies the action status to filter by. Omit it to include all
              statuses.

          type: Type specifies the action type to filter by. Omit it to include all action
              types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get_api_list(
            path_template("/workflows/{workflow_id}/runs/{run_id}/actions", workflow_id=workflow_id, run_id=run_id),
            page=SyncPaginatedResults[AssetActionRun],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_id": asset_id,
                        "created": created,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                        "type": type,
                    },
                    action_list_params.ActionListParams,
                ),
                security={"project_access_token": True},
            ),
            model=AssetActionRun,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        action_run_id: str,
        *,
        workflow_id: str,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetActionRun:
        """
        Retrieve one action execution in a retained Workflow run, including its resolved
        inputs, status, and result.

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
        if not action_run_id:
            raise ValueError(f"Expected a non-empty value for `action_run_id` but received {action_run_id!r}")
        return await self._get(
            path_template(
                "/workflows/{workflow_id}/runs/{run_id}/actions/{action_run_id}",
                workflow_id=workflow_id,
                run_id=run_id,
                action_run_id=action_run_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[AssetActionRun]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[AssetActionRun], DataWrapper[AssetActionRun]),
        )

    def list(
        self,
        run_id: str,
        *,
        workflow_id: str,
        asset_id: str | Omit = omit,
        created: action_list_params.Created | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["pending", "running", "waiting", "completed", "failed", "skipped", "cancelled"] | Omit = omit,
        type: Literal["create_static_rendition", "create_caption", "create_transcript", "translate_caption"]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AssetActionRun, AsyncPaginatedResults[AssetActionRun]]:
        """List actions in a retained Workflow run, newest first.

        Includes resolved inputs,
        statuses, output references, and skip or failure reasons.

        Args:
          asset_id: AssetId specifies the Asset whose results to return. Omit it to include all
              Assets.

          limit: Limit specifies the maximum number of results to return. Accepts 1 to 100.
              Defaults to 100.

          offset: Offset specifies the number of matching results to skip. Must be at least 0.
              Defaults to 0.

          status: Status specifies the action status to filter by. Omit it to include all
              statuses.

          type: Type specifies the action type to filter by. Omit it to include all action
              types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get_api_list(
            path_template("/workflows/{workflow_id}/runs/{run_id}/actions", workflow_id=workflow_id, run_id=run_id),
            page=AsyncPaginatedResults[AssetActionRun],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asset_id": asset_id,
                        "created": created,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                        "type": type,
                    },
                    action_list_params.ActionListParams,
                ),
                security={"project_access_token": True},
            ),
            model=AssetActionRun,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.retrieve = to_raw_response_wrapper(
            actions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            actions.list,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.retrieve = async_to_raw_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            actions.list,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.retrieve = to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            actions.list,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.retrieve = async_to_streamed_response_wrapper(
            actions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            actions.list,
        )
