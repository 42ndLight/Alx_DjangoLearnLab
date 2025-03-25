from .models import Post, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    model = Comment
    fields = ['id', 'user', 'content', 'created_at']
    read_only_fields = ['user', 'created_at']
    

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comment = CommentSerializer(many=True, read_only=True)

    model = Post
    fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']
    read_only_fields = ['author', 'created_at', 'updated_at']
    
