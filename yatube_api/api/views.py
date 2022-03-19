"""views_api."""
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from posts.models import Comment, Group, Post
from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """PostViewSet."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """PostViewSetCreate."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """PostViewSetUpdate."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        """PostViewSetDestroy."""
        if self.request.user != instance.author:
            raise PermissionDenied()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """GroupViewSet."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """CommentViewSet."""
    serializer_class = CommentSerializer

    def get_queryset(self):
        """CommentViewSet_queryset."""
        post_id = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return Comment.objects.filter(post=post_id.pk)

    def perform_create(self, serializer):
        """CommentViewSetCreate."""
        post_id = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post_id)

    def perform_update(self, serializer):
        """CommentViewSetUpdate."""
        if self.request.user != serializer.instance.author:
            raise PermissionDenied()
        serializer.save(author=self.request.user, status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        """CommentViewSetDestroy."""
        if self.request.user != instance.author:
            raise PermissionDenied()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)