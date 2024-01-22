from rest_framework.response import Response
from rest_framework import status, viewsets
from comments.models import Comment


class CommentView(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        return Response(comments, status=status.HTTP_200_OK)
