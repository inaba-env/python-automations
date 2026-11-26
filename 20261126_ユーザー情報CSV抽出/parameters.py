"""実行時に受け取る引数。"""

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Parameters:
    limit: int | None
    headless: bool


def parse_parameters() -> Parameters:
    parser = argparse.ArgumentParser(description="ユーザー情報を詳細ページから抜き出して CSV にする")
    parser.add_argument("--limit", type=int, default=None, help="詳細を抜くのを N 件で止める")
    parser.add_argument("--no-headless", action="store_true", help="Chrome の画面を出して動かす")
    args = parser.parse_args()
    return Parameters(limit=args.limit, headless=not args.no_headless)
