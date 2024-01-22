from rest_framework.routers import DefaultRouter
from django.urls import path, include
from articles.views import ArticleView

router = DefaultRouter()
router.register(r"articles", ArticleView, basename="article")


urlpatterns = [
    path("", include(router.urls)),
]
