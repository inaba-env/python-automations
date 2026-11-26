"""UserDetail を CSV の 1 行にする。"""

from dataclasses import asdict

from constants import CSV_COLUMNS
from schema import UserDetail


def to_row(detail: UserDetail) -> dict[str, str]:
    values = asdict(detail)
    return {header: values[field] for header, field in CSV_COLUMNS.items()}
