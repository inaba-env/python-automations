"""ユーザー詳細画面。"""

from sdk.webdriver import WebDriverSession

from constants import DETAIL_FIELDS, WAIT_SECONDS
from schema import UserDetail, UserLink


def read_detail(session: WebDriverSession, link: UserLink) -> UserDetail:
    session.get(link.url, seconds=WAIT_SECONDS)
    values = {field: session.get_text(xpath) for field, xpath in DETAIL_FIELDS.items()}
    return UserDetail(user_id=link.user_id, **values)
