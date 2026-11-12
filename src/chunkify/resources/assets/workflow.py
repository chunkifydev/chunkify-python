# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import DataWrapper
from ...pagination import SyncPaginatedResults, AsyncPaginatedResults
from ..._base_client import AsyncPaginator, make_request_options
from ...types.assets import workflow_list_actions_params
from ...types.workflows.workflow_run import WorkflowRun
from ...types.assets.asset_action_run import AssetActionRun

__all__ = ["WorkflowResource", "AsyncWorkflowResource"]


class WorkflowResource(SyncAPIResource):
    """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""

    @cached_property
    def with_raw_response(self) -> WorkflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return WorkflowResourceWithStreamingResponse(self)

    def update(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRun:
        """Update a ready Asset to the latest revision of its selected Workflow.

        Existing
        outputs are preserved and missing outputs are created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._post(
            path_template("/assets/{asset_id}/workflow/update", asset_id=asset_id),
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

    def list_actions(
        self,
        asset_id: str,
        *,
        created: workflow_list_actions_params.Created | Omit = omit,
        latest_per_action: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        revision: int | Omit = omit,
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
        """List retained Workflow actions for an Asset, newest first.

        Direct output
        requests are excluded.

        Args:
          latest_per_action: LatestPerAction specifies whether to return only the latest execution of each
              rule and action on the Asset. Defaults to false. Pagination and total count
              apply after this selection.

          limit: Limit specifies the maximum number of results to return. Accepts 1 to 100.
              Defaults to 100.

          offset: Offset specifies the number of matching results to skip. Must be at least 0.
              Defaults to 0.

          revision: Revision specifies the Workflow revision to filter by. Omit it to include all
              revisions.

          status: Status specifies the action status to filter by. Omit it to include all
              statuses.

          type: Type specifies the action type to filter by. Omit it to include all action
              types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get_api_list(
            path_template("/assets/{asset_id}/workflow/actions", asset_id=asset_id),
            page=SyncPaginatedResults[AssetActionRun],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created": created,
                        "latest_per_action": latest_per_action,
                        "limit": limit,
                        "offset": offset,
                        "revision": revision,
                        "status": status,
                        "type": type,
                    },
                    workflow_list_actions_params.WorkflowListActionsParams,
                ),
                security={"project_access_token": True},
            ),
            model=AssetActionRun,
        )


class AsyncWorkflowResource(AsyncAPIResource):
    """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""

    @cached_property
    def with_raw_response(self) -> AsyncWorkflowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncWorkflowResourceWithStreamingResponse(self)

    async def update(
        self,
        asset_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRun:
        """Update a ready Asset to the latest revision of its selected Workflow.

        Existing
        outputs are preserved and missing outputs are created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return await self._post(
            path_template("/assets/{asset_id}/workflow/update", asset_id=asset_id),
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

    def list_actions(
        self,
        asset_id: str,
        *,
        created: workflow_list_actions_params.Created | Omit = omit,
        latest_per_action: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        revision: int | Omit = omit,
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
        """List retained Workflow actions for an Asset, newest first.

        Direct output
        requests are excluded.

        Args:
          latest_per_action: LatestPerAction specifies whether to return only the latest execution of each
              rule and action on the Asset. Defaults to false. Pagination and total count
              apply after this selection.

          limit: Limit specifies the maximum number of results to return. Accepts 1 to 100.
              Defaults to 100.

          offset: Offset specifies the number of matching results to skip. Must be at least 0.
              Defaults to 0.

          revision: Revision specifies the Workflow revision to filter by. Omit it to include all
              revisions.

          status: Status specifies the action status to filter by. Omit it to include all
              statuses.

          type: Type specifies the action type to filter by. Omit it to include all action
              types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not asset_id:
            raise ValueError(f"Expected a non-empty value for `asset_id` but received {asset_id!r}")
        return self._get_api_list(
            path_template("/assets/{asset_id}/workflow/actions", asset_id=asset_id),
            page=AsyncPaginatedResults[AssetActionRun],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created": created,
                        "latest_per_action": latest_per_action,
                        "limit": limit,
                        "offset": offset,
                        "revision": revision,
                        "status": status,
                        "type": type,
                    },
                    workflow_list_actions_params.WorkflowListActionsParams,
                ),
                security={"project_access_token": True},
            ),
            model=AssetActionRun,
        )


class WorkflowResourceWithRawResponse:
    def __init__(self, workflow: WorkflowResource) -> None:
        self._workflow = workflow

        self.update = to_raw_response_wrapper(
            workflow.update,
        )
        self.list_actions = to_raw_response_wrapper(
            workflow.list_actions,
        )


class AsyncWorkflowResourceWithRawResponse:
    def __init__(self, workflow: AsyncWorkflowResource) -> None:
        self._workflow = workflow

        self.update = async_to_raw_response_wrapper(
            workflow.update,
        )
        self.list_actions = async_to_raw_response_wrapper(
            workflow.list_actions,
        )


class WorkflowResourceWithStreamingResponse:
    def __init__(self, workflow: WorkflowResource) -> None:
        self._workflow = workflow

        self.update = to_streamed_response_wrapper(
            workflow.update,
        )
        self.list_actions = to_streamed_response_wrapper(
            workflow.list_actions,
        )


class AsyncWorkflowResourceWithStreamingResponse:
    def __init__(self, workflow: AsyncWorkflowResource) -> None:
        self._workflow = workflow

        self.update = async_to_streamed_response_wrapper(
            workflow.update,
        )
        self.list_actions = async_to_streamed_response_wrapper(
            workflow.list_actions,
        )
