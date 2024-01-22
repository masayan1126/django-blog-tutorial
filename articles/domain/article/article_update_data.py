from dataclasses import dataclass
from typing import List


@dataclass
class ArticleUpdateData:
    id: int
    title: str
    content: str
    author_id: int
    tags: List[int]
    meta_title: str
    meta_description: str

    def __repr__(self):
        return f"ArticleUpdateData(id={self.id}, title={self.title}, content={self.content}, author_id={self.author_id}, tags={self.tags}, meta_title={self.meta_title}, meta_description={self.meta_description})"
