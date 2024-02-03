from dataclasses import dataclass
from typing import List
from rest_framework import serializers

from articles.http.request.article_create_data import ArticleCreateData


# MEMO: dataclassを使用すると、__init__や__repr__、__eq__を自動で定義してくれる
# MEMO: 型をつけれるものには基本的には型をつける


@dataclass
class ArticleCreateRequestValidator:
    def do_validate(self, article_create_request_data: dict) -> ArticleCreateData:
        serializer = ArticleCreateRequestSerializer(
            data={
                "title": article_create_request_data["title"],
                "content": article_create_request_data["content"],
                "author_id": article_create_request_data["author_id"],
                "tags": article_create_request_data["tags"],
                "meta_title": article_create_request_data["meta_title"],
                "meta_description": article_create_request_data["meta_description"],
            }
        )
        serializer.is_valid(
            raise_exception=True,
        )

        return ArticleCreateData(
            title=serializer.data["title"],
            content=serializer.data["content"],
            author_id=serializer.data["author_id"],
            tags=serializer.data["tags"],
            meta_title=serializer.data["meta_title"],
            meta_description=serializer.data["meta_description"],
        )


class ArticleCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    author_id = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.IntegerField())
    meta_title = serializers.CharField()
    meta_description = serializers.CharField()
