"""一覧をページ送りして、全ユーザーの ID と詳細ページの URL を集める。"""

import logging

from sdk.webdriver import WebDriverSession

from components import user_list_page
from schema import UserLink


class CollectUserLinksUseCase:
    def __init__(self, session: WebDriverSession, logger: logging.Logger) -> None:
        self._session = session
        self._logger = logger

    def execute(self, *, list_url: str) -> list[UserLink]:
        self._session.get(list_url)
        links: list[UserLink] = []
        page = 1
        while True:
            page_links = user_list_page.read_links(self._session)
            links.extend(page_links)
            self._logger.info("一覧 %d ページ目: %d 人（累計 %d 人）", page, len(page_links), len(links))
            if not user_list_page.go_next_page(self._session):
                break
            page += 1
        return links
