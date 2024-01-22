from articles.domain.article.article_domain import ArticleDomain
from articles.repository.article.article_repository import ArticleRepository


class ArticleFindUseCase:
    def find(self, id: int) -> ArticleDomain:
        article = ArticleRepository.find_by_id(id=id)

        return article
