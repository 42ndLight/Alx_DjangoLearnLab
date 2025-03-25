from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
urlpatterns = router.urls