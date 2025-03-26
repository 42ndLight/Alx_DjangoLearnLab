from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment
from rest_framework.permissions import IsAuthenticated
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
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        following_user = self.request.user.follwing.all()

        return Post.objects.filter(author__in=following_user).order_by('-created_at')
