from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from rest_framework import permissions  
from rest_framework import generics
from .serializers import PostSerializer, CommentSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_class = [permissions.IsAuthenticated]

    def get_queryset(self):
        following_users = self.request.user.following.all()

        return Post.objects.filter(author__in=following_users).order_by('-created_at')
