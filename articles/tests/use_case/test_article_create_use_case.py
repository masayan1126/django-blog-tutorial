from django.db import IntegrityError
from django.test import TestCase
from articles.http.request.article_create_data import ArticleCreateData
from articles.models import Article
from articles.repository.article.article_repository import ArticleRepository
from articles.use_case.article_create_use_case import ArticleCreateUseCase
from unittest.mock import patch
from authors.models import Author
from tags.models import Tag


# MEMO: ユースケースのテスト。ユースケースのpublicメソッド全てに対してテストを書く。異常系も想定できるものがあれば書く
class TestArticleCrateUseCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")

        tag_names = ["tag1", "tag2", "tag3"]
        tag_instances = [Tag(name=name) for name in tag_names]
        tags = Tag.objects.bulk_create(tag_instances)
        self.tag_ids = [tag.id for tag in tags]

        self.sut = ArticleCreateUseCase()

    def test_記事を新規作成できる(self):
        article_create_data = ArticleCreateData(
            title="Article title1",
            content="Article content1",
            author_id=self.author.id,
            tags=self.tag_ids,
            meta_title="Article Meta Title1",
            meta_description="Article Meta Description1",
        )

        self.sut.create(article_create_data)

        articles = Article.objects.filter(
            title=article_create_data.title,
            content=article_create_data.content,
            author=article_create_data.author_id,
            articleseo__meta_title=article_create_data.meta_title,
            articleseo__meta_description=article_create_data.meta_description,
        )

        # インプットの記事作成データがDBに保存されていること
        self.assertTrue(articles.exists())
        # 1件の記事が保存されていること
        self.assertTrue(articles.count() == 1)

        # 3件のタグが保存されていること
        tags = articles[0].tags.all()
        self.assertTrue(tags.count() == 3)

    @patch.object(ArticleRepository, "save", side_effect=IntegrityError)
    def test_記事の新規作成時に例外が発生した場合ロールバックされる(self, _):  # モックオブジェクトは使用しないが、定義は必要
        article_create_data = ArticleCreateData(
            title="Article title1",
            content="Article content1",
            author_id=self.author.id,
            tags=self.tag_ids,
            meta_title="Article Meta Title1",
            meta_description="Article Meta Description1",
        )

        # MEMO: トランザクションが正常に動作していることを確認するために、ArticleRepositoryのsaveメソッドをモックにして、
        #       例外を発生させるようにしている
        try:
            self.sut.create(article_create_data)
        except IntegrityError:
            pass

        # トランザクションが正常に動作していることを確認するために、DBに保存されていないことを確認する
        articles = Article.objects.filter(
            title=article_create_data.title,
            content=article_create_data.content,
            author=article_create_data.author_id,
            articleseo__meta_title=article_create_data.meta_title,
            articleseo__meta_description=article_create_data.meta_description,
        )

        # 記事が保存されていないこと
        self.assertFalse(articles.exists())
        # 1件の記事が保存されていないこと
        self.assertTrue(articles.count() == 0)
