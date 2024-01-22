from django.db import models
from authors.models import Author
from tags.models import Tag
from django.db.models import Prefetch


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # MEMO:多对一、一对多
    tags = models.ManyToManyField(Tag, blank=True)  # MEMO:多对多
    # MEMO:多对多の場合は、自動的に中間テーブルが作成される。throughで中間テーブルを指定することも可能

    def __str__(self):
        return f"id:{self.id} - title:{self.title} - content:{self.content} - author:{self.author.name} - tags:{self.tags.all()} \n --------------------------------"

    # MEMO: 結合が必要なメソッドはモデルに実装するようにする
    @staticmethod
    def article_with(article_id, *related_models):
        article = Article.objects

        # MEMO: "一対一"または"多対一"のリレーションを持つモデルを取得する場合はselect_relatedを使用
        if "articleseo" in related_models:
            article = article.select_related("articleseo")

        if "author" in related_models:
            article = article.select_related("author")

        if "tags" in related_models:
            # MEMO: タグを全て一括で取得する宣言
            prefetch = Prefetch("tags", queryset=Tag.objects.all())
            # MEMO: "一対多"または"多対多"のリレーションシップにはprefetch_relatedを使用
            # MEMO: prefetch_related実行時点で、記事IDに一致するタグがメモリにロードされる
            article = article.prefetch_related(prefetch)

        return article.get(id=article_id)

    @staticmethod
    def articles_with(query, *related_models):
        articles = Article.objects

        if "articleseo" in related_models:
            articles = Article.objects.select_related("articleseo")

        if "author" in related_models:
            articles = articles.select_related("author")

        if "tags" in related_models:
            prefetch = Prefetch("tags", queryset=Tag.objects.all())
            articles = articles.prefetch_related(prefetch)

        return articles.filter(query)

    # def to_domain(self) -> ArticleDomain:
    #     return ArticleDomain(
    #         id=self.id,
    #         title=self.title,
    #         content=self.content,
    #         author=self.author.id,
    #         tags=[tag.id for tag in self.tags.all()],
    #     )

    # def from_domain(self, article: ArticleDomain):
    #     self.id = article.id
    #     self.title = article.title
    #     self.content = article.content
    #     self.author = Author.objects.get(pk=article.author)
    #     self.tags.set(Tag.objects.filter(pk__in=article.tags))


# MEMO: アプリケーションの単位として構成されないモデル(ArticleSEO)は、アプリケーションとして定義されるモデル(Article)と同じモデルファイルに定義する必要がある?(分けたらマイグレーションが作成されなかった)
class ArticleSEO(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f"id:{self.id} - article_id:{self.article.id} - meta_title:{self.meta_title} - meta_description:{self.meta_description} \n --------------------------------"
