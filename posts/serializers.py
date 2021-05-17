from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'text', 'image', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
