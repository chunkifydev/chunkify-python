# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["MetricsCreditsSpent"]


class MetricsCreditsSpent(BaseModel):
    """Settled credits in integer units, with 10000 units equal to USD 1 of credits.

    Category values are parts of total, not additional charges.
    """

    assets: int
    """Amount specifies settled credits spent on assets.

    Integer units; 10000 units equal USD 1 of credits.
    """

    egress: int
    """Amount specifies settled credits spent on egress.

    Integer units; 10000 units equal USD 1 of credits.
    """

    static_renditions: int
    """Amount specifies settled credits spent on static renditions.

    Integer units; 10000 units equal USD 1 of credits.
    """

    thumbnails: int
    """Amount specifies settled credits spent on thumbnails.

    Integer units; 10000 units equal USD 1 of credits.
    """

    total: int
    """Total specifies the sum of these media-processing and output-egress charges.

    Integer units; 10000 units equal USD 1 of credits.
    """

    transcodings: int
    """Amount specifies settled credits spent on transcodings.

    Integer units; 10000 units equal USD 1 of credits.
    """

    transcription: int
    """Amount specifies settled credits spent on transcription.

    Integer units; 10000 units equal USD 1 of credits.
    """

    translation: int
    """Amount specifies settled credits spent on translation.

    Integer units; 10000 units equal USD 1 of credits.
    """
