"""工程をまたいで受け渡すデータの型。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class UserLink:
    """一覧で見つけたユーザー。"""

    user_id: str
    url: str


@dataclass(frozen=True)
class UserDetail:
    """詳細ページから抜いた値。項目は constants.DETAIL_FIELDS と揃える。"""

    user_id: str
    name: str
    email: str
    department: str
