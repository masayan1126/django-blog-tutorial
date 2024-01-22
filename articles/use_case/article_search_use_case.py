from typing import List
from articles.domain.article.article_domain import ArticleDomain
from articles.domain.article.article_criteria import ArticleCriteria
from articles.repository.article.article_repository import ArticleRepository


class ArticleSearchUseCase:
    def search(self, criteria: ArticleCriteria) -> List[ArticleDomain]:
        articles = ArticleRepository.search_by_criteria(criteria=criteria)

        return articles
