# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
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
from ....types.workflows.workflow_run import WorkflowRun

__all__ = ["WorkflowResource", "AsyncWorkflowResource"]


class WorkflowResource(SyncAPIResource):
    """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""

    @cached_property
    def actions(self) -> ActionsResource:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return ActionsResource(self._client)

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


class AsyncWorkflowResource(AsyncAPIResource):
    """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""

    @cached_property
    def actions(self) -> AsyncActionsResource:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return AsyncActionsResource(self._client)

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


class WorkflowResourceWithRawResponse:
    def __init__(self, workflow: WorkflowResource) -> None:
        self._workflow = workflow

        self.update = to_raw_response_wrapper(
            workflow.update,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return ActionsResourceWithRawResponse(self._workflow.actions)


class AsyncWorkflowResourceWithRawResponse:
    def __init__(self, workflow: AsyncWorkflowResource) -> None:
        self._workflow = workflow

        self.update = async_to_raw_response_wrapper(
            workflow.update,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return AsyncActionsResourceWithRawResponse(self._workflow.actions)


class WorkflowResourceWithStreamingResponse:
    def __init__(self, workflow: WorkflowResource) -> None:
        self._workflow = workflow

        self.update = to_streamed_response_wrapper(
            workflow.update,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return ActionsResourceWithStreamingResponse(self._workflow.actions)


class AsyncWorkflowResourceWithStreamingResponse:
    def __init__(self, workflow: AsyncWorkflowResource) -> None:
        self._workflow = workflow

        self.update = async_to_streamed_response_wrapper(
            workflow.update,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """Automatic video-on-demand Assets and independent H.264 MP4 static renditions."""
        return AsyncActionsResourceWithStreamingResponse(self._workflow.actions)
