from django.urls import path
from .views import search_posts, tag_posts, profile_view, register, user_login, user_logout, ListPostView, DetailPostView, CreatePostView, UpdatePostView, DeletePostView, CommentCreateView, CommentDeleteView, CommentUpdateView, CommentListView

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('posts', ListPostView.as_view(), name='index'),
    path('post/<int:pk>', DetailPostView.as_view(), name='detail'),
    path('post/new/', CreatePostView.as_view(), name='create'),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='create_comment'),
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='list-comments'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='update-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete-comment'),
    path('search/', search_posts, name='search_posts'),
    path('tags/<str:tag_name>/', tag_posts, name='tag_posts'),
]