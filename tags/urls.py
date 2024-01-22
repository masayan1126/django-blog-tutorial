from rest_framework.routers import DefaultRouter
from django.urls import path, include

from tags.views import TagView

router = DefaultRouter()
router.register(r"tags", TagView, basename="tag")


urlpatterns = [
    path("", include(router.urls)),
]
