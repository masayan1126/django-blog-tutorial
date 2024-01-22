from rest_framework.routers import DefaultRouter
from django.urls import path, include
from comments.views import CommentView

router = DefaultRouter()
router.register(r"comments", CommentView, basename="comment")


urlpatterns = [
    path(
        "articles/<int:article_id>/",
        include(
            [
                path("", include(router.urls)),
            ]
        ),
    ),
]
