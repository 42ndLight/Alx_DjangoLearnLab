from django.shortcuts import render
from rest_framework import viewset
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Create your views here.
class PostViewSet(viewset.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(viewset.ModelViewSet):
    queryset = Comment.objcts.all()
    serializer_class = CommentSerializer
