"""工程をまたいで受け渡すデータの型。"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ExampleRecord:
    id: str
