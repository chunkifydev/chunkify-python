# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ....._models import BaseModel
from .analytics_key import AnalyticsKey

__all__ = ["KeyCreateResponse"]


class KeyCreateResponse(BaseModel):
    data: AnalyticsKey
    """One key per purpose.

    Public player values remain available; read and MCP values are returned only on
    creation or rotation.
    """

    key: str
    """Key is the new credential.

    Save read and MCP keys now; later reads omit their values. Public keys remain
    available.
    """

    status: Literal["success"]
