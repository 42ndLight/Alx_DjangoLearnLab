from .views import PostViewSet, CommentViewSet, UserFeedView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='feed'),
    path('', include(router.urls))
    ]