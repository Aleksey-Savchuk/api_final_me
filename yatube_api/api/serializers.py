"""serializers_api."""
from posts.models import Comment, Group, Post
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    """GroupSerializer."""

    class Meta:
        """GroupSerializerMeta."""
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """CommentSerializer."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """CommentSerializerMeta."""
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class PostSerializer(serializers.ModelSerializer):
    """PostSerializer."""
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """PostSerializerMeta."""
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
