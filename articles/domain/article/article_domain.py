from dataclasses import dataclass
from typing import List


@dataclass
class ArticleDomain:
    def __init__(
        self,
        id: int,
        title: str,
        content: str,
        author: int,
        tags: List[int],
        meta_title: str,
        meta_description: str,
    ):
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.tags = tags
        self.meta_title = meta_title
        self.meta_description = meta_description

    def __repr__(self):
        return f"Article(id={self.id}, title={self.title}, content={self.content}, author={self.author}, tags={self.tags}, meta_title={self.meta_title}, meta_description={self.meta_description})"
