from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment, Like
from rest_framework import permissions  
from rest_framework import generics, status
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
from .serializers import PostSerializer, CommentSerializer, LikeSerializer

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
    

class LikePostView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        post = generics.get_object_or_404(Post, pk=self.kwargs['post_id'])

        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response(
                {'detail': 'You have already liked this post.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if request.user != post.author:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.id
            )
        
        serializer = self.get_serializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UnlikePostView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        post = generics.get_object_or_404(Post, pk=pk)
        return generics.get_object_or_404(
            Like,
            user=self.request.user,
            post=post
        )