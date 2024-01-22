from typing import List


class ArticleCriteria:
    author_ids: List[int] = []
    title: str = ""

    def set_author_ids(self, author_ids: List[int]):
        self.author_ids = author_ids
        return self

    def set_title(self, title: str):
        self.title = title
        return self

    def __repr__(self):
        return f"ArticleCriteria(author_ids={self.author_ids}, title={self.title})"
