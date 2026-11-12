# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MetricStorageParams"]


class MetricStorageParams(TypedDict, total=False):
    format: Literal["json", "csv"]
    """Response format.

    Defaults to JSON unless Accept requests CSV. Overrides Accept when supplied;
    errors remain JSON.
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """Inclusive UTC start date, YYYY-MM-DD.

    Supply both dates for a custom range of at most 366 days. Omit both for the past
    7 UTC calendar days including today.
    """

    storage_id: str
    """Filter to one persistent storage configuration in the authenticated project."""

    to: str
    """Exclusive UTC end date, YYYY-MM-DD.

    Must be after from and at most 366 days later.
    """
