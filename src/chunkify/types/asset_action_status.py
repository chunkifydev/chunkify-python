# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["AssetActionStatus"]

AssetActionStatus: TypeAlias = Literal["pending", "running", "waiting", "completed", "failed", "skipped", "cancelled"]
