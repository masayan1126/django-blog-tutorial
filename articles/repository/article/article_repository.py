from typing import List
from articles.domain.article.article_domain import ArticleDomain
from articles.http.request.article_create_data import ArticleCreateData
from articles.domain.article.article_criteria import ArticleCriteria
from articles.domain.article.article_serializer import ArticleSerializer
from articles.domain.article.article_update_data import ArticleUpdateData
from articles.domain.article_seo.article_seo_serializer import ArticleSEOSerializer
from articles.models import Article
from django.db.models import Q


# MEMO: リポジトリではインスタンス間で共有したいクラス変数やインスタンス変数がないので静的クラスのメソッドで実装する
class ArticleRepository:
    @staticmethod
    def save(data: ArticleCreateData) -> ArticleDomain:
        article_serializer = ArticleSerializer(
            data={
                "title": data.title,
                "content": data.content,
                "author": data.author_id,
                "tags": data.tags,
            }
        )

        article_serializer.is_valid(raise_exception=True)
        article_serializer.save()

        article_seo_serializer = ArticleSEOSerializer(
            data={
                "meta_title": data.meta_title,
                "meta_description": data.meta_description,
                "article": article_serializer.data["id"],
            }
        )

        article_seo_serializer.is_valid(raise_exception=True)
        article_seo_serializer.save()

        return ArticleDomain(
            id=article_serializer.data["id"],
            title=article_serializer.data["title"],
            content=article_serializer.data["content"],
            author=article_serializer.data["author"],
            tags=article_serializer.data["tags"],
            meta_title=article_seo_serializer.data["meta_title"],
            meta_description=article_seo_serializer.data["meta_description"],
        )

    @staticmethod
    def update(data: ArticleUpdateData) -> ArticleDomain:
        old_article = Article.article_with(data.id, "tags", "articleseo", "author")

        article_serializer = ArticleSerializer(
            old_article,
            data={
                "title": data.title,
                "content": data.content,
                "author": data.author_id,
                "tags": data.tags,
            },
        )

        article_serializer.is_valid(raise_exception=True)
        article_serializer.save()

        old_article_seo = old_article.articleseo

        article_seo_serializer = ArticleSEOSerializer(
            old_article_seo,
            data={
                "meta_title": data.meta_title,
                "meta_description": data.meta_description,
                "article": article_serializer.data["id"],
            },
        )

        article_seo_serializer.is_valid(raise_exception=True)
        article_seo_serializer.save()

        return ArticleDomain(
            id=article_serializer.data["id"],
            title=article_serializer.data["title"],
            content=article_serializer.data["content"],
            author=article_serializer.data["author"],
            tags=article_serializer.data["tags"],
            meta_title=article_seo_serializer.data["meta_title"],
            meta_description=article_seo_serializer.data["meta_description"],
        )

    @staticmethod
    def find_by_id(id: int) -> ArticleDomain:
        article = Article.article_with(id, "tags", "articleseo", "author")

        return ArticleDomain(
            id=article.id,
            title=article.title,
            content=article.content,
            author=article.author.id,
            tags=[tag.id for tag in article.tags.all()],
            meta_title=article.articleseo.meta_title,
            meta_description=article.articleseo.meta_description,
        )

    # MEMO: よくあるクエリパラメーターでの検索で一致する複数件のリソースを取得したい場合はcriteriaパターンを使う
    @staticmethod
    def search_by_criteria(
        criteria: ArticleCriteria,
    ) -> List[ArticleDomain]:
        query = ArticleRepository._build_query(criteria)

        articles = Article.articles_with(query, "tags", "articleseo", "author")

        article_domains = []

        for article in articles:
            # MEMO: こういうアクセスをして、オブジェクトが取れていればN+1問題は解決しているが、sqlが実行されていればN+1問題は解決されていないので、nが大きい場合は、気を付ける必要がある
            # print(article.tags.all())
            # print(article.author.id)

            tags = [tag.id for tag in article.tags.all()]

            article_domains.append(
                ArticleDomain(
                    id=article.id,
                    title=article.title,
                    content=article.content,
                    author=article.author.id,
                    tags=tags,
                    meta_title=article.articleseo.meta_title,
                    meta_description=article.articleseo.meta_description,
                )
            )

        return article_domains

    @staticmethod
    def delete(id: int) -> int:
        num_of_deleted, deleted_info = Article.objects.get(pk=id).delete()

        return num_of_deleted

    # MEMO: criteriaでのクエリの組み立て
    @staticmethod
    def _build_query(criteria: ArticleCriteria) -> Q:
        query = Q()

        if len(criteria.author_ids) > 0:
            query = Q(author__in=criteria.author_ids)

        if criteria.title != "":
            query &= Q(title__icontains=criteria.title)

        return query
