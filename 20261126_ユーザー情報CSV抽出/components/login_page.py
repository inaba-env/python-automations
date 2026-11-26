"""ログイン画面。"""

from sdk.webdriver import WebDriverSession

from constants import (
    LOGGED_IN_MARK,
    LOGIN_ID_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_SUBMIT_BUTTON,
)


def login(session: WebDriverSession, url: str, login_id: str, password: str) -> None:
    session.get(url)
    session.send_keys(LOGIN_ID_INPUT, login_id)
    session.send_keys(LOGIN_PASSWORD_INPUT, password)
    session.click(LOGIN_SUBMIT_BUTTON)
    # ログイン後の画面に出る要素で、ログインできたかを確かめる（出なければ待ち時間切れで止まる）
    session.wait_present(LOGGED_IN_MARK)
