"""ユーザー一覧画面。"""

from urllib.parse import parse_qs, urlparse

from sdk.webdriver import WebDriverSession

from constants import NEXT_PAGE_BUTTON, USER_LIST_ROW_LINK
from schema import UserLink


def read_links(session: WebDriverSession) -> list[UserLink]:
    """今開いている一覧ページに並ぶユーザーを読む。"""
    session.wait_present(USER_LIST_ROW_LINK)
    links = []
    for a in session.find_elements(USER_LIST_ROW_LINK):
        url = a.get_attribute("href") or ""
        links.append(UserLink(user_id=_user_id_from_url(url), url=url))
    return links


def go_next_page(session: WebDriverSession) -> bool:
    """次のページへ進む。次のページが無ければ False。"""
    if not session.is_present(NEXT_PAGE_BUTTON):
        return False
    session.click(NEXT_PAGE_BUTTON)
    return True


def _user_id_from_url(url: str) -> str:
    """詳細ページの URL からユーザー ID を取り出す。

    `/users/123` のような形なら末尾、`?id=123` のような形なら id の値を使う。
    """
    parsed = urlparse(url)
    query_id = parse_qs(parsed.query).get("id")
    if query_id:
        return query_id[0]
    return parsed.path.rstrip("/").rsplit("/", 1)[-1]
