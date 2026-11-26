"""サンプルの流れ。コピーして書き換える。"""

import logging

from sdk.webdriver import WebDriverSession

from components import example_page


class ExampleUseCase:
    def __init__(self, session: WebDriverSession, logger: logging.Logger) -> None:
        self._session = session
        self._logger = logger

    def execute(self) -> None:
        text = example_page.read_first_paragraph(self._session, "https://example.com")
        self._logger.info("最初の段落: %s", text)
