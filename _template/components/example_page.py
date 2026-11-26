"""サンプルの画面。コピーして書き換える。"""

from sdk.webdriver import WebDriverSession


def read_first_paragraph(session: WebDriverSession, url: str) -> str:
    session.get(url)
    return session.get_text("//p")
