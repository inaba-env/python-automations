"""決まった列順で CSV を書き出す。

既定の文字コードは cp932。受け取った CSV を Excel で開く先方が多いため。
cp932 に無い文字（一部の旧字体・絵文字など）があると、既定では書き出しを止める。
`errors="replace"` を渡すと「?」に置き換えて書き出す。
"""

import csv
from collections.abc import Iterable, Mapping
from pathlib import Path


def write_csv(
    path: Path,
    columns: list[str],
    rows: Iterable[Mapping[str, object]],
    *,
    encoding: str = "cp932",
    errors: str = "strict",
) -> int:
    """`columns` の順で 1 行目に見出しを書き、`rows` を書き出す。書いた行数を返す。

    `rows` の各行は `columns` の見出しをキーに持つ。キーが足りない行は止める
    （列ずれに気付かないまま納品するのを防ぐため）。
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding=encoding, errors=errors, newline="") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="raise")
        writer.writeheader()
        for row in rows:
            missing = [c for c in columns if c not in row]
            if missing:
                raise KeyError(f"{count + 1} 行目に列がありません: {missing}")
            writer.writerow(row)
            count += 1
    return count
