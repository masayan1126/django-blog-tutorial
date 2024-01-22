from articles.models import Article, ArticleSEO
from authors.models import Author
from comments.models import Comment
from tags.models import Tag
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Initialize data for Article, Tag, Author, Comment"

    def handle(self, *args, **options):
        # Create authors
        author1 = Author.objects.create(name="Author 1")
        author2 = Author.objects.create(name="Author 2")

        # Create articles
        article1 = Article.objects.create(
            title="Article 1", content="Content 1", author=author1
        )
        article2 = Article.objects.create(
            title="Article 2", content="Content 2", author=author2
        )

        article_meta1 = ArticleSEO.objects.create(
            article=article1,
            meta_title="Meta title 1",
            meta_description="Meta description 1",
        )

        article_meta2 = ArticleSEO.objects.create(
            article=article2,
            meta_title="Meta title 2",
            meta_description="Meta description 2",
        )

        # Create tags
        tag1 = Tag.objects.create(name="Tag 1")
        tag2 = Tag.objects.create(name="Tag 2")

        # Add tags to articles
        article1.tags.add(tag1)
        article2.tags.add(tag2)

        # Create comments
        Comment.objects.create(content="Comment 1", article=article1)
        Comment.objects.create(content="Comment 2", article=article2)

        self.stdout.write(self.style.SUCCESS("Successfully initialized data"))
