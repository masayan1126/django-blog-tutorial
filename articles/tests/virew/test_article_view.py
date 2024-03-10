from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from authors.models import Author
from tags.models import Tag
import json


class TestArticleView(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author1")

        tag_names = ["tag1", "tag2", "tag3"]
        tag_instances = [Tag(name=name) for name in tag_names]
        tags = Tag.objects.bulk_create(tag_instances)
        self.tag_ids = [tag.id for tag in tags]

        self.url = reverse("article-list")

    def test_記事を新規作成できる(
        self,
    ):
        request_data = {
            "title": "Title1",
            "content": "Content1",
            "author_id": self.author.id,
            "tags": self.tag_ids,
            "meta_title": "Meta Title1",
            "meta_description": "Meta description1",
        }

        response = self.client.post(
            reverse("article-list"), request_data, format="json"
        )

        # レスポンスボディがバイトなので、それを文字列に変換してから、辞書に変換する
        expected_response_body = json.loads(response.content.decode())
        expected_response_code = status.HTTP_201_CREATED

        self.assertEqual(
            expected_response_body,
            {
                "id": 1,
                "title": "Title1",
                "content": "Content1",
                "author": self.author.id,
                "tags": self.tag_ids,
                "seo": {
                    "meta_title": "Meta Title1",
                    "meta_description": "Meta description1",
                },
            },
        )

        self.assertEqual(expected_response_code, response.status_code)
