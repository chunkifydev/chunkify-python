# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["JobStorage"]


class JobStorage(BaseModel):
    """Storage settings for where the job output will be saved"""

    id: str
    """ID of the storage"""

    path: str
    """Path where the output will be stored"""
