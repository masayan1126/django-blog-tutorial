from rest_framework.response import Response
from rest_framework import status, viewsets

from authors.models import Author


class AuthorView(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        author = Author.objects.create(**request.data)
        return Response(author, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        authors = Author.objects.all()
        return Response(authors, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        author = Author.objects.get(pk=kwargs["pk"])
        return Response(author, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        author = Author.objects.get(pk=kwargs["pk"])
        author.name = request.data["name"]
        author.save()
        return Response(author, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        author = Author.objects.get(pk=kwargs["pk"])
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
