from typing import List
from articles.domain.article.article_domain import ArticleDomain


class ArticleTransformer:
    @staticmethod
    def to_dictionary(article: ArticleDomain) -> dict:
        # MEMO: ここの形式はフロントエンドに依存
        return {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "author": article.author,
            "tags": article.tags,
            "seo": {
                "title": article.meta_title,
                "description": article.meta_description,
            },
        }

    @staticmethod
    def to_array(articles: List[ArticleDomain]) -> List[dict]:
        return [ArticleTransformer.to_dictionary(article) for article in articles]
