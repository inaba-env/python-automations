"""実行時に受け取る引数。"""

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Parameters:
    headless: bool


def parse_parameters() -> Parameters:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--no-headless", action="store_true", help="Chrome の画面を出して動かす")
    args = parser.parse_args()
    return Parameters(headless=not args.no_headless)
