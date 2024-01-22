from typing import List, TypedDict
from articles.domain.article.article_domain import ArticleDomain


class SeoDict(TypedDict):
    meta_title: str
    meta_description: str


class ArticleDict(TypedDict):
    id: int
    title: str
    content: str
    author: int
    tags: List[int]
    seo: SeoDict


# TypeDictを使用すると、辞書のキーと値の型を厳密に定義することができるが、実際にやるかどうかは要検討
class ArticleTransformer:
    @staticmethod
    def to_dictionary(article: ArticleDomain) -> ArticleDict:
        # MEMO: ここの形式はフロントエンドに依存
        return {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "author": article.author,
            "tags": article.tags,
            "seo": {
                "meta_title": article.meta_title,
                "meta_description": article.meta_description,
            },
        }

    @staticmethod
    def to_array(articles: List[ArticleDomain]) -> List[ArticleDict]:
        return [ArticleTransformer.to_dictionary(article) for article in articles]
