from rest_framework.routers import DefaultRouter
from django.urls import path, include

from authors.views import AuthorView

router = DefaultRouter()
router.register(r"authors", AuthorView, basename="author")


urlpatterns = [
    path("", include(router.urls)),
]
