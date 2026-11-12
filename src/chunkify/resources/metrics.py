# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ..types import metric_usage_params, metric_assets_params, metric_storage_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.metrics_usage import MetricsUsage
from ..types.metrics_assets import MetricsAssets
from ..types.metrics_storage import MetricsStorage

__all__ = ["MetricsResource", "AsyncMetricsResource"]


class MetricsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return MetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return MetricsResourceWithStreamingResponse(self)

    def assets(
        self,
        *,
        format: Literal["json", "csv"] | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricsAssets:
        """
        Retrieve Asset outcomes, timings, output sizes and source profiles by UTC
        creation date.

        Args:
          format: Response format. Defaults to JSON unless Accept requests CSV. Overrides Accept
              when supplied; errors remain JSON.

          from_: Inclusive UTC start date, YYYY-MM-DD. Supply both dates for a custom range of at
              most 366 days. Omit both for the past 7 UTC calendar days including today.

          to: Exclusive UTC end date, YYYY-MM-DD. Must be after from and at most 366 days
              later.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/metrics/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "from_": from_,
                        "to": to,
                    },
                    metric_assets_params.MetricAssetsParams,
                ),
                post_parser=DataWrapper[MetricsAssets]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[MetricsAssets], DataWrapper[MetricsAssets]),
        )

    def storage(
        self,
        *,
        format: Literal["json", "csv"] | Omit = omit,
        from_: str | Omit = omit,
        storage_id: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricsStorage:
        """
        Retrieve recorded additions and successful removals by storage and UTC date.
        Historical coverage depends on event retention.

        Args:
          format: Response format. Defaults to JSON unless Accept requests CSV. Overrides Accept
              when supplied; errors remain JSON.

          from_: Inclusive UTC start date, YYYY-MM-DD. Supply both dates for a custom range of at
              most 366 days. Omit both for the past 7 UTC calendar days including today.

          storage_id: Filter to one persistent storage configuration in the authenticated project.

          to: Exclusive UTC end date, YYYY-MM-DD. Must be after from and at most 366 days
              later.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/metrics/storage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "from_": from_,
                        "storage_id": storage_id,
                        "to": to,
                    },
                    metric_storage_params.MetricStorageParams,
                ),
                post_parser=DataWrapper[MetricsStorage]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[MetricsStorage], DataWrapper[MetricsStorage]),
        )

    def usage(
        self,
        *,
        format: Literal["json", "csv"] | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricsUsage:
        """
        Retrieve project usage totals and daily values for a UTC date range.

        Args:
          format: Response format. Defaults to JSON unless Accept requests CSV. Overrides Accept
              when supplied; errors remain JSON.

          from_: Inclusive UTC start date, YYYY-MM-DD. Supply both dates for a custom range of at
              most 366 days. Omit both for the past 7 UTC calendar days including today.

          to: Exclusive UTC end date, YYYY-MM-DD. Must be after from and at most 366 days
              later.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/metrics/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "from_": from_,
                        "to": to,
                    },
                    metric_usage_params.MetricUsageParams,
                ),
                post_parser=DataWrapper[MetricsUsage]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[MetricsUsage], DataWrapper[MetricsUsage]),
        )


class AsyncMetricsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/chunkifydev/chunkify-python#with_streaming_response
        """
        return AsyncMetricsResourceWithStreamingResponse(self)

    async def assets(
        self,
        *,
        format: Literal["json", "csv"] | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricsAssets:
        """
        Retrieve Asset outcomes, timings, output sizes and source profiles by UTC
        creation date.

        Args:
          format: Response format. Defaults to JSON unless Accept requests CSV. Overrides Accept
              when supplied; errors remain JSON.

          from_: Inclusive UTC start date, YYYY-MM-DD. Supply both dates for a custom range of at
              most 366 days. Omit both for the past 7 UTC calendar days including today.

          to: Exclusive UTC end date, YYYY-MM-DD. Must be after from and at most 366 days
              later.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/metrics/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "from_": from_,
                        "to": to,
                    },
                    metric_assets_params.MetricAssetsParams,
                ),
                post_parser=DataWrapper[MetricsAssets]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[MetricsAssets], DataWrapper[MetricsAssets]),
        )

    async def storage(
        self,
        *,
        format: Literal["json", "csv"] | Omit = omit,
        from_: str | Omit = omit,
        storage_id: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricsStorage:
        """
        Retrieve recorded additions and successful removals by storage and UTC date.
        Historical coverage depends on event retention.

        Args:
          format: Response format. Defaults to JSON unless Accept requests CSV. Overrides Accept
              when supplied; errors remain JSON.

          from_: Inclusive UTC start date, YYYY-MM-DD. Supply both dates for a custom range of at
              most 366 days. Omit both for the past 7 UTC calendar days including today.

          storage_id: Filter to one persistent storage configuration in the authenticated project.

          to: Exclusive UTC end date, YYYY-MM-DD. Must be after from and at most 366 days
              later.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/metrics/storage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "from_": from_,
                        "storage_id": storage_id,
                        "to": to,
                    },
                    metric_storage_params.MetricStorageParams,
                ),
                post_parser=DataWrapper[MetricsStorage]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[MetricsStorage], DataWrapper[MetricsStorage]),
        )

    async def usage(
        self,
        *,
        format: Literal["json", "csv"] | Omit = omit,
        from_: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MetricsUsage:
        """
        Retrieve project usage totals and daily values for a UTC date range.

        Args:
          format: Response format. Defaults to JSON unless Accept requests CSV. Overrides Accept
              when supplied; errors remain JSON.

          from_: Inclusive UTC start date, YYYY-MM-DD. Supply both dates for a custom range of at
              most 366 days. Omit both for the past 7 UTC calendar days including today.

          to: Exclusive UTC end date, YYYY-MM-DD. Must be after from and at most 366 days
              later.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/metrics/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "from_": from_,
                        "to": to,
                    },
                    metric_usage_params.MetricUsageParams,
                ),
                post_parser=DataWrapper[MetricsUsage]._unwrapper,
                security={"project_access_token": True},
            ),
            cast_to=cast(Type[MetricsUsage], DataWrapper[MetricsUsage]),
        )


class MetricsResourceWithRawResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.assets = to_raw_response_wrapper(
            metrics.assets,
        )
        self.storage = to_raw_response_wrapper(
            metrics.storage,
        )
        self.usage = to_raw_response_wrapper(
            metrics.usage,
        )


class AsyncMetricsResourceWithRawResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.assets = async_to_raw_response_wrapper(
            metrics.assets,
        )
        self.storage = async_to_raw_response_wrapper(
            metrics.storage,
        )
        self.usage = async_to_raw_response_wrapper(
            metrics.usage,
        )


class MetricsResourceWithStreamingResponse:
    def __init__(self, metrics: MetricsResource) -> None:
        self._metrics = metrics

        self.assets = to_streamed_response_wrapper(
            metrics.assets,
        )
        self.storage = to_streamed_response_wrapper(
            metrics.storage,
        )
        self.usage = to_streamed_response_wrapper(
            metrics.usage,
        )


class AsyncMetricsResourceWithStreamingResponse:
    def __init__(self, metrics: AsyncMetricsResource) -> None:
        self._metrics = metrics

        self.assets = async_to_streamed_response_wrapper(
            metrics.assets,
        )
        self.storage = async_to_streamed_response_wrapper(
            metrics.storage,
        )
        self.usage = async_to_streamed_response_wrapper(
            metrics.usage,
        )
