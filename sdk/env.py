"""業務フォルダの .env を読む。

読むのは、実行したディレクトリではなく、渡されたフォルダ（業務フォルダ）の .env。
別のフォルダから `python 20261126_xxx/impl.py` と実行しても、ほかの業務の .env を読まない。
"""

import os
from pathlib import Path

from dotenv import load_dotenv


def load_env(base_dir: Path) -> None:
    """`base_dir/.env` を環境変数に読み込む。すでにある環境変数は上書きしない。"""
    env_path = base_dir / ".env"
    if not env_path.exists():
        raise FileNotFoundError(
            f"{env_path} がありません。.env.example をコピーして値を入れてください"
        )
    load_dotenv(env_path, override=False)


def require_env(name: str) -> str:
    """環境変数を読む。無いか空なら、どのキーが足りないかを書いて止める。"""
    value = os.environ.get(name, "")
    if not value:
        raise KeyError(f".env に {name} がありません")
    return value
