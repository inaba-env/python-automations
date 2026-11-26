"""入口。`python impl.py` で実行する。

ここでするのは、.env を読む・ブラウザなどを用意する・usecase を順に呼ぶ、の 3 つだけ。
実処理は usecases / components に書く。
"""

import logging
from pathlib import Path

from sdk.env import load_env
from sdk.webdriver import WebDriverSession

from parameters import parse_parameters
from usecases import ExampleUseCase

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

logger = logging.getLogger("impl")


def execute() -> None:
    params = parse_parameters()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    # .env を読むのはここだけ。値は require_env で読み、usecases / components には引数で渡す
    load_env(BASE_DIR)

    with WebDriverSession(headless=params.headless) as session:
        ExampleUseCase(session, logger).execute()


if __name__ == "__main__":
    execute()
