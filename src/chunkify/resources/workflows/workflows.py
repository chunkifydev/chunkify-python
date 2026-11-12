# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, cast
from typing_extensions import Literal

import httpx

from ...types import workflow_list_params, workflow_create_params, workflow_update_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .revisions import (
    RevisionsResource,
    AsyncRevisionsResource,
    RevisionsResourceWithRawResponse,
    AsyncRevisionsResourceWithRawResponse,
    RevisionsResourceWithStreamingResponse,
    AsyncRevisionsResourceWithStreamingResponse,
)
from .runs.runs import (
    RunsResource,
    AsyncRunsResource,
    RunsResourceWithRawResponse,
    AsyncRunsResourceWithRawResponse,
    RunsResourceWithStreamingResponse,
    AsyncRunsResourceWithStreamingResponse,
)
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
from ...types.workflow import Workflow
from ...types.workflow_rule_param import WorkflowRuleParam

__all__ = ["WorkflowsResource", "AsyncWorkflowsResource"]


class WorkflowsResource(SyncAPIResource):
    @cached_property
    def revisions(self) -> RevisionsResource:
        return RevisionsResource(self._client)

    @cached_property
    def runs(self) -> RunsResource:
        return RunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return WorkflowsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        rules: Iterable[WorkflowRuleParam],
        schema_version: Literal[1],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workflow:
        """Create a Workflow with its first definition revision.

        Select it when creating an
        Asset or Upload, or set it as the Project default.

        Args:
          name: Name specifies the Workflow name. Use 1 to 128 characters.

          rules: Rules specifies the event subscriptions and actions in this definition. Provide
              exactly one asset.ready rule and up to 15 connected rules, with at most 32
              actions and 65536 encoded bytes across all rules. Array order affects display
              only.

          schema_version: SchemaVersion specifies the Workflow definition format. The supported version
              is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/workflows",
            body=maybe_transform(
                {
                    "name": name,
                    "rules": rules,
                    "schema_version": schema_version,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Workflow]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Workflow], DataWrapper[Workflow]),
        )

    def retrieve(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workflow:
        """
        Retrieve a Workflow and its current definition, including archived Workflows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return self._get(
            path_template("/workflows/{workflow_id}", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Workflow]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Workflow], DataWrapper[Workflow]),
        )

    def update(
        self,
        workflow_id: str,
        *,
        expected_revision: int | Omit = omit,
        name: str | Omit = omit,
        rules: Iterable[WorkflowRuleParam] | Omit = omit,
        schema_version: Literal[1] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Update the Workflow name or replace its rules.

        Replacing rules requires the
        current revision. A changed definition creates a new revision; unchanged rules
        and name-only edits preserve it. Existing Assets and Uploads keep their selected
        revision until a ready Asset explicitly updates to the latest revision. Archived
        Workflows cannot be updated.

        Args:
          expected_revision: ExpectedRevision specifies the current Workflow revision when replacing rules.
              The update returns a conflict if it no longer matches. Required when rules is
              provided. Must be at least 1.

          name: Name specifies the Workflow name. Use 1 to 128 characters.

          rules: Rules specifies the event subscriptions and actions in this definition. Provide
              exactly one asset.ready rule and up to 15 connected rules, with at most 32
              actions and 65536 encoded bytes across all rules. Array order affects display
              only. Replaces the complete definition and requires schema_version and
              expected_revision. Existing Assets and Uploads keep their pinned revision.

          schema_version: SchemaVersion specifies the Workflow definition format. The supported version
              is 1. Required when rules is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            path_template("/workflows/{workflow_id}", workflow_id=workflow_id),
            body=maybe_transform(
                {
                    "expected_revision": expected_revision,
                    "name": name,
                    "rules": rules,
                    "schema_version": schema_version,
                },
                workflow_update_params.WorkflowUpdateParams,
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
        archived: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedResults[Workflow]:
        """List Workflows in the Project, newest first.

        Archived Workflows are excluded
        unless archived is true.

        Args:
          archived: Archived specifies whether to include archived Workflows. Defaults to false.

          limit: Limit specifies the maximum number of results to return. Accepts 1 to 100.
              Defaults to 100.

          offset: Offset specifies the number of matching results to skip. Must be at least 0.
              Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/workflows",
            page=SyncPaginatedResults[Workflow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "limit": limit,
                        "offset": offset,
                    },
                    workflow_list_params.WorkflowListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Workflow,
        )

    def delete(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive the Workflow and clear it from the Project default.

        New Assets cannot
        select it and new events do not start runs. Accepted actions finish, and outputs
        and retained history remain available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/workflows/{workflow_id}", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class AsyncWorkflowsResource(AsyncAPIResource):
    @cached_property
    def revisions(self) -> AsyncRevisionsResource:
        return AsyncRevisionsResource(self._client)

    @cached_property
    def runs(self) -> AsyncRunsResource:
        return AsyncRunsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncWorkflowsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        rules: Iterable[WorkflowRuleParam],
        schema_version: Literal[1],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workflow:
        """Create a Workflow with its first definition revision.

        Select it when creating an
        Asset or Upload, or set it as the Project default.

        Args:
          name: Name specifies the Workflow name. Use 1 to 128 characters.

          rules: Rules specifies the event subscriptions and actions in this definition. Provide
              exactly one asset.ready rule and up to 15 connected rules, with at most 32
              actions and 65536 encoded bytes across all rules. Array order affects display
              only.

          schema_version: SchemaVersion specifies the Workflow definition format. The supported version
              is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/workflows",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "rules": rules,
                    "schema_version": schema_version,
                },
                workflow_create_params.WorkflowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Workflow]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Workflow], DataWrapper[Workflow]),
        )

    async def retrieve(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workflow:
        """
        Retrieve a Workflow and its current definition, including archived Workflows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        return await self._get(
            path_template("/workflows/{workflow_id}", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[Workflow]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[Workflow], DataWrapper[Workflow]),
        )

    async def update(
        self,
        workflow_id: str,
        *,
        expected_revision: int | Omit = omit,
        name: str | Omit = omit,
        rules: Iterable[WorkflowRuleParam] | Omit = omit,
        schema_version: Literal[1] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Update the Workflow name or replace its rules.

        Replacing rules requires the
        current revision. A changed definition creates a new revision; unchanged rules
        and name-only edits preserve it. Existing Assets and Uploads keep their selected
        revision until a ready Asset explicitly updates to the latest revision. Archived
        Workflows cannot be updated.

        Args:
          expected_revision: ExpectedRevision specifies the current Workflow revision when replacing rules.
              The update returns a conflict if it no longer matches. Required when rules is
              provided. Must be at least 1.

          name: Name specifies the Workflow name. Use 1 to 128 characters.

          rules: Rules specifies the event subscriptions and actions in this definition. Provide
              exactly one asset.ready rule and up to 15 connected rules, with at most 32
              actions and 65536 encoded bytes across all rules. Array order affects display
              only. Replaces the complete definition and requires schema_version and
              expected_revision. Existing Assets and Uploads keep their pinned revision.

          schema_version: SchemaVersion specifies the Workflow definition format. The supported version
              is 1. Required when rules is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            path_template("/workflows/{workflow_id}", workflow_id=workflow_id),
            body=await async_maybe_transform(
                {
                    "expected_revision": expected_revision,
                    "name": name,
                    "rules": rules,
                    "schema_version": schema_version,
                },
                workflow_update_params.WorkflowUpdateParams,
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
        archived: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Workflow, AsyncPaginatedResults[Workflow]]:
        """List Workflows in the Project, newest first.

        Archived Workflows are excluded
        unless archived is true.

        Args:
          archived: Archived specifies whether to include archived Workflows. Defaults to false.

          limit: Limit specifies the maximum number of results to return. Accepts 1 to 100.
              Defaults to 100.

          offset: Offset specifies the number of matching results to skip. Must be at least 0.
              Defaults to 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/workflows",
            page=AsyncPaginatedResults[Workflow],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "limit": limit,
                        "offset": offset,
                    },
                    workflow_list_params.WorkflowListParams,
                ),
                security={"project_access_token": True},
            ),
            model=Workflow,
        )

    async def delete(
        self,
        workflow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive the Workflow and clear it from the Project default.

        New Assets cannot
        select it and new events do not start runs. Accepted actions finish, and outputs
        and retained history remain available.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workflow_id:
            raise ValueError(f"Expected a non-empty value for `workflow_id` but received {workflow_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/workflows/{workflow_id}", workflow_id=workflow_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                security={"project_access_token": True},
            ),
            cast_to=NoneType,
        )


class WorkflowsResourceWithRawResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.create = to_raw_response_wrapper(
            workflows.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.update = to_raw_response_wrapper(
            workflows.update,
        )
        self.list = to_raw_response_wrapper(
            workflows.list,
        )
        self.delete = to_raw_response_wrapper(
            workflows.delete,
        )

    @cached_property
    def revisions(self) -> RevisionsResourceWithRawResponse:
        return RevisionsResourceWithRawResponse(self._workflows.revisions)

    @cached_property
    def runs(self) -> RunsResourceWithRawResponse:
        return RunsResourceWithRawResponse(self._workflows.runs)


class AsyncWorkflowsResourceWithRawResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.create = async_to_raw_response_wrapper(
            workflows.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workflows.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            workflows.update,
        )
        self.list = async_to_raw_response_wrapper(
            workflows.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workflows.delete,
        )

    @cached_property
    def revisions(self) -> AsyncRevisionsResourceWithRawResponse:
        return AsyncRevisionsResourceWithRawResponse(self._workflows.revisions)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithRawResponse:
        return AsyncRunsResourceWithRawResponse(self._workflows.runs)


class WorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

        self.create = to_streamed_response_wrapper(
            workflows.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            workflows.update,
        )
        self.list = to_streamed_response_wrapper(
            workflows.list,
        )
        self.delete = to_streamed_response_wrapper(
            workflows.delete,
        )

    @cached_property
    def revisions(self) -> RevisionsResourceWithStreamingResponse:
        return RevisionsResourceWithStreamingResponse(self._workflows.revisions)

    @cached_property
    def runs(self) -> RunsResourceWithStreamingResponse:
        return RunsResourceWithStreamingResponse(self._workflows.runs)


class AsyncWorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

        self.create = async_to_streamed_response_wrapper(
            workflows.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workflows.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            workflows.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workflows.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workflows.delete,
        )

    @cached_property
    def revisions(self) -> AsyncRevisionsResourceWithStreamingResponse:
        return AsyncRevisionsResourceWithStreamingResponse(self._workflows.revisions)

    @cached_property
    def runs(self) -> AsyncRunsResourceWithStreamingResponse:
        return AsyncRunsResourceWithStreamingResponse(self._workflows.runs)
