from rest_framework.response import Response
from rest_framework import status, viewsets
from tags.serializer import TagSerializer
from tags.models import Tag


class TagView(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        tag = Tag.objects.get(pk=kwargs["pk"])
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        tag = Tag.objects.get(pk=kwargs["pk"])
        tag.name = request.data["name"]

        serializer = TagSerializer(tag)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        tag = Tag.objects.get(pk=kwargs["pk"])
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
