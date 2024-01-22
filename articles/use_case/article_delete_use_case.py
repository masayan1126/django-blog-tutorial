from articles.repository.article.article_repository import ArticleRepository
from django.db import transaction


class ArticleDeleteUseCase:
    @transaction.atomic
    def delete(
        self,
        id: int,
    ) -> int:
        return ArticleRepository.delete(id)
