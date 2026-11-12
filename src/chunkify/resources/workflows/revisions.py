# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import DataWrapper
from ..._base_client import make_request_options
from ...types.workflows.workflow_revision import WorkflowRevision

__all__ = ["RevisionsResource", "AsyncRevisionsResource"]


class RevisionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return RevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return RevisionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        revision: int,
        *,
        workflow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRevision:
        """
        Retrieve an immutable definition revision, including revisions of archived
        Workflows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return self._get(
            path_template("/workflows/{workflow_id}/revisions/{revision}", workflow_id=workflow_id, revision=revision),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[WorkflowRevision]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[WorkflowRevision], DataWrapper[WorkflowRevision]),
        )


class AsyncRevisionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncRevisionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        revision: int,
        *,
        workflow_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkflowRevision:
        """
        Retrieve an immutable definition revision, including revisions of archived
        Workflows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return await self._get(
            path_template("/workflows/{workflow_id}/revisions/{revision}", workflow_id=workflow_id, revision=revision),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[WorkflowRevision]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[WorkflowRevision], DataWrapper[WorkflowRevision]),
        )


class RevisionsResourceWithRawResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.retrieve = to_raw_response_wrapper(
            revisions.retrieve,
        )


class AsyncRevisionsResourceWithRawResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.retrieve = async_to_raw_response_wrapper(
            revisions.retrieve,
        )


class RevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.retrieve = to_streamed_response_wrapper(
            revisions.retrieve,
        )


class AsyncRevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.retrieve = async_to_streamed_response_wrapper(
            revisions.retrieve,
        )
