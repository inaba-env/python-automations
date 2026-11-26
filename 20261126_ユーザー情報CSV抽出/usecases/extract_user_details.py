"""詳細ページを 1 件ずつ開いて情報を抜く。"""

import logging

from sdk.webdriver import WebDriverSession

from components import user_detail_page
from schema import UserDetail, UserLink

# 続けてこの件数失敗したら止める。ログインが切れたときに、残り全件を失敗で流さないため
MAX_CONSECUTIVE_FAILURES = 5


class ExtractUserDetailsUseCase:
    def __init__(self, session: WebDriverSession, logger: logging.Logger) -> None:
        self._session = session
        self._logger = logger

    def execute(self, links: list[UserLink], *, limit: int | None) -> list[UserDetail]:
        targets = links if limit is None else links[:limit]
        self._logger.info("詳細: 全 %d 人のうち %d 人を抜きます", len(links), len(targets))

        details: list[UserDetail] = []
        failures: list[str] = []
        consecutive = 0
        for i, link in enumerate(targets, start=1):
            try:
                details.append(user_detail_page.read_detail(self._session, link))
            except Exception as e:  # 1 人の失敗で全体を止めず、記録して次へ進む
                failures.append(link.user_id)
                consecutive += 1
                self._logger.warning("失敗 %s: %s", link.user_id, e)
                if consecutive >= MAX_CONSECUTIVE_FAILURES:
                    raise RuntimeError(
                        f"{consecutive} 件続けて失敗したので止めます。ログインが切れていないか確かめてください"
                    ) from e
                continue
            consecutive = 0
            if i % 50 == 0:
                self._logger.info("詳細 %d / %d 人", i, len(targets))

        if failures:
            self._logger.warning("失敗 %d 人（CSV に入っていません）: %s", len(failures), failures)
        return details
