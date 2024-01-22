from typing import Tuple
from articles.domain.article.article_domain import ArticleDomain
from articles.domain.article.article_create_data_ import ArticleCreateData
from articles.repository.article.article_repository import ArticleRepository
from django.db import transaction


class ArticleCreateUseCase:
    # MEMO: ユースケースにトランザクションを貼る
    @transaction.atomic
    def create(
        self,
        article_create_data: ArticleCreateData,
    ) -> ArticleDomain:
        return ArticleRepository.save(article_create_data)
