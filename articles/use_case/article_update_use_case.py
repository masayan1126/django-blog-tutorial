from articles.domain.article.article_domain import ArticleDomain
from articles.domain.article.article_update_data import ArticleUpdateData
from articles.repository.article.article_repository import ArticleRepository
from django.db import transaction


class ArticleUpdateUseCase:
    @transaction.atomic
    def update(
        self,
        article_update_data: ArticleUpdateData,
    ) -> ArticleDomain:
        article = ArticleRepository.update(article_update_data)

        return article
