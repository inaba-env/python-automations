"""抜いた情報を決まった形式で CSV に書き出す。"""

import logging
from pathlib import Path

from sdk.csv import write_csv

from components import csv_rows
from constants import CSV_COLUMNS, CSV_ENCODING
from schema import UserDetail


class ExportCsvUseCase:
    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger

    def execute(self, details: list[UserDetail], output_path: Path) -> None:
        count = write_csv(
            output_path,
            list(CSV_COLUMNS),
            (csv_rows.to_row(d) for d in details),
            encoding=CSV_ENCODING,
        )
        self._logger.info("CSV に %d 人を書き出しました: %s", count, output_path)
