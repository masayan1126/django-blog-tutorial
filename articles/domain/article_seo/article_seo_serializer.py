from rest_framework import serializers

from articles.models import ArticleSEO


class ArticleSEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSEO
        fields = "__all__"
