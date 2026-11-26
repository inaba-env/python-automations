"""入口。`python impl.py` で実行する。

ここでするのは、.env を読む・ブラウザを起動してログインする・usecase を順に呼ぶ、の 3 つだけ。
実処理は usecases / components に書く。
"""

import logging
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

from sdk.env import load_env, require_env
from sdk.webdriver import WebDriverSession

from components import login_page
from constants import JST, USER_LIST_PATH
from parameters import parse_parameters
from usecases import CollectUserLinksUseCase, ExportCsvUseCase, ExtractUserDetailsUseCase

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

logger = logging.getLogger("impl")


def execute() -> None:
    params = parse_parameters()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    # .env を読むのはここだけ。usecases / components には引数で渡す
    load_env(BASE_DIR)
    login_url = require_env("LOGIN_URL")
    login_id = require_env("LOGIN_ID")
    login_password = require_env("LOGIN_PASSWORD")

    now = datetime.now(JST)

    with WebDriverSession(headless=params.headless) as session:
        login_page.login(session, login_url, login_id, login_password)

        links = CollectUserLinksUseCase(session, logger).execute(
            list_url=urljoin(login_url, USER_LIST_PATH)
        )
        details = ExtractUserDetailsUseCase(session, logger).execute(links, limit=params.limit)

    output_path = OUTPUT_DIR / f"users_{now:%Y%m%d}.csv"
    ExportCsvUseCase(logger).execute(details, output_path)


if __name__ == "__main__":
    execute()
