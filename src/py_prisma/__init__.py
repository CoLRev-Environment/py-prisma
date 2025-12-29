"""Package for py-prisma."""

from dataclasses import asdict
from pathlib import Path

from .loader import load_status_from_records
from .loader import PrismaStatus
from .prisma import plot_prisma2020

__author__ = "Gerit Wagner"
__email__ = "gerit.wagner@uni-bamberg.de"

__all__ = [
    "PrismaStatus",
    "load_status_from_records",
    "plot_prisma2020",
]


def plot_prisma_from_records(
    *,
    records_path: str | Path = "data/records.bib",
    output_path: str | Path = "prisma.png",
    show: bool = False,
) -> None:

    params = load_status_from_records(records_path)

    plot_prisma2020(
        **asdict(params),
        filename=str(output_path),
        show=show,
    )
