from dataclasses import dataclass
from typing import List


# MEMO: dataclassを使用すると、__init__や__repr__、__eq__を自動で定義してくれる
# MEMO: 型をつけれるものには基本的には型をつける


@dataclass
class ArticleCreateData:
    title: str
    content: str
    author_id: int
    tags: List[int]
    meta_title: str
    meta_description: str

    # MEMO: 何かしらのデータ格納用クラスにはデバッグがしやすいように、以下のように__repr__を定義したい
    def __repr__(self):
        return f"ArticleCreateData(title={self.title}, content={self.content}, author_id={self.author_id}, tags={self.tags}, meta_title={self.meta_title}, meta_description={self.meta_description})"
