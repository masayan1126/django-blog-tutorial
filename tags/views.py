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
        # manyで複数のオブジェクトをシリアライズすることができる
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        # request(request.data.get("key")でリクエストボディを取得できる) print(request.data)  # <QueryDict: {'name': ['vvff'], 'color': ['tag-1']}>
        # request.userでリクエストを送信したユーザーを取得できる
        # request.authで認証トークンを取得できる
        # request.accepted_media_typeでリクエストヘッダーのContent-Typeを取得できる

        # request.parser_context
        # {'view': <tags.api.views.TagViewSet object at 0x11b075c70>, 'args': (), 'kwargs': {'space': 1497118514, 'pk': '621014733821'}, 'request': <rest_framework.request.Request: GET '/spaces/1497118514/tags/621014733821/'>, 'encoding': 'utf-8'}

        # kwargs(パスパラメータが入ってる)

        tag = Tag.objects.get(pk=kwargs["pk"])
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        tag = Tag.objects.get(pk=kwargs["pk"])
        tag.name = request.data["name"]

        serializer = TagSerializer(tag)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # partial=Trueは、シリアライザーの部分更新を有効にするフラグです。 部分更新を行う場合、更新するフィールドのみを指定してオブジェクトを更新することができます。 つまり、partial=Trueを指定することで、指定されたフィールドのみを更新し、他のフィールドは変更されないようにすることができます。
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        tag = Tag.objects.get(pk=kwargs["pk"])
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
